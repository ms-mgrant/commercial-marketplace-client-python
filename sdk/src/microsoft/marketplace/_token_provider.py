from msal import ConfidentialClientApplication
import uuid

AAD_AUTHORITY = "https://login.microsoftonline.com/%s/"

class MarketplaceTokenProvider(object):
    def acquire_token(self):
        return ""

class ClientSecretTokenProviderSettings(object):

    def __init__(self, tenant_id, client_id, client_secret):
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret

class ClientSecretTokenProvider(MarketplaceTokenProvider):

    def __init__(self, token_provider_settings):
        self.token_provider_settings = token_provider_settings

    def acquire_token(self):
        authority = ""