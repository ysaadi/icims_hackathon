"""
Running this file will seed your local MongoDB with the company, application, and people data
Usage: python starter.py
"""
import requests
import json
import extra_endpoints
import os
from os import environ
from pymongo import MongoClient
from extra_endpoints import *

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

def save_data(company_id, company_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    json_dir=os.path.join(dir_path, 'json_data')
    if(not os.path.isdir(json_dir)):
      os.mkdir(json_dir)
    with open(os.path.join(json_dir, company_name+'_'+'people'), 'w+') as people_json:
      people = get_company_people_info(company_id).json()
      json.dump(people, people_json)
    with open(os.path.join(json_dir, company_name+'_'+'applications'), 'w+') as applications_json:
      applications = get_company_application_info(company_id).json()
      json.dump(applications, applications_json)
    with open(os.path.join(json_dir, company_name+'_'+'jobs'), 'w+') as jobs_json:
      jobs = get_company_job_info(company_id).json()
      json.dump(jobs, jobs_json)

def seed_data(company_id, index_name):
    headers = {"Content-Type": "application/json"}
    # index, type, id
    es_base_url = "https://search-icims-hack-56-4ojyhi66tg25f2gpnb6p3dbv4y.us-east-2.es.amazonaws.com/%s/%s/%s"
    type_id = 0
    # change the function that pulls the different types of data: people, application, jobs
    #people = get_company_people_info(company_id).json()
    #for person in people:
    #    payload = json.dumps(person)
    #    r = requests.put(es_base_url % (index_name,"person",type_id), headers=headers, data=payload)
    #    type_id += 1
    #    print(f"Person {person['id']}: seeded. Status: {r.status_code}")
    type_id = 0
    applications = get_company_application_info(company_id).json()
    for application in applications:
        payload = json.dumps(application)
        r = requests.put(es_base_url % (index_name,"application",type_id), headers=headers, data=payload)
        type_id += 1
        print(f"Application {application['id']}: seeded. Status: {r.status_code}")
    type_id = 0
    jobs = get_company_job_info(company_id).json()
    for job in jobs:
        payload = json.dumps(job)
        r = requests.put(es_base_url % (index_name,"job",type_id), headers=headers, data=payload)
        type_id += 1
        print(f"Job {job['id']}: seeded. Status: {r.status_code}")

def seed_mongo_people(company_id):
    client = MongoClient('localhost', 27017)
    db = client.icims
    people = db.people
    collection_l = get_company_people_info(company_id).json()
    counter = 0    
    for entry in collection_l:
        entry['uid'] = counter
        result = people.insert_one(entry)
        print(f"result: {result.inserted_id} ")
        print(f"{entry['firstName']} has been seeded")
        counter += 1

def seed_mongo_applications(company_id):
    client = MongoClient('localhost', 27017)
    db = client.icims
    applications = db.applications
    collection_l = get_company_application_info(company_id).json()
    counter = 0    
    for entry in collection_l:
        entry['aid'] = counter
        result = applications.insert_one(entry)
        print(f"result: {result.inserted_id} ")
        print(f"{entry['jobId']} has been seeded")
        counter += 1

def seed_mongo_companies():
    client = MongoClient('localhost', 27017)
    db = client.icims
    companies = db.companies
    collection_l = list_companies()
    counter = 0    
    for entry in collection_l:
        entry['cid'] = counter
        result = companies.insert_one(entry)
        print(f"result: {result.inserted_id} ")
        print(f"{entry['companyId']} has been seeded")
        counter += 1

def get_company_id_and_name_list(name=False):
    h = list_companies()
    if name == False:
        myList = [compId['companyId'] for compId in h]
        return myList
    myList_with_names = [(compId['companyId'],compId['name']) for compId in h]
    return myList_with_names

if __name__ == "__main__":
    #list_of_company_ids = get_company_id_list()
    #seed_mongo_companies()
    #for company_id in list_of_company_ids:
    #    seed_mongo_applications(company_id)
    #    seed_mongo_people(company_id)
    #companies=extra_endpoints.list_companies()
    companies={
      '31': 'Yaman Saadi',
      '73': 'mcds',
      '74': 'cafe',
      '75': 'hyndai',
      '76': 'meepo',
      '77': 'Jakiro',
      '78': 'Nausicaa',
      '79': 'sneevil'
    }
    for company in companies.keys():
      #companyId=company['companyId']
      #companyName=company['name'].lower().replace(" ", "")
      #seed_data(companyId,companyName)
      save_data(company, companies[company])
