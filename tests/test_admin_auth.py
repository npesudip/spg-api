import requests
import json
import pytest
from utils.print_helpers import pretty_print
from assertpy import assert_that

register_payload = json.dumps({
    "email": "sudip.ebp@gmail.com",
    "password": "admin@123"
})
register_headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'
                     '.eyJ1c2VyIjoiNjIwZTA2MjJlZWViNjY2ZDQ2Y2I3YWVlIiwiaWF0IjoxNjQ1NDMxODQ0LCJleHAiOjE2NDU1MTgyNDR9'
                     '.B0Cpn4D7nbP7YziqMMXN4egCxchPLNYKv1nRSY-Cc_k',
    'Content-Type': 'application/json'
}

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


def test_login_with_admin():
    url = "https://devapi.red.global/v1/admin/auth/register"
    response = requests.post(url, headers=register_headers, data=register_payload)
    assert_that(response.status_code).is_equal_to(200)


def test_register_new_user():
    url = "https://devapi.red.global/v1/admin/auth/register"
    response = requests.request("POST", url, headers=register_headers, data=register_payload)
    pretty_print(response.text)
    assert_that(response.status_code).is_equal_to(200)

def test_login_new_user():
    """
    login with user
    """
    url = "https://devapi.red.global/v1/admin/auth/login"
    response = requests.request("POST", url, headers=headers, data=payload)
    pretty_print(response.json())
    assert_that(response.status_code).is_equal_to(200)
