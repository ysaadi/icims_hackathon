"""
Non-documented API endpoints for ICIMS
    - create_companies
    - list myCompanies
Uses browser cookie. Set in envvar
"""
import requests
import random
from os import environ

# This uses a personal cookie so do not share you cookie.
# You can find your cookie via Internet Browser tools.
# Cookie name is: "icims.hack.user"
# Should be a dictionary
# {"icims.hack.user": "FAKE_COOKIE_VALUE; path=/; domain=.hackicims.com; Expires=Tue, 19 Jan 2038 03:14:07 GMT;"}
cookie_value = environ['COOKIE_VALUE']
cookie = {"icims.hack.user": cookie_value}

# Update this list with whatever company names you want. If you need a lot, consider using a small rainbow table
COMPANY_NAMES = ["mcds", "cafe", "hyundai", "trump", "russia"]

base_url = "https://hackicims.com/docs-api/%s"
headers = {"content-type": "application/json"}

# Ranges are updateable and can be changed to whatever range you feel appropriate
def create_companies(names):
    base_payload = "{\"name\":\"%s\",\"numJobs\":%d,\"numPeople\":%d,\"numApps\":%d}"
    endpoint = "createCompany"
    for name in names:
        company_name = name
        num_jobs = random.randint(15,50)
        num_people = random.randint(200,654)
        num_apps = random.randint(num_people-50,num_people+16)
        payload = base_payload % (company_name, num_jobs, num_people, num_apps)
        r = requests.post(base_url % endpoint,headers=headers,cookies=cookie,data=payload)
        #print(payload % (company_name, num_jobs, num_people, num_apps))

def list_companies(): #returns list of dicts
    endpoint = "myCompanies"
    r = requests.get(base_url % endpoint,cookies=cookie)
    return r.json()
