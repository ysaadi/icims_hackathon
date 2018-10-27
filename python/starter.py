import requests
import json
from os import environ

COOKIE_VALUE = environ['COOKIE_VALUE']

API_KEY = environ["API_KEY"]

base_url = "https://hackicims.com/api/v1/companies/%s/%s/%s"

headers = {"Authorization": "Bearer " + API_KEY}

def get_company_application_info(company_id, id=''):
    url = base_url % (company_id, "applications" , id)
    r = requests.get(url, headers=headers)
    return r

def get_company_people_info(company_id, id=''):
    url = base_url % (company_id, "people" , id)
    r = requests.get(url, headers=headers)
    return r

def get_company_job_info(company_id, id=''):
    url = base_url % (company_id, "applications" , id)
    r = requests.get(url, headers=headers)
    return r


def seed_data(company_id, index_name):
    headers = {"Content-Type": "application/json"}
    es_base_url = "https://search-icims-hack-56-4ojyhi66tg25f2gpnb6p3dbv4y.us-east-2.es.amazonaws.com/%s/%s/%s"
    type_id = 0
    # change the function that pulls the different types of data: people, application, jobs
    people = get_company_people_info(company_id).json()
    for person in people:
        payload = json.dumps(person)
        r = requests.put(es_base_url % (index_name,"person",type_id), headers=headers, data=payload)
        type_id += 1
        print(f"Person {person['id']}: seeded. Status: {r.status_code}")


myList = [
 (31, 'yamansaadi'),
 (73, 'mcds'),
 (74, 'cafe'),
 (75, 'hyundai'),
 (76, 'meepo'),
 (77, 'jakiro'),
 (78, 'nausicaa'),
 (79, 'sneevil')
 ]