"""
this is one time test - first login with admin.
"""

import requests
import json
from utils.print_helpers import pretty_print
from assertpy import assert_that

url = "https://devapi.red.global/v1/admin/auth/register"

payload = json.dumps({
  "fullName": "Test User",
  "profilePhoto": None,
  "role": "spgSuperAdmin",
  "title": "Head",
  "email": "1testebp@gmail.com",
  "password": "admin@123",
  "countryCode": "+977",
  "contactNumber": "9849036338",
  "monitoringCentre": None,
  "entity": None
})
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'
                   '.eyJ1c2VyIjoiNjIwZTA2MjJlZWViNjY2ZDQ2Y2I3YWVlIiwiaWF0IjoxNjQ1NDMxODQ0LCJleHAiOjE2NDU1MTgyNDR9'
                   '.B0Cpn4D7nbP7YziqMMXN4egCxchPLNYKv1nRSY-Cc_k',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

pretty_print(response.text)

assert_that(response.status_code).is_equal_to(201)
