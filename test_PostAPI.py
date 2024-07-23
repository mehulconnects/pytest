import requests
import Helperlib

print(Helperlib.PostHelper.postdata)

# Sending the POST request
response = requests.post(Helperlib.PostHelper.post_url, json=Helperlib.PostHelper.postdata)

# Print the response status code
print("Response Code:", response.status_code)

# Print the response content
print("Response Content:", response.json())