# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class FulfillmentOperationsOperations:
    """FulfillmentOperationsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~microsoft.marketplace.saas.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def resolve(
        self,
        x_ms_marketplace_token: str,
        request_id_parameter: Optional[str] = None,
        correlation_id: Optional[str] = None,
        **kwargs
    ) -> Optional["models.ResolvedSubscription"]:
        """Resolve a subscription.

        The resolve endpoint enables the publisher to resolve a marketplace token to a persistent
        resource ID. The resource ID is the unique identifier for a SaaS subscription. When a user is
        redirected to a partner's website, the URL contains a token in the query parameters. The
        partner is expected to use this token and make a request to resolve it. The response contains
        the unique SaaS subscription ID, name, offer ID, and plan for the resource. This token is valid
        for one hour only.

        :param x_ms_marketplace_token: The token query parameter in the URL when the user is redirected
         to the SaaS partner's website from Azure (for example,  https://contoso.com/signup?token=..).
         Note, The URL decodes the token value from the browser before using it.
        :type x_ms_marketplace_token: str
        :param request_id_parameter: A unique string value for tracking the request from the client,
         preferably a GUID. If this value isn't provided, one will be generated and provided in the
         response headers.
        :type request_id_parameter: str
        :param correlation_id: A unique string value for operation on the client. This parameter
         correlates all events from client operation with events on the server side. If this value isn't
         provided, one will be generated and provided in the response headers.
        :type correlation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ResolvedSubscription, or the result of cls(response)
        :rtype: ~microsoft.marketplace.saas.models.ResolvedSubscription or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["models.ResolvedSubscription"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-08-31"
        accept = "application/json"

        # Construct URL
        url = self.resolve.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if request_id_parameter is not None:
            header_parameters['x-ms-requestid'] = self._serialize.header("request_id_parameter", request_id_parameter, 'str')
        if correlation_id is not None:
            header_parameters['x-ms-correlationid'] = self._serialize.header("correlation_id", correlation_id, 'str')
        header_parameters['x-ms-marketplace-token'] = self._serialize.header("x_ms_marketplace_token", x_ms_marketplace_token, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 400, 403, 404, 500]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ResolvedSubscription', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    resolve.metadata = {'url': '/saas/subscriptions/resolve'}  # type: ignore

    def list_subscriptions(
        self,
        continuation_token_parameter: Optional[str] = None,
        request_id_parameter: Optional[str] = None,
        correlation_id: Optional[str] = None,
        **kwargs
    ) -> AsyncIterable["models.SubscriptionsResponse"]:
        """List subscriptions.

        Lists all the SaaS subscriptions for a publisher.

        :param continuation_token_parameter: Optional value, only used for ListSubscriptions.
        :type continuation_token_parameter: str
        :param request_id_parameter: A unique string value for tracking the request from the client,
         preferably a GUID. If this value isn't provided, one will be generated and provided in the
         response headers.
        :type request_id_parameter: str
        :param correlation_id: A unique string value for operation on the client. This parameter
         correlates all events from client operation with events on the server side. If this value isn't
         provided, one will be generated and provided in the response headers.
        :type correlation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SubscriptionsResponse or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~microsoft.marketplace.saas.models.SubscriptionsResponseor Noneor None]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SubscriptionsResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-08-31"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            if request_id_parameter is not None:
                header_parameters['x-ms-requestid'] = self._serialize.header("request_id_parameter", request_id_parameter, 'str')
            if correlation_id is not None:
                header_parameters['x-ms-correlationid'] = self._serialize.header("correlation_id", correlation_id, 'str')
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_subscriptions.metadata['url']  # type: ignore
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
                if continuation_token_parameter is not None:
                    query_parameters['continuationToken'] = self._serialize.query("continuation_token_parameter", continuation_token_parameter, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('SubscriptionsResponse', pipeline_response)
            list_of_elem = deserialized.subscriptions
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200, 403, 500]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_subscriptions.metadata = {'url': '/saas/subscriptions/'}  # type: ignore

    async def get_subscription(
        self,
        subscription_id: str,
        request_id_parameter: Optional[str] = None,
        correlation_id: Optional[str] = None,
        **kwargs
    ) -> Optional["models.Subscription"]:
        """Get subscription.

        Gets the specified SaaS subscription. Use this call to get license information and plan
        information.

        :param subscription_id:
        :type subscription_id: str
        :param request_id_parameter: A unique string value for tracking the request from the client,
         preferably a GUID. If this value isn't provided, one will be generated and provided in the
         response headers.
        :type request_id_parameter: str
        :param correlation_id: A unique string value for operation on the client. This parameter
         correlates all events from client operation with events on the server side. If this value isn't
         provided, one will be generated and provided in the response headers.
        :type correlation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Subscription, or the result of cls(response)
        :rtype: ~microsoft.marketplace.saas.models.Subscription or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["models.Subscription"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-08-31"
        accept = "application/json"

        # Construct URL
        url = self.get_subscription.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if request_id_parameter is not None:
            header_parameters['x-ms-requestid'] = self._serialize.header("request_id_parameter", request_id_parameter, 'str')
        if correlation_id is not None:
            header_parameters['x-ms-correlationid'] = self._serialize.header("correlation_id", correlation_id, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 403, 404, 500]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Subscription', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_subscription.metadata = {'url': '/saas/subscriptions/{subscriptionId}'}  # type: ignore

    async def update_subscription(
        self,
        subscription_id: str,
        body: "models.SubscriberPlan",
        request_id_parameter: Optional[str] = None,
        correlation_id: Optional[str] = None,
        **kwargs
    ) -> None:
        """Patch a subscription.

        Use this call to update the plan, the user count (quantity), or both.

        :param subscription_id:
        :type subscription_id: str
        :param body:
        :type body: ~microsoft.marketplace.saas.models.SubscriberPlan
        :param request_id_parameter: A unique string value for tracking the request from the client,
         preferably a GUID. If this value isn't provided, one will be generated and provided in the
         response headers.
        :type request_id_parameter: str
        :param correlation_id: A unique string value for operation on the client. This parameter
         correlates all events from client operation with events on the server side. If this value isn't
         provided, one will be generated and provided in the response headers.
        :type correlation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-08-31"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update_subscription.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if request_id_parameter is not None:
            header_parameters['x-ms-requestid'] = self._serialize.header("request_id_parameter", request_id_parameter, 'str')
        if correlation_id is not None:
            header_parameters['x-ms-correlationid'] = self._serialize.header("correlation_id", correlation_id, 'str')
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'SubscriberPlan')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202, 400, 403, 404, 500]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        if response.status_code == 202:
            response_headers['Operation-Location']=self._deserialize('str', response.headers.get('Operation-Location'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    update_subscription.metadata = {'url': '/saas/subscriptions/{subscriptionId}'}  # type: ignore

    async def delete_subscription(
        self,
        subscription_id: str,
        request_id_parameter: Optional[str] = None,
        correlation_id: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete a subscription.

        Unsubscribe and delete the specified subscription.

        :param subscription_id:
        :type subscription_id: str
        :param request_id_parameter: A unique string value for tracking the request from the client,
         preferably a GUID. If this value isn't provided, one will be generated and provided in the
         response headers.
        :type request_id_parameter: str
        :param correlation_id: A unique string value for operation on the client. This parameter
         correlates all events from client operation with events on the server side. If this value isn't
         provided, one will be generated and provided in the response headers.
        :type correlation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-08-31"

        # Construct URL
        url = self.delete_subscription.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if request_id_parameter is not None:
            header_parameters['x-ms-requestid'] = self._serialize.header("request_id_parameter", request_id_parameter, 'str')
        if correlation_id is not None:
            header_parameters['x-ms-correlationid'] = self._serialize.header("correlation_id", correlation_id, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202, 400, 403, 404, 500]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        if response.status_code == 202:
            response_headers['Operation-Location']=self._deserialize('str', response.headers.get('Operation-Location'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    delete_subscription.metadata = {'url': '/saas/subscriptions/{subscriptionId}'}  # type: ignore

    async def list_available_plans(
        self,
        subscription_id: str,
        request_id_parameter: Optional[str] = None,
        correlation_id: Optional[str] = None,
        **kwargs
    ) -> Optional["models.SubscriptionPlans"]:
        """List available plans.

        Use this call to find out if there are any private or public offers for the current publisher.

        :param subscription_id:
        :type subscription_id: str
        :param request_id_parameter: A unique string value for tracking the request from the client,
         preferably a GUID. If this value isn't provided, one will be generated and provided in the
         response headers.
        :type request_id_parameter: str
        :param correlation_id: A unique string value for operation on the client. This parameter
         correlates all events from client operation with events on the server side. If this value isn't
         provided, one will be generated and provided in the response headers.
        :type correlation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SubscriptionPlans, or the result of cls(response)
        :rtype: ~microsoft.marketplace.saas.models.SubscriptionPlans or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["models.SubscriptionPlans"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-08-31"
        accept = "application/json"

        # Construct URL
        url = self.list_available_plans.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if request_id_parameter is not None:
            header_parameters['x-ms-requestid'] = self._serialize.header("request_id_parameter", request_id_parameter, 'str')
        if correlation_id is not None:
            header_parameters['x-ms-correlationid'] = self._serialize.header("correlation_id", correlation_id, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 403, 404, 500]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('SubscriptionPlans', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    list_available_plans.metadata = {'url': '/saas/subscriptions/{subscriptionId}/listAvailablePlans'}  # type: ignore

    async def activate_subscription(
        self,
        subscription_id: str,
        body: "models.SubscriberPlan",
        request_id_parameter: Optional[str] = None,
        correlation_id: Optional[str] = None,
        **kwargs
    ) -> None:
        """Activate a subscription.

        Use this call to activate a subscription.

        :param subscription_id:
        :type subscription_id: str
        :param body:
        :type body: ~microsoft.marketplace.saas.models.SubscriberPlan
        :param request_id_parameter: A unique string value for tracking the request from the client,
         preferably a GUID. If this value isn't provided, one will be generated and provided in the
         response headers.
        :type request_id_parameter: str
        :param correlation_id: A unique string value for operation on the client. This parameter
         correlates all events from client operation with events on the server side. If this value isn't
         provided, one will be generated and provided in the response headers.
        :type correlation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-08-31"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.activate_subscription.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if request_id_parameter is not None:
            header_parameters['x-ms-requestid'] = self._serialize.header("request_id_parameter", request_id_parameter, 'str')
        if correlation_id is not None:
            header_parameters['x-ms-correlationid'] = self._serialize.header("correlation_id", correlation_id, 'str')
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'SubscriberPlan')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 400, 403, 404, 500]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    activate_subscription.metadata = {'url': '/saas/subscriptions/{subscriptionId}/activate'}  # type: ignore