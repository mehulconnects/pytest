import requests
url = 'https://reqres.in/api/users/2'

def test_deleteAPI():
    #delete method
    del_response = requests.delete(url)

    #fetch response code
    print(del_response.status_code)
    assert del_response.status_code == 204
    if del_response.status_code == 204:
        print('recod deleted')
    else:
        print('Deletion failed')

    # The recod is not deleted as this is a testing API (shows deleted but not deleted actually)
    get_request = requests.get(url)
    print(get_request.text)
