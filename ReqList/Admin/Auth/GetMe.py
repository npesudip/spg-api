import requests

url = "https://devapi.red.global/v1/admin/auth/refresh-token"

payload = {}
headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'
                     '.eyJ1c2VyIjoiNjIxMzRjOGU4Mzg1OGM5NjNiYjQ4MzhhIiwiaWF0IjoxNjQ1NDM5MzE0LCJleHAiOjE2NDU1MjU3MTR9'
                     '.-ALbQTjkDOr9eHixELrEvAzR9W3I1N2u77xSvMhK68M',
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
