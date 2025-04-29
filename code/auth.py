# code/auth.py

import os
from dotenv import load_dotenv
from azure.identity.aio import ClientSecretCredential
from msgraph import GraphServiceClient

load_dotenv()

async def get_graph_client():
    credential = ClientSecretCredential(
        tenant_id=os.getenv("TENANT_ID"),
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
    )
    graph_client = GraphServiceClient(credential=credential)
    return graph_client




#-----------------------------------------------------------------
# import webbrowser
# import requests
# import msal
# from msal import PublicClientApplication
# import os
# from dotenv import load_dotenv

# load_dotenv()

# authority_url = 'https://login.microsoftonline.com/consumers/'


# CLIENT_ID=os.getenv("CLIENT_ID")

# base_url = 'https://graph.microsoft.com/v1.0/me/'
# endpoint = base_url + 'sendMail'
# SCOPES = ['Mail.ReadWrite','Mail.ReadWrite.Shared','Mail.Send','Mail.Send.Shared']

# # Authentication with authorization
# client_instance = msal.ConfidentialClientApplication(
#     client_id=CLIENT_ID,
#     client_credential=os.getenv("CLIENT_SECRET"),
#     authority=authority_url
# )

# authorization_request_url = client_instance.get_authorization_request_url(SCOPES)
# # print(authorization_request_url)
# webbrowser.open(authorization_request_url,new=True)

# authorization_code=os.getenv("AUTHORIZATION_CODE_LOCALHOST")

# access_token = client_instance.acquire_token_by_authorization_code(
#     code=authorization_code,
#     scopes=SCOPES
# )

# access_token_id = access_token['access_token']
# headers = {'Authorization': 'Bearer ' + access_token_id}

# endpoint = base_url + 'me'
# response = requests.get(endpoint, headers=headers)
# print(response)
# print(response.json())