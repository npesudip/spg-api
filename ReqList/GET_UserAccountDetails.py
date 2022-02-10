import requests
import json
from utils.print_helpers import pretty_print
from utils.config import uri

get_page_details = "v1/api/page?pageType=privacyPolicy"

url = uri + get_page_details
payload = ""
headers = {}

response = requests.get(url=url, headers=headers, data=payload)
status_code = response.status_code
pretty_print(response.text)
print("Status Code  :", status_code)
print("Headers      :", headers)
print("BaseURL      :", url)


def test_verify_status_code_is_200():
    assert status_code == 200, "Status Code Do Not Matched"

