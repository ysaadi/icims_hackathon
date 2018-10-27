import requests
import json
from os import environ

COOKIE_VALUE = environ['COOKIE_VALUE']

API_KEY = "be5bba71add4ce76a6f85e528491b23cf9e151787cb1aa1e9a7726b3737719b96943e68b037912cee6c60da4724926900d6f6a1141a7584a6d5686efdc038647"

base_url = "https://hackicims.com/api/v1/companies/%s/%s/%s"

headers = {'Authorization': "Bearer be5bba71add4ce76a6f85e528491b23cf9e151787cb1aa1e9a7726b3737719b96943e68b037912cee6c60da4724926900d6f6a1141a7584a6d5686efdc038647"}

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
