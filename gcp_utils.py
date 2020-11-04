# -*- encoding: utf-8 -*-
from google.oauth2 import service_account
import os

def get_credentials_file(default_filename):
    file_env = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    file_cur = default_filename
    file_home = os.path.join(os.path.expanduser('~'),'google-stt.json')
    if file_env!=None and os.path.exists(file_env):
        return file_env
    elif os.path.exists(file_cur):
        return file_cur
    elif os.path.exists(file_home):
        return file_home
    else:
        return None

def read_credentials(credentials_filename):
    assert credentials_filename!=None, 'Need a credentials file'
    return service_account.Credentials.from_service_account_file(credentials_filename)

def get_credentials(default_filename):
    return read_credentials(get_credentials_file(default_filename))

