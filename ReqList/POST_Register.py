import json
from datetime import datetime

import requests

from TestData.people import People
from utils.config import uri
from utils.print_helpers import pretty_print

current_date_and_time = datetime.now()
current_date_and_time_string = str(current_date_and_time)
extension = ".txt"

post_register = "v1/admin/auth/register"
url = uri + post_register

# Test Data Generations
fullName = People.fullName
email = People.email
contactNumber = People.contactNumber

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
    "codeContactNumber": "+977" + str(contactNumber),
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

# storing this number to the file for sending verification code
file_name = current_date_and_time_string + extension
print(file_name)
f = open("../Reports/"+str(file_name), "x")
f.write(str(contactNumber))
