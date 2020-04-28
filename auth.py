import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

import utils

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

CLIENT_SECRET = utils.get_file('client_secret.json')
TOKEN = utils.get_file('token.pickle')


def get_credentials():
    print("getting credentials")
    credentials = None
    if os.path.exists(TOKEN):
        with open(TOKEN, 'rb') as token:
            credentials = pickle.load(token)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
            print("refreshed")
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET, SCOPES)
            credentials = flow.run_console()
            print("created")
        with open(TOKEN, 'wb') as token:
            pickle.dump(credentials, token)
    else:
        print("still valid")
    return credentials


def get_gmail_service(credentials):
    return build('gmail', 'v1', credentials=credentials)
