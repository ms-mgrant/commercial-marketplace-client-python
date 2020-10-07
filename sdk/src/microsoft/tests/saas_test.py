import os

from src.microsoft.marketplace.token_provider import MarketplaceTokenProvider

tenant_id = os.environ["AAD_TENANT_ID"]
client_id = os.environ["AAD_APP_CLIENT_ID"]
client_secret = os.environ["AAD_APP_CLIENT_SECRET"]
provider = MarketplaceTokenProvider(
    tenant_id=tenant_id,
    client_id=client_id,
    client_secret=client_secret
)
token = provider.acquire_token()

