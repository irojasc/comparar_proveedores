import os
import requests
from dotenv import load_dotenv

#load env variables
load_dotenv(dotenv_path='./.env', verbose= True)
URL_DEV = os.getenv("URL_DEV")
#####

def get_all_suppliers(data_auth):
    try:
        endpoint = f'{URL_DEV}/company/supplier'
        headers = {"Authorization": 'Bearer %s' % data_auth['access_token']}
        response = requests.get(endpoint, headers=headers)
        returned = list(map(get_all_suppliers_format, enumerate(response.json())))
        return returned
    except Exception as e:
        print(f'Error: {e}')
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
