# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.core import AsyncPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import SaaSAPIConfiguration
from .operations import FulfillmentOperationsOperations
from .operations import SubscriptionOperationsOperations
from .. import models


class SaaSAPI(object):
    """This spec details the APIs that enable partners to sell their SaaS applications in the AppSource marketplace and the Azure Marketplace. These APIs are a requirement for transactable SaaS offers on the AppSource and Azure Marketplace.

    :ivar fulfillment_operations: FulfillmentOperationsOperations operations
    :vartype fulfillment_operations: microsoft.marketplace.saas.aio.operations.FulfillmentOperationsOperations
    :ivar subscription_operations: SubscriptionOperationsOperations operations
    :vartype subscription_operations: microsoft.marketplace.saas.aio.operations.SubscriptionOperationsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://marketplaceapi.microsoft.com/api'
        self._config = SaaSAPIConfiguration(credential, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.fulfillment_operations = FulfillmentOperationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.subscription_operations = SubscriptionOperationsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "SaaSAPI":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)