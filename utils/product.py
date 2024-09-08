import os
import requests
from dotenv import load_dotenv

#load env variables
load_dotenv(dotenv_path='./.env', override=True)
URL_DEV = os.getenv("URL_DEV")
#####

def get_all_publishers(data_auth):
    try:
        endpoint = f'{URL_DEV}/linker/companypublisher/nopair'
        headers = {"Authorization": 'Bearer %s' % data_auth['access_token']}
        response = requests.get(endpoint, headers=headers, timeout=5)
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
