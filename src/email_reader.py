import os
import base64
import email
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def get_email_headers(payload, header_name):
    for header in payload.get('headers', []):
        if header['name'].lower() == header_name.lower():
            return header['value']
    return None

def decode_body(part):
    data = part.get('body', {}).get('data')
    if data:
        decoded_bytes = base64.urlsafe_b64decode(data)
        return decoded_bytes.decode('utf-8', errors='ignore')
    return ""

def get_email_body(payload):
    if 'parts' in payload:
        # Multipart message (can be nested)
        for part in payload['parts']:
            if part.get('mimeType') == 'text/plain':
                return decode_body(part)
            elif part.get('mimeType') == 'text/html':
                # fallback: decode html if plain not found
                return decode_body(part)
    else:
        # Single part message
        return decode_body(payload)
    return ""

def read_unread_emails(max_results=5):
    service = authenticate_gmail()
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], q="is:unread", maxResults=max_results).execute()
    messages = results.get('messages', [])
    email_data = []

    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
        payload = msg_data.get('payload', {})
        headers = payload.get('headers', [])

        from_ = get_email_headers(payload, 'From')
        subject = get_email_headers(payload, 'Subject')
        body = get_email_body(payload)

        email_data.append({
            'id': msg['id'],
            'from': from_,
            'subject': subject,
            'body': body
        })

    return email_data
