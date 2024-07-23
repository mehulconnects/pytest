import requests
import pytest
import Helperlib



# This fixture will be executed whereever its called as a parameter
# code written before yield will be executed fist before code in the calling function and
# code written after yield will be executed after code in the calling function
@pytest.fixture(scope='module')
def setup_teardown():
    print("\nThis is a pre-req")
    # This is where all the CVEs will be posted
    yield  # everything above this will be executed before the function and below this will be executed after the function
    print("\nThis is teardown")
    # This is where the delete method will be called

# marked test cases could be filtered and called for execution using below command
# pytest -m fixture name i.e. pytest -m regression

@pytest.mark.regression
def test_getuserdata(setup_teardown):
    url = 'https://reqres.in/api/users?page=2'
    response = requests.get(url)
    print(response.status_code)
    assert response.status_code == 200
    #print(response.json())

test_getuserdata(setup_teardown)

@pytest.mark.xfail
def test_getuserdata1(setup_teardown):
    url = 'https://reqres.in/api/users?page=2'
    response = requests.get(url)
    print(response.status_code)
    assert response.status_code == 200, "getuserdata1 failed as statuscode was 200 instead of 201"
    print(response.json())

test_getuserdata1(setup_teardown)