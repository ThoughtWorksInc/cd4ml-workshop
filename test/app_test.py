import requests

def test_endpoint():
    query_params = '?date=2017-06-14&item_nbr=99197';
    resp = requests.get('http://localhost:5005/prediction' + query_params);

    assert resp.status_code == 200
