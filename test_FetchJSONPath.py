import json
import requests
import jsonpath
import pytest


@pytest.mark.test1
def test_FetchJSONPath():
    url = 'https://reqres.in/api/users?page=2'

    response = requests.get(url)
    print(response)
    print(response.status_code)

    #parse response to json format
    json_response = json.loads(response.text)
    print(json_response)

    #Fetch value using json path
    # METHOD 2
    pages = jsonpath.jsonpath(json_response,'total_pages')
    print(pages[0])
    assert pages[0] == 2

    #Fetch value using json path
    # METHOD 1

    j = response.json()
    print (j['page'])
    emailresult = j['data'][1]['email']
    print (emailresult)
    assert emailresult == 'lindsay.ferguson@reqres.in'

test_FetchJSONPath()