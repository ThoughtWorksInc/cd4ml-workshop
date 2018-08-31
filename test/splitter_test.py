import sys
import os
import pandas as pd
sys.path.append(os.path.join('..', 'src'))
sys.path.append(os.path.join('src'))
import splitter

def test_get_validation_period():
    latest_date = pd.to_datetime('2017-11-22')
    actual_begin_date, actual_end_date = splitter.get_validation_period(latest_date)
    expected_begin_date = pd.to_datetime('2017-11-01')
    expected_end_date = pd.to_datetime('2017-11-16')
    assert actual_begin_date == expected_begin_date
    assert actual_end_date == expected_end_date

def test_split_validation_train_by_validation_period():
    date1 = pd.to_datetime('2017-11-12')
    date2 = pd.to_datetime('2017-11-25')
    date3 = pd.to_datetime('2017-11-30')
    date4 = pd.to_datetime('2017-12-01')
    validation_begin_date = pd.to_datetime('2017-11-15')
    validation_end_date = pd.to_datetime('2017-11-30')
    d = {'date': [date1, date2, date3, date4], 'col2': [3, 4, 5, 6]}
    df = pd.DataFrame(data=d)
    df_train, df_validation = splitter.split_validation_train_by_validation_period(df, validation_begin_date, validation_end_date)
    assert df_train.shape[0] == 1
    assert df_validation.shape[0] == 2
