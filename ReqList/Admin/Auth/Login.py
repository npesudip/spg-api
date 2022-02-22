"""
test -2 :
-- Login with admin user
-- first register a user from admin
-- now login with new user
"""

import requests
import json
from utils.print_helpers import pretty_print
from assertpy import assert_that

url = "https://devapi.red.global/v1/admin/auth/login"

payload = json.dumps({
  "email": "sudip.ebp@gmail.com",
  "password": "admin@123"
})
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'
                   '.eyJ1c2VyIjoiNjIwZTA2MjJlZWViNjY2ZDQ2Y2I3YWVlIiwiaWF0IjoxNjQ1NDMxODQ0LCJleHAiOjE2NDU1MTgyNDR9'
                   '.B0Cpn4D7nbP7YziqMMXN4egCxchPLNYKv1nRSY-Cc_k',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

pretty_print(response.json())

assert_that(response.status_code).is_equal_to(200)
