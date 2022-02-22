import requests
import json

url = "http://localhost:5000/v1/admin/user/"

payload = json.dumps({
  "firstName": "subash11",
  "lastName": "Timalsina",
  "countryCode": "+977",
  "role": "user",
  "profilePhoto": "https://www.howtogeek.com/wp-content/uploads/2018/06/shutterstock_1006988770.png",
  "email": "hello111a1@gmail.com",
  "phoneNumber": "98493112716"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
