#!/usr/bin/python3
import requests
import json
import os

API_KEY = os.environ['API_KEY']
print(API_KEY)

#curl -X GET https://hackicims.com/api/v1/companies/32/jobs -H 'Authorization: Bearer <API_KEY>' -H 'Content-Type: application/json' | jq .
# GET Request to get company information
headers = {"Authorization": "Bearer e0add267c28fb96c6ff77194434d446d4dd3faadc996be6f9e2af00a5f425bb59a4609ea62e1040c0b42228dfd4cf695ecb56f771bfb43d44f67819fc5155473","Content-Type":"application/json"}
r = requests.get("https://hackicims.com/api/v1/companies/32", headers=headers)
print(r.json())
# Do something with r.json() or r.text
# Status codes can be checked with r.status_code

# POST Request to make a job post named Software Developer for company 2002
# payload = json.JSONEncoder().encode({"title": "Software Developer"})
# r = requests.post("https://hackicims.com/api/v1/companies/2002/jobs", data=payload, headers=headers)
# Status codes can be checked with r.status_code

