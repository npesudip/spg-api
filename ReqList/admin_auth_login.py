import requests
import json

url = "https://devapi.red.global/v1/admin/auth/login"

payload = json.dumps({
  "email": "admin@spg.com",
  "password": "admin@123"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=payload)
json_response = response.json()

print(json_response)
