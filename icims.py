#!/usr/bin/python3
import requests
import json
import os
from flask import Flask, jsonify, make_response, abort, request, render_template
from flask_restful import Api, Resource, reqparse
from python.starter import *
from extra_endpoints import *

COOKIE_VALUE = os.environ['COOKIE_VALUE']
print(COOKIE_VALUE)
API_KEY = os.environ['API_KEY']
print(API_KEY)

cookie = {"icims.hack.user": COOKIE_VALUE}
print(cookie)

app = Flask(__name__)

headers = {"Authorization": "Bearer " + API_KEY, "Content-Type":"application/json"}

'''
Show default page
'''
@app.route('/')
def showPage():
    return render_template('index.html')

'''
Get all companies information
'''
@app.route('/companies')
def getCompanies():
    r = requests.get("https://hackicims.com/docs-api/myCompanies", cookies=cookie)
    print(r.json())
    return json.dumps(r.json())

'''
Get all candidates for a company
'''
@app.route('/company/<string:companyId>/candidates')
def getCandidates(companyId):
    print(companyId)
    r = requests.get("http://hackicims.com/api/v1/companies/"+ companyId + "/people", headers=headers)
    print(json.dumps(r.json()))
    return json.dumps(r.json())

@app.route('/company/analysis')
def analysis():
    myDict = {}

    comp_list = get_company_id_and_name_list(True)
    for company, name in comp_list:
        myDict[name] = {}
        applications = get_company_application_info(company).json()
        for app in applications:
            if app['status'] in myDict[name]:
                myDict[name][app['status']] += 1
            else:
                myDict[name][app['status']] = 1
    return json.dumps(myDict)




if __name__ == '__main__':
    app.run(debug=True)

#curl -X GET https://hackicims.com/api/v1/companies/32/jobs -H 'Authorization: Bearer <API_KEY>' -H 'Content-Type: application/json' | jq .
# GET Request to get company information
#headers = {"Authorization": "Bearer " + API_KEY,"Content-Type":"application/json"}
#r = requests.get("https://hackicims.com/api/v1/companies/32", headers=headers)
# print(r.json())
# Do something with r.json() or r.text
# Status codes can be checked with r.status_code

# POST Request to make a job post named Software Developer for company 2002
# payload = json.JSONEncoder().encode({"title": "Software Developer"})
# r = requests.post("https://hackicims.com/api/v1/companies/2002/jobs", data=payload, headers=headers)
# Status codes can be checked with r.status_code

