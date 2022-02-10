import faker.providers.date_time
import requests
import json
from json import dumps
from uuid import uuid4
from faker import Faker
import random

from utils.print_helpers import pretty_print
from utils.config import uri


fake = Faker()
fullName = fake.name()
singleName = fullName.replace(" ","_")
email = singleName.lower()+"@gmail.com"
print(email)

contactNumber = random.randint(9800000000, 9899999999)
print(contactNumber)
print(type(contactNumber))

post_register = "v1/admin/auth/register"
url = uri+post_register
print(url)

payload = json.dumps({
  "fullName": fullName,
  "profilePhoto": None,
  "role": "spgSuperAdmin",
  "title": "Head",
  "email": email,
  "password": "admin@123",
  "phoneCode": "+977",
  "countryCode": "NP",
  "contactNumber": contactNumber,
  "codeContactNumber": "+977"+str(contactNumber),
  "monitoringCentre": None,
  "entity": None
})
headers = {
  'Authorization': 'token',
  'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=payload)
status_code = response.status_code
# pretty_print(response.text)
pretty_print(response.json())

assert status_code == 201, "Satus code did not matched"
assert response.json()["data"]["contactNumber"] == str(contactNumber), "Contact Number Mismatched"
assert response.json()["data"]["fullName"] == str(fullName), "Contact Number Mismatched"
assert response.json()["message"] == 'Your profile is good to go!', 'success message mismatch'
