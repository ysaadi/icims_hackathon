from starter import *

company_id = 31
#applications = get_company_application_info(company_id)
#people = get_company_people_info(company_id)

# Random analysis. Returns dictionary of how many people attended specific school
def school_analysis(company_id):
    myDict = {}
    people = get_company_people_info(company_id)
    for person in people.json():
        education_l = person['education']
        if education_l: 
            for education in education_l:
                if education['school'] in myDict:
                    myDict[education['school']] += 1
                else:
                    myDict[education['school']] = 1
    return myDict

comp_list = get_company_id_and_name_list(True)

def full_analysis(list_of_company_ids):
    myDict = {}
    comp_list = get_company_id_and_name_list(True)
    for company, name in list_of_company_ids:
        myDict[name] = {}
        applications = get_company_application_info(company).json()
        for app in applications:
            if app['status'] in myDict[name]:
                myDict[name][app['status']] += 1
            else:
                myDict[name][app['status']] = 1
    return myDict

            

    
