import extra_endpoints
import requests

elastic_endpoint='https://search-icims-hack-56-4ojyhi66tg25f2gpnb6p3dbv4y.us-east-2.es.amazonaws.com'
def main():
  companies=extra_endpoints.list_companies()
  for company in companies:
    url=elastic_endpoint+'/'+company['name'].lower().replace(" ", "")
    print(requests.put(url))

if __name__ == '__main__':
  main()
