from dotenv import dotenv_values

from evocarshare import CredentialBundle


def credentials_from_env() -> CredentialBundle:
    """Creates a CredentialBundle with secrets loaded from Environment"""
    config = dotenv_values(".env")

    api_key = config["EVOAPI_KEY"] or ""
    client_id = config["EVOAPI_CLIENTID"] or ""
    client_secret = config["EVOAPI_CLIENTSECRET"] or ""

    return CredentialBundle(api_key, client_id, client_secret)
