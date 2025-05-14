# import json
# import requests
# import os
# from dotenv import load_dotenv
# from datetime import datetime

# # Load environment variables
# load_dotenv()

# tenant_id = os.getenv("TENANT_ID")
# client_id = os.getenv("CLIENT_ID")
# client_secret = os.getenv("CLIENT_SECRET")
# sender_email=os.getenv("SENDER_EMAIL")

# def get_access_token():
#     url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
#     payload = {
#         'grant_type': "client_credentials",
#         'client_id': client_id,
#         'client_secret': client_secret,
#         'scope': 'https://graph.microsoft.com/.default'
#     }
#     response = requests.post(url, data=payload)
#     response_data = response.json()
#     return response_data['access_token']

# def send_email():
#     access_token = get_access_token()
#     headers = {
#         "Authorization": f"Bearer {access_token}",
#         "Content-Type": "application/json"
#     }

#     #now = datetime.utcnow().isoformat() + "Z"

#     url = f"https://graph.microsoft.com/v1.0/users/{sender_email}/sendMail"

#     payload = {
#         "message": {
#             "subject": "An Email Test from Python",
#             "body": {
#                 "contentType": "Text",
#                 "content": f"The test email now"
#             },
#             "toRecipients": [
#                 {"emailAddress": {"address": "SyamA@AIReactor.onmicrosoft.com"}},
#                 {"emailAddress": {"address": "PragnaP@AIReactor.onmicrosoft.com"}}
#             ],
#             "ccRecipients": [
#                 {"emailAddress": {"address": "MeherD@AIReactor.onmicrosoft.com"}}
#             ]
#         },
#         "saveToSentItems": True
#     }

#     response = requests.post(url, headers=headers, json=payload)
#     print(response.status_code, response.text)

# # Call the function
# send_email()


#-----------------------------------------------------

# send_email.py

import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

tenant_id = os.getenv("TENANT_ID")
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
sender_email = os.getenv("SENDER_EMAIL")

def get_access_token():
    url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
    payload = {
        'grant_type': "client_credentials",
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'https://graph.microsoft.com/.default'
    }
    response = requests.post(url, data=payload)
    response_data = response.json()
    return response_data['access_token']

def send_email(subject, content, to_addresses, cc_addresses=None):
    access_token = get_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    url = f"https://graph.microsoft.com/v1.0/users/{sender_email}/sendMail"

    payload = {
        "message": {
            "subject": subject,
            "body": {
                "contentType": "Text",
                "content": content
            },
            "toRecipients": [{"emailAddress": {"address": addr}} for addr in to_addresses],
        },
        "saveToSentItems": True
    }

    if cc_addresses:
        payload["message"]["ccRecipients"] = [{"emailAddress": {"address": addr}} for addr in cc_addresses]

    response = requests.post(url, headers=headers, json=payload)
    print(f"Email sent to {', '.join(to_addresses)}. Status: {response.status_code}")
    print(response.text)
