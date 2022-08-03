# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient

from .._serialization import Deserializer, Serializer
from ._configuration import SaaSAPIConfiguration
from .operations import FulfillmentOperationsOperations, SubscriptionOperationsOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Dict

    from azure.core.credentials_async import AsyncTokenCredential

class SaaSAPI:  # pylint: disable=client-accepts-api-version-keyword
    """This spec details the APIs that enable partners to sell their SaaS applications in the
    AppSource marketplace and the Azure Marketplace. These APIs are a requirement for transactable
    SaaS offers on the AppSource and Azure Marketplace.

    :ivar fulfillment_operations: FulfillmentOperationsOperations operations
    :vartype fulfillment_operations:
     azure.marketplace.aio.operations.FulfillmentOperationsOperations
    :ivar subscription_operations: SubscriptionOperationsOperations operations
    :vartype subscription_operations:
     azure.marketplace.aio.operations.SubscriptionOperationsOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :keyword endpoint: Service URL. Default value is "https://marketplaceapi.microsoft.com/api".
    :paramtype endpoint: str
    :keyword api_version: Api Version. Default value is "2018-08-31". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        *,
        endpoint: str = "https://marketplaceapi.microsoft.com/api",
        **kwargs: Any
    ) -> None:
        self._config = SaaSAPIConfiguration(credential=credential, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.fulfillment_operations = FulfillmentOperationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.subscription_operations = SubscriptionOperationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )


    def send_request(
        self,
        request: HttpRequest,
        **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "SaaSAPI":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
