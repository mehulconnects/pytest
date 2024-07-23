import jsonpath
import requests
import json
import Helperlib

def test_postAPI():

    # Read postdata.json file
    file = open('postdata.json','r')
    json_input = file.read()
    #convert text to json for parsing
    request_json = json.loads(json_input)
    print(request_json)
    # Make post request with json input body
    response = requests.post(Helperlib.PostJSONHelper.PostJSONurl,request_json)
    print(response.status_code)
    print(response.text)
    #Validating Respose code
    assert response.status_code == 201
    # Fetch header from the respose
    response_header = response.headers.get(Helperlib.PostJSONHelper.PostJSONresponse_header)
    print(response_header)
    #parse response to json format
    respose_json = json.loads(response.text)
    # Pick ID using Json path
    id = jsonpath.jsonpath(respose_json,Helperlib.PostJSONHelper.PostJSONresponse_id)
    print(id[0])