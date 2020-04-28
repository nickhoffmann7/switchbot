import base64
from email.mime.text import MIMEText

from googleapiclient import errors


def create_message(receiver, subject, message):
    message = MIMEText(message)
    message['to'] = receiver
    message['from'] = 'me'
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}


def send_message(service, message):
    try:
        message = service.users().messages().send(userId='me', body=message).execute()
        print('Email sent: %s' % message)
    except errors.HttpError as error:
        print('An error occurred: %s' % error)
