from msal import ConfidentialClientApplication
import uuid

AAD_AUTHORITY = "https://login.microsoftonline.com/{}/"
MARKETPLACE_RESOURCE_SCOPE = "20e940b3-4c77-4b0b-9a53-9e16a1b010a7/.default"


class MarketplaceTokenProvider(object):
    def __init__(self, tenant_id, client_id, client_secret):
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret

    def acquire_token(self):
        app = ConfidentialClientApplication(
            self.client_id,
            authority=AAD_AUTHORITY.format(self.tenant_id),
            client_credential=self.client_secret)
        result = app.acquire_token_for_client(scopes=[MARKETPLACE_RESOURCE_SCOPE])
        return result
