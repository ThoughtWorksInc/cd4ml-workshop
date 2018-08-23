from flask import Flask, render_template, jsonify, request
from datetime import datetime
from sklearn.externals import joblib
import pandas as pd
import decision_tree

app = Flask(__name__, template_folder='webapp/templates', static_folder='webapp/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction')
def get_prediction():
  loaded_model = joblib.load('data/decision_tree/model.pkl')

  date_string = request.args.get('date')

  date = datetime.strptime(date_string, '%Y-%m-%d')

  data = {
    "date": date_string,
    "store_nbr": request.args.get("store_nbr"),
    "item_nbr": request.args.get("item_nbr"),
    "onpromotion": request.args.get("onpromotion"),
    "city": "Quito",
    "state": "Pichincha",
    "cluster": request.args.get("cluster"),
    "family": request.args.get("family"),
    "class": request.args.get("class"),
    "perishable": request.args.get("perishable"),
    "transactions": request.args.get("transactions"),
    "year": date.year,
    "month": date.month,
    "day": date.day,
    "dayofweek": date.weekday(),
    "days_til_end_of_data": 0,
    "cpi": 105.55273726978949,
    "dayoff": request.args.get("day_off")
  }
  df = pd.DataFrame(data=data, index=['row1'])

  df = decision_tree.encode_categorical_columns(df)
  pred = loaded_model.predict(df)

  return "%d" % pred[0]

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5005)