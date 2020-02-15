# Connect to gmail API and read e-mail
# follow these steps: https://developers.google.com/gmail/api/quickstart/python


from __future__ import print_function

import base64
import pickle
import os.path
from email.mime.text import MIMEText

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def get_credentials():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('../exercises/02_private/token.pickle'):
        with open('../exercises/02_private/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '../exercises/02_private/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('../exercises/02_private/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service


SERVICE = get_credentials()


def get_labels():
    # Call the Gmail API
    results = SERVICE.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

get_labels()


def get_drafts():
    # Assignment: create get drafts function
    pass


def create_message(sender, to, subject, message_text):
    # Assignment: create create_message function
    pass


test_message = create_message('hvdveer@gmail.com', 'hvdveer@gmail.com', 'hello', "hii")


def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print('Message Id: %s' % message['id'])
        return message

    except:
        print('An error occurred:')

send_message(SERVICE, user_id='me', message=test_message)