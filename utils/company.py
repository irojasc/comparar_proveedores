import os
import requests
from dotenv import load_dotenv

#load env variables
load_dotenv(dotenv_path='./.env', override=True)
ADMIN_URL_GENESIS = os.getenv("ADMIN_URL_GENESIS")

#####
def get_all_suppliers(data_auth):
    try:
        endpoint = f'{ADMIN_URL_GENESIS}/company/supplier'
        headers = {"Authorization": 'Bearer %s' % data_auth['access_token']}
        response = requests.get(endpoint, headers=headers, timeout=5)
        returned = list(map(get_all_suppliers_format, enumerate(response.json())))
        return returned
    except Exception as e:
        print(f'Error at get_all_suppliers: {e}')
        return []

##formats
def get_all_suppliers_format(value):
    index, data = value
    return{
        'index': index,
        'content': '%d-%s-%s'%(index, data['docNum'], data['docName']),
        'isSelected': False,
        'content_root': 'xxxxx'
    }
###
def create_new_company(payload, data_auth):
    try:
        endpoint = f'{ADMIN_URL_GENESIS}/company/newcompany'
        headers = {"Authorization": 'Bearer %s' % data_auth['access_token']}
        response = requests.post(endpoint, json=payload, headers=headers, timeout=30)
        return response.status_code
    except Exception as e:
        print(f'Error at get_all_suppliers: {e}')
        return 304
