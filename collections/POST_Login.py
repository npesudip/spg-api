import requests
import json
from utils.print_helpers import pretty_print
from TestData.people import name
from utils.config import uri

login_url = "/v1/api/user/login"

name = name
# print(name)
url = uri + login_url
print(url)

payload = json.dumps({
    "email": "admin@spg.com",
    "password": "admin@123"
})
headers = {
    'Authorization': '{{token}}',
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=payload)
status_code = response.status_code
print(status_code)
pretty_print(response.text)
assert status_code == 204, "Status Code Do Not Matched"