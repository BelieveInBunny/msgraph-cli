# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class policiespermissiongrantpoliciesOperations(object):
    """policiespermissiongrantpoliciesOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~identity_sign_ins.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_excludes(
        self,
        permission_grant_policy_id,  # type: str
        orderby=None,  # type: Optional[List[Union[str, "models.Enum138"]]]
        select=None,  # type: Optional[List[Union[str, "models.Enum139"]]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.collectionofpermissiongrantconditionset"]
        """Get excludes from policies.

        Get excludes from policies.

        :param permission_grant_policy_id: key: id of permissionGrantPolicy.
        :type permission_grant_policy_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~identity_sign_ins.models.Enum138]
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_sign_ins.models.Enum139]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either collectionofpermissiongrantconditionset or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~identity_sign_ins.models.collectionofpermissiongrantconditionset]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.collectionofpermissiongrantconditionset"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_excludes.metadata['url']  # type: ignore
                path_format_arguments = {
                    'permissionGrantPolicy-id': self._serialize.url("permission_grant_policy_id", permission_grant_policy_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if self._config.top is not None:
                    query_parameters['$top'] = self._serialize.query("self._config.top", self._config.top, 'int', minimum=0)
                if self._config.skip is not None:
                    query_parameters['$skip'] = self._serialize.query("self._config.skip", self._config.skip, 'int', minimum=0)
                if self._config.search is not None:
                    query_parameters['$search'] = self._serialize.query("self._config.search", self._config.search, 'str')
                if self._config.filter is not None:
                    query_parameters['$filter'] = self._serialize.query("self._config.filter", self._config.filter, 'str')
                if self._config.count is not None:
                    query_parameters['$count'] = self._serialize.query("self._config.count", self._config.count, 'bool')
                if orderby is not None:
                    query_parameters['$orderby'] = self._serialize.query("orderby", orderby, '[str]', div=',')
                if select is not None:
                    query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
                if expand is not None:
                    query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('collectionofpermissiongrantconditionset', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.odataerror, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_excludes.metadata = {'url': '/policies/permissionGrantPolicies/{permissionGrantPolicy-id}/excludes'}  # type: ignore

    def create_excludes(
        self,
        permission_grant_policy_id,  # type: str
        body,  # type: "models.microsoftgraphpermissiongrantconditionset"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.microsoftgraphpermissiongrantconditionset"
        """Create new navigation property to excludes for policies.

        Create new navigation property to excludes for policies.

        :param permission_grant_policy_id: key: id of permissionGrantPolicy.
        :type permission_grant_policy_id: str
        :param body: New navigation property.
        :type body: ~identity_sign_ins.models.microsoftgraphpermissiongrantconditionset
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphpermissiongrantconditionset, or the result of cls(response)
        :rtype: ~identity_sign_ins.models.microsoftgraphpermissiongrantconditionset
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphpermissiongrantconditionset"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_excludes.metadata['url']  # type: ignore
        path_format_arguments = {
            'permissionGrantPolicy-id': self._serialize.url("permission_grant_policy_id", permission_grant_policy_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'microsoftgraphpermissiongrantconditionset')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphpermissiongrantconditionset', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_excludes.metadata = {'url': '/policies/permissionGrantPolicies/{permissionGrantPolicy-id}/excludes'}  # type: ignore

    def get_excludes(
        self,
        permission_grant_policy_id,  # type: str
        permission_grant_condition_set_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum140"]]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.microsoftgraphpermissiongrantconditionset"
        """Get excludes from policies.

        Get excludes from policies.

        :param permission_grant_policy_id: key: id of permissionGrantPolicy.
        :type permission_grant_policy_id: str
        :param permission_grant_condition_set_id: key: id of permissionGrantConditionSet.
        :type permission_grant_condition_set_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_sign_ins.models.Enum140]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphpermissiongrantconditionset, or the result of cls(response)
        :rtype: ~identity_sign_ins.models.microsoftgraphpermissiongrantconditionset
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphpermissiongrantconditionset"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_excludes.metadata['url']  # type: ignore
        path_format_arguments = {
            'permissionGrantPolicy-id': self._serialize.url("permission_grant_policy_id", permission_grant_policy_id, 'str'),
            'permissionGrantConditionSet-id': self._serialize.url("permission_grant_condition_set_id", permission_grant_condition_set_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphpermissiongrantconditionset', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_excludes.metadata = {'url': '/policies/permissionGrantPolicies/{permissionGrantPolicy-id}/excludes/{permissionGrantConditionSet-id}'}  # type: ignore

    def update_excludes(
        self,
        permission_grant_policy_id,  # type: str
        permission_grant_condition_set_id,  # type: str
        body,  # type: "models.microsoftgraphpermissiongrantconditionset"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property excludes in policies.

        Update the navigation property excludes in policies.

        :param permission_grant_policy_id: key: id of permissionGrantPolicy.
        :type permission_grant_policy_id: str
        :param permission_grant_condition_set_id: key: id of permissionGrantConditionSet.
        :type permission_grant_condition_set_id: str
        :param body: New navigation property values.
        :type body: ~identity_sign_ins.models.microsoftgraphpermissiongrantconditionset
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
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_excludes.metadata['url']  # type: ignore
        path_format_arguments = {
            'permissionGrantPolicy-id': self._serialize.url("permission_grant_policy_id", permission_grant_policy_id, 'str'),
            'permissionGrantConditionSet-id': self._serialize.url("permission_grant_condition_set_id", permission_grant_condition_set_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'microsoftgraphpermissiongrantconditionset')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    update_excludes.metadata = {'url': '/policies/permissionGrantPolicies/{permissionGrantPolicy-id}/excludes/{permissionGrantConditionSet-id}'}  # type: ignore

    def delete_excludes(
        self,
        permission_grant_policy_id,  # type: str
        permission_grant_condition_set_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete navigation property excludes for policies.

        Delete navigation property excludes for policies.

        :param permission_grant_policy_id: key: id of permissionGrantPolicy.
        :type permission_grant_policy_id: str
        :param permission_grant_condition_set_id: key: id of permissionGrantConditionSet.
        :type permission_grant_condition_set_id: str
        :param if_match: ETag.
        :type if_match: str
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
        accept = "application/json"

        # Construct URL
        url = self.delete_excludes.metadata['url']  # type: ignore
        path_format_arguments = {
            'permissionGrantPolicy-id': self._serialize.url("permission_grant_policy_id", permission_grant_policy_id, 'str'),
            'permissionGrantConditionSet-id': self._serialize.url("permission_grant_condition_set_id", permission_grant_condition_set_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete_excludes.metadata = {'url': '/policies/permissionGrantPolicies/{permissionGrantPolicy-id}/excludes/{permissionGrantConditionSet-id}'}  # type: ignore

    def list_includes(
        self,
        permission_grant_policy_id,  # type: str
        orderby=None,  # type: Optional[List[Union[str, "models.Enum141"]]]
        select=None,  # type: Optional[List[Union[str, "models.Enum142"]]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.collectionofpermissiongrantconditionset0"]
        """Get includes from policies.

        Get includes from policies.

        :param permission_grant_policy_id: key: id of permissionGrantPolicy.
        :type permission_grant_policy_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~identity_sign_ins.models.Enum141]
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_sign_ins.models.Enum142]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either collectionofpermissiongrantconditionset0 or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~identity_sign_ins.models.collectionofpermissiongrantconditionset0]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.collectionofpermissiongrantconditionset0"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_includes.metadata['url']  # type: ignore
                path_format_arguments = {
                    'permissionGrantPolicy-id': self._serialize.url("permission_grant_policy_id", permission_grant_policy_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if self._config.top is not None:
                    query_parameters['$top'] = self._serialize.query("self._config.top", self._config.top, 'int', minimum=0)
                if self._config.skip is not None:
                    query_parameters['$skip'] = self._serialize.query("self._config.skip", self._config.skip, 'int', minimum=0)
                if self._config.search is not None:
                    query_parameters['$search'] = self._serialize.query("self._config.search", self._config.search, 'str')
                if self._config.filter is not None:
                    query_parameters['$filter'] = self._serialize.query("self._config.filter", self._config.filter, 'str')
                if self._config.count is not None:
                    query_parameters['$count'] = self._serialize.query("self._config.count", self._config.count, 'bool')
                if orderby is not None:
                    query_parameters['$orderby'] = self._serialize.query("orderby", orderby, '[str]', div=',')
                if select is not None:
                    query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
                if expand is not None:
                    query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('collectionofpermissiongrantconditionset0', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.odataerror, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_includes.metadata = {'url': '/policies/permissionGrantPolicies/{permissionGrantPolicy-id}/includes'}  # type: ignore

    def create_includes(
        self,
        permission_grant_policy_id,  # type: str
        body,  # type: "models.microsoftgraphpermissiongrantconditionset"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.microsoftgraphpermissiongrantconditionset"
        """Create new navigation property to includes for policies.

        Create new navigation property to includes for policies.

        :param permission_grant_policy_id: key: id of permissionGrantPolicy.
        :type permission_grant_policy_id: str
        :param body: New navigation property.
        :type body: ~identity_sign_ins.models.microsoftgraphpermissiongrantconditionset
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphpermissiongrantconditionset, or the result of cls(response)
        :rtype: ~identity_sign_ins.models.microsoftgraphpermissiongrantconditionset
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphpermissiongrantconditionset"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_includes.metadata['url']  # type: ignore
        path_format_arguments = {
            'permissionGrantPolicy-id': self._serialize.url("permission_grant_policy_id", permission_grant_policy_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'microsoftgraphpermissiongrantconditionset')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphpermissiongrantconditionset', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_includes.metadata = {'url': '/policies/permissionGrantPolicies/{permissionGrantPolicy-id}/includes'}  # type: ignore

    def get_includes(
        self,
        permission_grant_policy_id,  # type: str
        permission_grant_condition_set_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum143"]]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.microsoftgraphpermissiongrantconditionset"
        """Get includes from policies.

        Get includes from policies.

        :param permission_grant_policy_id: key: id of permissionGrantPolicy.
        :type permission_grant_policy_id: str
        :param permission_grant_condition_set_id: key: id of permissionGrantConditionSet.
        :type permission_grant_condition_set_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_sign_ins.models.Enum143]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphpermissiongrantconditionset, or the result of cls(response)
        :rtype: ~identity_sign_ins.models.microsoftgraphpermissiongrantconditionset
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphpermissiongrantconditionset"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_includes.metadata['url']  # type: ignore
        path_format_arguments = {
            'permissionGrantPolicy-id': self._serialize.url("permission_grant_policy_id", permission_grant_policy_id, 'str'),
            'permissionGrantConditionSet-id': self._serialize.url("permission_grant_condition_set_id", permission_grant_condition_set_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphpermissiongrantconditionset', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_includes.metadata = {'url': '/policies/permissionGrantPolicies/{permissionGrantPolicy-id}/includes/{permissionGrantConditionSet-id}'}  # type: ignore

    def update_includes(
        self,
        permission_grant_policy_id,  # type: str
        permission_grant_condition_set_id,  # type: str
        body,  # type: "models.microsoftgraphpermissiongrantconditionset"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property includes in policies.

        Update the navigation property includes in policies.

        :param permission_grant_policy_id: key: id of permissionGrantPolicy.
        :type permission_grant_policy_id: str
        :param permission_grant_condition_set_id: key: id of permissionGrantConditionSet.
        :type permission_grant_condition_set_id: str
        :param body: New navigation property values.
        :type body: ~identity_sign_ins.models.microsoftgraphpermissiongrantconditionset
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
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_includes.metadata['url']  # type: ignore
        path_format_arguments = {
            'permissionGrantPolicy-id': self._serialize.url("permission_grant_policy_id", permission_grant_policy_id, 'str'),
            'permissionGrantConditionSet-id': self._serialize.url("permission_grant_condition_set_id", permission_grant_condition_set_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'microsoftgraphpermissiongrantconditionset')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    update_includes.metadata = {'url': '/policies/permissionGrantPolicies/{permissionGrantPolicy-id}/includes/{permissionGrantConditionSet-id}'}  # type: ignore

    def delete_includes(
        self,
        permission_grant_policy_id,  # type: str
        permission_grant_condition_set_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete navigation property includes for policies.

        Delete navigation property includes for policies.

        :param permission_grant_policy_id: key: id of permissionGrantPolicy.
        :type permission_grant_policy_id: str
        :param permission_grant_condition_set_id: key: id of permissionGrantConditionSet.
        :type permission_grant_condition_set_id: str
        :param if_match: ETag.
        :type if_match: str
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
        accept = "application/json"

        # Construct URL
        url = self.delete_includes.metadata['url']  # type: ignore
        path_format_arguments = {
            'permissionGrantPolicy-id': self._serialize.url("permission_grant_policy_id", permission_grant_policy_id, 'str'),
            'permissionGrantConditionSet-id': self._serialize.url("permission_grant_condition_set_id", permission_grant_condition_set_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete_includes.metadata = {'url': '/policies/permissionGrantPolicies/{permissionGrantPolicy-id}/includes/{permissionGrantConditionSet-id}'}  # type: ignore
