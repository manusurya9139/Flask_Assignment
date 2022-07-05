import pytest
import requests

main_url = "http://127.0.0.1:5000"
# Pytest for SEQUENCE
def test_get_sequence_valid_odd_input():
    valid_url = main_url + "/sequence/elem/11"
    response = requests.get(valid_url)
    resp = response.json()
    assert response.status_code == 200
    assert resp['data'] == '11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1'
    assert resp['status'] == 0
    assert resp['message'] == 'Success'

def test_get_sequence_valid_even_input():
    valid_url = main_url + "/sequence/elem/20"
    response = requests.get(valid_url)
    resp = response.json()
    assert response.status_code == 200
    assert resp['data'] == '20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1'
    assert resp['status'] == 0 
    assert resp['message'] == 'Success'

def test_get_sequence_invalid_input():
    invalid_url = main_url + "/sequence/elem/invalid"
    response = requests.get(invalid_url)
    resp = response.json()
    assert response.status_code == 200
    assert resp['message'] == 'Please provide integer value as input.'
    assert resp['status'] == -1
    assert resp['data'] == []

def test_get_max_sequence_valid_input():
    valid_url = main_url + "/sequence/longest/11"
    response = requests.get(valid_url)
    resp = response.json()

    assert response.status_code == 200
    assert resp['data'] == 9
    assert resp['status'] == 0
    assert resp['message'] == 'Success'

def test_get_max_sequence_invalid_input():
    invalid_url = main_url + "/sequence/longest/invalid"
    response = requests.get(invalid_url)
    resp = response.json()

    assert response.status_code == 200
    assert resp['data'] == []
    assert resp['status'] == -1
    assert resp['message'] == 'Please provide integer value as input.'


#Pytest for IRIS and
def test_iris_get_max_sepal_len(mocker):
    url = main_url + "/iris/group/sepal_length/2"
    response = requests.get(url)

    assert response.status_code == 200
    assert "sepal_length" in response.text
    assert "sepal_width" in response.text
    assert "petal_length" in response.text
    assert "petal_width" in response.text
    assert "species" in response.text


def test_iris_describe(mocker):
    url = main_url + "/iris/describe"
    response = requests.get(url)

    assert response.status_code == 200
    assert "sepal_length" in response.text
    assert "sepal_width" in response.text
    assert "petal_length" in response.text
    assert "petal_width" in response.text
    assert "count" in response.text
    assert "mean" in response.text
    assert "std" in response.text
    assert "min" in response.text
    assert "25%" in response.text
    assert "50%" in response.text
    assert "75%" in response.text
    assert "max" in response.text

