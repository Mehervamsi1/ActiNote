# code/auth.py

from azure.identity.aio import ClientSecretCredential
from msgraph import GraphServiceClient
import os

async def get_graph_client():
    tenant_id = os.getenv("TENANT_ID")
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    credential = ClientSecretCredential(
        tenant_id=tenant_id,
        client_id=client_id,
        client_secret=client_secret
    )

    graph_client = GraphServiceClient(credential=credential)
    return graph_client
