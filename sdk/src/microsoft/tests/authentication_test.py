import base64
import os

from azure.identity import CertificateCredential
from cryptography.hazmat.primitives.serialization import pkcs12

from src.microsoft.marketplace.token_provider import MarketplaceTokenProvider


def test_client_secret_auth():
    tenant_id = os.environ["AAD_TENANT_ID"]
    client_id = os.environ["AAD_APP_CLIENT_ID"]
    client_secret = os.environ["AAD_APP_CLIENT_SECRET"]

    provider = MarketplaceTokenProvider(
        tenant_id=tenant_id,
        client_id=client_id,
        client_secret=client_secret
    )
    token = provider.acquire_token()
    assert (token['token_type'] == "Bearer")
    assert (token['expires_in'] == 3599)
    assert (len(token['access_token']) > 0)


def test_client_certificate_auth():
    # cred = CertificateCredential
    tenant_id = os.environ["AAD_TENANT_ID"]
    client_id = os.environ["AAD_APP_CLIENT_ID"]
    client_cert = os.environ["AAD_APP_CERT"]
    cert_secret = os.environ["AAD_APP_CERT_SECRET"]
    cert_thumbprint = os.environ["AAD_APP_THUMBPRINT"]

    cert_bytes = base64.b64decode(client_cert)
    password_bytes = bytes(cert_secret, "utf-8")
    cert_parts = pkcs12.load_key_and_certificates(cert_bytes, password_bytes)
    private_key = cert_parts[0]
    pem_file = open('d:/key.pkcs12', 'wb')
    pem_file.write(cert_bytes)
    provider = MarketplaceTokenProvider(
        tenant_id=tenant_id,
        client_id=client_id,
        client_secret={"thumbprint": cert_thumbprint, "private_key": private_key}
    )

    token = provider.acquire_token()
    assert (token['token_type'] == "Bearer")
    assert (token['expires_in'] == 3599)
    assert (len(token['access_token']) > 0)

