from __future__ import print_function
import base64
import os.path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://mail.google.com/']


creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())


service = build('gmail', 'v1', credentials=creds)


def create_message(sender, to, subject):
    message = MIMEMultipart()
    #message = MIMEText(message_text)
    body = (
        f"Hi,\n\n"
        f"Amazon has dropped the price of the[PRODUCT_NAME] from original price[ORIGINAL_PRICE] to[DISCOUNTED_PRICE]\n\n"
        f"Amazon Link to the product[PRODUCT_URL].\n\n"
        f"Rohit"
    )
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}


def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                   .execute())
        print('Message Id: %s' % message['id'])
        return message
    except Exception as error:
        print(error)


message = create_message('me', 'iamrohitraveendran@gmail.com', 'hello')
print(send_message(service=service, user_id='me', message=message))