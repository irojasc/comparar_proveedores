import os
from os.path import join, dirname
import requests
from urllib3 import encode_multipart_formdata
from dotenv import load_dotenv, find_dotenv

#load env variables
dotenv_path_ = join(dirname(__file__), '.env')
load_dotenv(dotenv_path='./.env', override= True)
ADMIN_URL_GENESIS = os.getenv("ADMIN_URL_GENESIS")
#####

session = requests.Session()

class Login:
    def __init__(self,  username: str = None, password: str = None):
        self.session = requests.Session()
        self.data_auth = {}
        if bool(username) and bool(password):
            self.LogIn(username, password)

    def __enter__(self):
        return self.data_auth

    def __exit__(self, *args):
        print("Session terminada")
        session.close()
        pass
        # self.file.close()

    def LogIn(self, username, password):
        data = {'username': username,
                'password':  password}
        request_body, content_type = encode_multipart_formdata(data)
        headers = {"Content-Type": content_type}
        inner_url = f'{ADMIN_URL_GENESIS}/Login/token'
        try:
            # x = self.session.post(inner_url, data=request_body, headers=headers)
            x = requests.post(inner_url, data=request_body, headers=headers, timeout=30)
            if (x.status_code == 200):
                self.data_auth = x.json()
            else:
                self.data_auth = {}
        except Exception as e:
            print(f"Error: {e}")
            self.data_auth = None

    