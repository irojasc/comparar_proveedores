import os
import requests
from dotenv import load_dotenv

#load env variables
load_dotenv(dotenv_path='./.env', override=True)
URL_DEV = os.getenv("URL_DEV")
#####

def get_all_company_publisher(data_auth):
    try:
        endpoint = f'{URL_DEV}/linker/companypublisher/pair'
        headers = {"Authorization": 'Bearer %s' % data_auth['access_token']}
        response = requests.get(endpoint, headers=headers, timeout=5)
        returned = get_company_publisher_format(response.json())
        return returned
    except Exception as e:
        print(f'Error at get_all_suppliers: {e}')
        return []

def get_company_publisher_format(data: dict):
    myList = []
    for key in data.keys():
        myList.append({
            'index':  key,
            'secondary': data[key],
            'content': f'-{key} * ' + '[' + '-'.join(data[key])+  ']',
            'isSelected': False
        })
    return myList

def post_company_publisher(payload,data_auth):
    try:
        endpoint = f'{URL_DEV}/linker/companypublisher'
        headers = {"Authorization": 'Bearer %s' % data_auth['access_token']}
        response = requests.post(endpoint, json={'data': payload}, headers=headers, timeout=30)
        # returned = get_company_publisher_format(response.json())
        return response.status_code
    except Exception as e:
        print(f'Error at get_all_suppliers: {e}')
        return 0

def delete_company_publisher(payload,data_auth):
    try:
        endpoint = f'{URL_DEV}/linker/companypublisher'
        headers = {"Authorization": 'Bearer %s' % data_auth['access_token']}
        response = requests.delete(endpoint, json={'data': payload}, headers=headers, timeout=30)
        return response.status_code
    except Exception as e:
        print(f'Error at get_all_suppliers: {e}')
        return 0
    

#add tabs at top place with multiple options pyqt5?
        