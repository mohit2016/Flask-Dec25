import pytest
from loan import app


# client -> act as a server to send requests to the flask app
@pytest.fixture
def client():
    return app.test_client()


def test_home(client):
    resp = client.get('/') # sending a GET request to the home endpoint
    assert resp.status_code == 200
    assert resp.text == "<h1>Welcome to the Loan Application Service! V2</h1>"


def test_predict(client):
    data = {
        "Gender": "Male",
        "Married": "No",
        "ApplicantIncome": 5000,
        "LoanAmount": 20,
        "CreditHistory": 1
    }
    resp = client.post('/predict', json=data) 
    assert resp.status_code == 200
    assert resp.json == {"loan_approval_status": "Approved"}    



# import requests
# requests.get('/')
# requests.post('/predict', json={})