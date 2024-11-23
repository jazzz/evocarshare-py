import os

from dotenv import load_dotenv

from evocarshare import CredentialBundle

load_dotenv(".env")


def credentials_from_env() -> CredentialBundle:
    """Creates a CredentialBundle with secrets loaded from Environment"""

    api_key = os.environ.get("EVOAPI_KEY") or ""
    client_id = os.environ.get("EVOAPI_CLIENTID") or ""
    client_secret = os.environ.get("EVOAPI_CLIENTSECRET") or ""

    return CredentialBundle(api_key, client_id, client_secret)
