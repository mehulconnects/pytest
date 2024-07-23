import pytest
class PostHelper:

    postdata = {
        "name": "Mehul",
        "job": "QAE"
    }

    post_url = "https://reqres.in/api/users"

class PostJSONHelper:
    PostJSONurl = 'https://reqres.in/api/users'
    PostJSONresponse_header = 'Connection'
    PostJSONresponse_id = 'id'