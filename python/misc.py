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