import os
import requests
from dotenv import load_dotenv

#load env variables
load_dotenv(dotenv_path='./.env', override=True)
ADMIN_URL_GENESIS = os.getenv("ADMIN_URL_GENESIS")
#####

def get_all_publishers(data_auth):
    try:
        endpoint = f'{ADMIN_URL_GENESIS}/linker/companypublisher/nopair'
        headers = {"Authorization": 'Bearer %s' % data_auth['access_token']}
        response = requests.get(endpoint, headers=headers, timeout=30)
        returned = list(map(get_all_suppliers_format, enumerate(response.json())))
        return returned
    except Exception as e:
        print(f'Error at get_all_publishers: {e}')
        return []

##formats
def get_all_suppliers_format(value):
    index, data = value
    return{
        'index': data['index'],
        'content': '%d-%s'%(data['index'], data['publisher']),
        'isSelected': False,
        'content_root': 'xxxxx'
    }
