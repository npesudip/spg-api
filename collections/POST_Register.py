import faker.providers.date_time
import requests
import json
from json import dumps
from uuid import uuid4
from faker import Faker


from utils.print_helpers import pretty_print
from utils.config import uri


fake = Faker()
fullName = fake.name()
singleName = fullName.replace(" ","_")
email = singleName+"@gmail.com"
print(email)


post_register = "/v1/admin/auth/register"
url = uri+post_register

payload = json.dumps({
  "fullName": fullName,
  "profilePhoto": None,
  "role": "user",
  "title": "Head",
  "email": "admin@spg.com",
  "password": "admin@123",
  "phoneCode": "+977",
  "countryCode": "NP",
  "contactNumber": "9840015130",
  "codeContactNumber": "+9779840015130",
  "monitoringCentre": None,
  "entity": None
})
headers = {
  'Authorization': 'token',
  'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=payload)
status_code = response.status_code
print(response.text)

assert status_code == 204, " Status code did not match "
