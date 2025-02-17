# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class usersonenotenotebookssectionsparentsectiongroupparentnotebookOperations:
    """usersonenotenotebookssectionsparentsectiongroupparentnotebookOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~users_actions.models
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

    async def copy_notebook(
        self,
        user_id: str,
        notebook_id: str,
        onenote_section_id: str,
        body: "models.pathsh9f1uhusersuseridonenotenotebooksnotebookidsectionsonenotesectionidparentsectiongroupparentnotebookmicrosoftgraphcopynotebookpostrequestbodycontentapplicationjsonschema",
        **kwargs
    ) -> "models.microsoftgraphonenoteoperation":
        """Invoke action copyNotebook.

        Invoke action copyNotebook.

        :param user_id: key: id of user.
        :type user_id: str
        :param notebook_id: key: id of notebook.
        :type notebook_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
        :param body: Action parameters.
        :type body: ~users_actions.models.pathsh9f1uhusersuseridonenotenotebooksnotebookidsectionsonenotesectionidparentsectiongroupparentnotebookmicrosoftgraphcopynotebookpostrequestbodycontentapplicationjsonschema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphonenoteoperation, or the result of cls(response)
        :rtype: ~users_actions.models.microsoftgraphonenoteoperation
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphonenoteoperation"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.copy_notebook.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'notebook-id': self._serialize.url("notebook_id", notebook_id, 'str'),
            'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'pathsh9f1uhusersuseridonenotenotebooksnotebookidsectionsonenotesectionidparentsectiongroupparentnotebookmicrosoftgraphcopynotebookpostrequestbodycontentapplicationjsonschema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphonenoteoperation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    copy_notebook.metadata = {'url': '/users/{user-id}/onenote/notebooks/{notebook-id}/sections/{onenoteSection-id}/parentSectionGroup/parentNotebook/microsoft.graph.copyNotebook'}  # type: ignore
