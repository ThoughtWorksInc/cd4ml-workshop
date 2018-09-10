import requests

def test_endpoint():
    query_params = '?day_off=false&perishable=false&date=2017-06-14&item_nbr=99197&family=GROCERY%20I&class=1067&transactions=4170';
    resp = requests.get('http://localhost:5005/prediction' + query_params);

    assert resp.status_code == 200
