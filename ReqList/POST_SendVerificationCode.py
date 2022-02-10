import requests
import json

from utils.config import uri
from SRS.endPoints import Ver_1_mobile

path = Ver_1_mobile.Send_Mobile_Verification_Code
url = uri + path

# Test Data
f = open("../Reports/phoneNumbers.txt", "r")
contactNumber = f.read()
print(contactNumber)

payload = json.dumps({
    "phoneCode": "+977",
    "countryCode": "NP",
    "contactNumber": str(contactNumber),
    "isResend": False
})
headers = {
    'Authorization': 'token',
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=payload)
status_code = response.status_code
print('response Json : ', response.json())

print(status_code)
print(response.json()["message"])
assert status_code == 201, "Satus code did not matched"
assert response.json()["message"] == 'OTP verification code has been sent to your contact.'
print(status_code)
print(response.json()["message"])
