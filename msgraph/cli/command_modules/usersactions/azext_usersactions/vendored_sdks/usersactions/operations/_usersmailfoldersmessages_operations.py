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
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class usersmailfoldersmessagesOperations(object):
    """usersmailfoldersmessagesOperations operations.

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

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def copy(
        self,
        user_id,  # type: str
        mail_folder_id,  # type: str
        message_id,  # type: str
        body,  # type: "models.pathsdy94gcusersuseridmailfoldersmailfolderidmessagesmessageidmicrosoftgraphcopypostrequestbodycontentapplicationjsonschema"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.microsoftgraphmessage"
        """Invoke action copy.

        Invoke action copy.

        :param user_id: key: id of user.
        :type user_id: str
        :param mail_folder_id: key: id of mailFolder.
        :type mail_folder_id: str
        :param message_id: key: id of message.
        :type message_id: str
        :param body: Action parameters.
        :type body: ~users_actions.models.pathsdy94gcusersuseridmailfoldersmailfolderidmessagesmessageidmicrosoftgraphcopypostrequestbodycontentapplicationjsonschema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphmessage, or the result of cls(response)
        :rtype: ~users_actions.models.microsoftgraphmessage
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphmessage"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.copy.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'mailFolder-id': self._serialize.url("mail_folder_id", mail_folder_id, 'str'),
            'message-id': self._serialize.url("message_id", message_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'pathsdy94gcusersuseridmailfoldersmailfolderidmessagesmessageidmicrosoftgraphcopypostrequestbodycontentapplicationjsonschema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphmessage', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    copy.metadata = {'url': '/users/{user-id}/mailFolders/{mailFolder-id}/messages/{message-id}/microsoft.graph.copy'}  # type: ignore

    def create_forward(
        self,
        user_id,  # type: str
        mail_folder_id,  # type: str
        message_id,  # type: str
        body,  # type: "models.paths29l6iuusersuseridmailfoldersmailfolderidmessagesmessageidmicrosoftgraphcreateforwardpostrequestbodycontentapplicationjsonschema"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.microsoftgraphmessage"
        """Invoke action createForward.

        Invoke action createForward.

        :param user_id: key: id of user.
        :type user_id: str
        :param mail_folder_id: key: id of mailFolder.
        :type mail_folder_id: str
        :param message_id: key: id of message.
        :type message_id: str
        :param body: Action parameters.
        :type body: ~users_actions.models.paths29l6iuusersuseridmailfoldersmailfolderidmessagesmessageidmicrosoftgraphcreateforwardpostrequestbodycontentapplicationjsonschema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphmessage, or the result of cls(response)
        :rtype: ~users_actions.models.microsoftgraphmessage
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphmessage"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_forward.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'mailFolder-id': self._serialize.url("mail_folder_id", mail_folder_id, 'str'),
            'message-id': self._serialize.url("message_id", message_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'paths29l6iuusersuseridmailfoldersmailfolderidmessagesmessageidmicrosoftgraphcreateforwardpostrequestbodycontentapplicationjsonschema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphmessage', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_forward.metadata = {'url': '/users/{user-id}/mailFolders/{mailFolder-id}/messages/{message-id}/microsoft.graph.createForward'}  # type: ignore

    def create_reply(
        self,
        user_id,  # type: str
        mail_folder_id,  # type: str
        message_id,  # type: str
        body,  # type: "models.pathsgpd5xxusersuseridmailfoldersmailfolderidmessagesmessageidmicrosoftgraphcreatereplypostrequestbodycontentapplicationjsonschema"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.microsoftgraphmessage"
        """Invoke action createReply.

        Invoke action createReply.

        :param user_id: key: id of user.
        :type user_id: str
        :param mail_folder_id: key: id of mailFolder.
        :type mail_folder_id: str
        :param message_id: key: id of message.
        :type message_id: str
        :param body: Action parameters.
        :type body: ~users_actions.models.pathsgpd5xxusersuseridmailfoldersmailfolderidmessagesmessageidmicrosoftgraphcreatereplypostrequestbodycontentapplicationjsonschema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphmessage, or the result of cls(response)
        :rtype: ~users_actions.models.microsoftgraphmessage
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphmessage"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_reply.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'mailFolder-id': self._serialize.url("mail_folder_id", mail_folder_id, 'str'),
            'message-id': self._serialize.url("message_id", message_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'pathsgpd5xxusersuseridmailfoldersmailfolderidmessagesmessageidmicrosoftgraphcreatereplypostrequestbodycontentapplicationjsonschema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphmessage', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_reply.metadata = {'url': '/users/{user-id}/mailFolders/{mailFolder-id}/messages/{message-id}/microsoft.graph.createReply'}  # type: ignore

    def create_reply_all(
        self,
        user_id,  # type: str
        mail_folder_id,  # type: str
        message_id,  # type: str
        body,  # type: "models.paths3m6qbmusersuseridmailfoldersmailfolderidmessagesmessageidmicrosoftgraphcreatereplyallpostrequestbodycontentapplicationjsonschema"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.microsoftgraphmessage"
        """Invoke action createReplyAll.

        Invoke action createReplyAll.

        :param user_id: key: id of user.
        :type user_id: str
        :param mail_folder_id: key: id of mailFolder.
        :type mail_folder_id: str
        :param message_id: key: id of message.
        :type message_id: str
        :param body: Action parameters.
        :type body: ~users_actions.models.paths3m6qbmusersuseridmailfoldersmailfolderidmessagesmessageidmicrosoftgraphcreatereplyallpostrequestbodycontentapplicationjsonschema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphmessage, or the result of cls(response)
        :rtype: ~users_actions.models.microsoftgraphmessage
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphmessage"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_reply_all.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'mailFolder-id': self._serialize.url("mail_folder_id", mail_folder_id, 'str'),
            'message-id': self._serialize.url("message_id", message_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'paths3m6qbmusersuseridmailfoldersmailfolderidmessagesmessageidmicrosoftgraphcreatereplyallpostrequestbodycontentapplicationjsonschema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphmessage', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_reply_all.metadata = {'url': '/users/{user-id}/mailFolders/{mailFolder-id}/messages/{message-id}/microsoft.graph.createReplyAll'}  # type: ignore

    def forward(
        self,
        user_id,  # type: str
        mail_folder_id,  # type: str
        message_id,  # type: str
        body,  # type: "models.paths1x7dum0usersuseridmailfoldersmailfolderidmessagesmessageidmicrosoftgraphforwardpostrequestbodycontentapplicationjsonschema"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Invoke action forward.

        Invoke action forward.

        :param user_id: key: id of user.
        :type user_id: str
        :param mail_folder_id: key: id of mailFolder.
        :type mail_folder_id: str
        :param message_id: key: id of message.
        :type message_id: str
        :param body: Action parameters.
        :type body: ~users_actions.models.paths1x7dum0usersuseridmailfoldersmailfolderidmessagesmessageidmicrosoftgraphforwardpostrequestbodycontentapplicationjsonschema
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
        url = self.forward.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'mailFolder-id': self._serialize.url("mail_folder_id", mail_folder_id, 'str'),
            'message-id': self._serialize.url("message_id", message_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'paths1x7dum0usersuseridmailfoldersmailfolderidmessagesmessageidmicrosoftgraphforwardpostrequestbodycontentapplicationjsonschema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    forward.metadata = {'url': '/users/{user-id}/mailFolders/{mailFolder-id}/messages/{message-id}/microsoft.graph.forward'}  # type: ignore

    def move(
        self,
        user_id,  # type: str
        mail_folder_id,  # type: str
        message_id,  # type: str
        body,  # type: "models.paths1ph8596usersuseridmailfoldersmailfolderidmessagesmessageidmicrosoftgraphmovepostrequestbodycontentapplicationjsonschema"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.microsoftgraphmessage"
        """Invoke action move.

        Invoke action move.

        :param user_id: key: id of user.
        :type user_id: str
        :param mail_folder_id: key: id of mailFolder.
        :type mail_folder_id: str
        :param message_id: key: id of message.
        :type message_id: str
        :param body: Action parameters.
        :type body: ~users_actions.models.paths1ph8596usersuseridmailfoldersmailfolderidmessagesmessageidmicrosoftgraphmovepostrequestbodycontentapplicationjsonschema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphmessage, or the result of cls(response)
        :rtype: ~users_actions.models.microsoftgraphmessage
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphmessage"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.move.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'mailFolder-id': self._serialize.url("mail_folder_id", mail_folder_id, 'str'),
            'message-id': self._serialize.url("message_id", message_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'paths1ph8596usersuseridmailfoldersmailfolderidmessagesmessageidmicrosoftgraphmovepostrequestbodycontentapplicationjsonschema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphmessage', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    move.metadata = {'url': '/users/{user-id}/mailFolders/{mailFolder-id}/messages/{message-id}/microsoft.graph.move'}  # type: ignore

    def reply(
        self,
        user_id,  # type: str
        mail_folder_id,  # type: str
        message_id,  # type: str
        body,  # type: "models.paths6zjq1husersuseridmailfoldersmailfolderidmessagesmessageidmicrosoftgraphreplypostrequestbodycontentapplicationjsonschema"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Invoke action reply.

        Invoke action reply.

        :param user_id: key: id of user.
        :type user_id: str
        :param mail_folder_id: key: id of mailFolder.
        :type mail_folder_id: str
        :param message_id: key: id of message.
        :type message_id: str
        :param body: Action parameters.
        :type body: ~users_actions.models.paths6zjq1husersuseridmailfoldersmailfolderidmessagesmessageidmicrosoftgraphreplypostrequestbodycontentapplicationjsonschema
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
        url = self.reply.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'mailFolder-id': self._serialize.url("mail_folder_id", mail_folder_id, 'str'),
            'message-id': self._serialize.url("message_id", message_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'paths6zjq1husersuseridmailfoldersmailfolderidmessagesmessageidmicrosoftgraphreplypostrequestbodycontentapplicationjsonschema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    reply.metadata = {'url': '/users/{user-id}/mailFolders/{mailFolder-id}/messages/{message-id}/microsoft.graph.reply'}  # type: ignore

    def reply_all(
        self,
        user_id,  # type: str
        mail_folder_id,  # type: str
        message_id,  # type: str
        body,  # type: "models.paths16mdb34usersuseridmailfoldersmailfolderidmessagesmessageidmicrosoftgraphreplyallpostrequestbodycontentapplicationjsonschema"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Invoke action replyAll.

        Invoke action replyAll.

        :param user_id: key: id of user.
        :type user_id: str
        :param mail_folder_id: key: id of mailFolder.
        :type mail_folder_id: str
        :param message_id: key: id of message.
        :type message_id: str
        :param body: Action parameters.
        :type body: ~users_actions.models.paths16mdb34usersuseridmailfoldersmailfolderidmessagesmessageidmicrosoftgraphreplyallpostrequestbodycontentapplicationjsonschema
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
        url = self.reply_all.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'mailFolder-id': self._serialize.url("mail_folder_id", mail_folder_id, 'str'),
            'message-id': self._serialize.url("message_id", message_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'paths16mdb34usersuseridmailfoldersmailfolderidmessagesmessageidmicrosoftgraphreplyallpostrequestbodycontentapplicationjsonschema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    reply_all.metadata = {'url': '/users/{user-id}/mailFolders/{mailFolder-id}/messages/{message-id}/microsoft.graph.replyAll'}  # type: ignore

    def send(
        self,
        user_id,  # type: str
        mail_folder_id,  # type: str
        message_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Invoke action send.

        Invoke action send.

        :param user_id: key: id of user.
        :type user_id: str
        :param mail_folder_id: key: id of mailFolder.
        :type mail_folder_id: str
        :param message_id: key: id of message.
        :type message_id: str
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
        url = self.send.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'mailFolder-id': self._serialize.url("mail_folder_id", mail_folder_id, 'str'),
            'message-id': self._serialize.url("message_id", message_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    send.metadata = {'url': '/users/{user-id}/mailFolders/{mailFolder-id}/messages/{message-id}/microsoft.graph.send'}  # type: ignore
