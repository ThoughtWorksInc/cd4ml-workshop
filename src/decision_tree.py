from enum import Enum
import numpy as np
import pandas as pd
import sys, os, json
from sklearn.preprocessing import LabelEncoder
from sklearn.externals import joblib
sys.path.append(os.path.join('..', 'src'))
sys.path.append(os.path.join('src'))
from sklearn import tree, ensemble, metrics
import evaluation
import tracking

class Model(Enum):
    DECISION_TREE = 0
    RANDOM_FOREST = 1
    ADABOOST = 2
    GRADIENT_BOOST = 3


def load_data():
    filename = "data/splitter/train.csv"
    print("Loading data from {}".format(filename))
    train = pd.read_csv(filename)

    filename = 'data/splitter/validation.csv'
    print("Loading data from {}".format(filename))
    validate = pd.read_csv(filename)

    return train, validate


def join_tables(train, validate):
    print("Joining tables for consistent encoding")
    return train.append(validate).drop('date', axis=1)


def encode_categorical_columns(df):
    obj_df = df.select_dtypes(include=['object', 'bool']).copy().fillna('-1')
    lb = LabelEncoder()
    for col in obj_df.columns:
        df[col] = lb.fit_transform(obj_df[col])
    return df


def encode(train, validate):
    print("Encoding categorical variables")
    train_ids = train.id
    validate_ids = validate.id

    joined = join_tables(train, validate)

    encoded = encode_categorical_columns(joined.fillna(-1))

    print("Not predicting returns...")
    encoded.loc[encoded.unit_sales < 0, 'unit_sales'] = 0

    validate = encoded[encoded['id'].isin(validate_ids)]
    train = encoded[encoded['id'].isin(train_ids)]
    return train, validate


def train_model(train, model=Model.DECISION_TREE, seed=None):
    print("Training model using regressor: {}".format(model.name))
    train_dropped = train.drop('unit_sales', axis=1)
    target = train['unit_sales']

    if model == Model.RANDOM_FOREST:
        params = {'n_estimators': 10}
        clf = ensemble.RandomForestRegressor(random_state=seed, **params)
    elif model == Model.ADABOOST:
        params = {'n_estimators': 50, 'learning_rate': 1.0, 'loss':'linear'}
        clf = ensemble.AdaBoostRegressor(random_state=seed, **params)
    elif model == Model.GRADIENT_BOOST:
        params = {'n_estimators': 200, 'max_depth': 4}
        clf = ensemble.GradientBoostingRegressor(random_state=seed, **params)
    else:
        params = {'criterion': 'mse'}
        clf = tree.DecisionTreeRegressor(random_state=seed)

    trained_model = clf.fit(train_dropped, target)
    return (trained_model,params)


def overwrite_unseen_prediction_with_zero(preds, train, validate):
    cols_item_store = ['item_nbr', 'store_nbr']
    cols_to_use = validate.columns.drop('unit_sales') if 'unit_sales' in validate.columns else validate.columns
    validate_train_joined = pd.merge(validate[cols_to_use], train, on=cols_item_store, how='left')
    unseen = validate_train_joined[validate_train_joined['unit_sales'].isnull()]
    validate['preds'] = preds
    validate.loc[validate.id.isin(unseen['id_x']), 'preds'] = 0
    preds = validate['preds'].tolist()
    return preds


def make_predictions(model, validate):
    print("Making prediction on validation data")
    validate_dropped = validate.drop('unit_sales', axis=1).fillna(-1)
    validate_preds = model.predict(validate_dropped)
    return validate_preds


def write_predictions_and_score(evaluation_metrics, model, columns_used):
    key = "decision_tree"
    if not os.path.exists('data/{}'.format(key)):
        os.makedirs('data/{}'.format(key))
    filename = 'data/{}/model.pkl'.format(key)
    print("Writing to {}".format(filename))
    joblib.dump(model, filename)

    filename = 'results/metrics.json'
    print("Writing to {}".format(filename))
    if not os.path.exists('results'):
        os.makedirs('results')
    with open(filename, 'w+') as score_file:
        json.dump(evaluation_metrics, score_file)


def main(model=Model.DECISION_TREE, seed=None):
    original_train, original_validate = load_data()
    train, validate = encode(original_train, original_validate)
    with tracking.track() as track:
        track.set_model(model)
        model, params = train_model(train, model, seed)
        track.log_params(params)
        validation_predictions = make_predictions(model, validate)

        print("Calculating metrics")
        evaluation_metrics = {
            'nwrmsle': evaluation.nwrmsle(validation_predictions, validate['unit_sales'].values, validate['perishable'].values),
            'r2_score': metrics.r2_score(y_true=validate['unit_sales'].values, y_pred=validation_predictions)
        }
        track.log_metrics(evaluation_metrics)

        write_predictions_and_score(evaluation_metrics, model, original_train.columns)

        print("Evaluation done with metrics {}.".format(json.dumps(evaluation_metrics)))


if __name__ == "__main__":
    main(model=Model.DECISION_TREE, seed=8675309)
