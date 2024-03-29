# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from msrest.pipeline import ClientRawResponse
from msrest.exceptions import HttpOperationError
from .BatchSetup import BatchSetup
from . import models
import json


class MAQTextAnalyticsLinuxConfiguration(Configuration):
    """Configuration for MAQTextAnalyticsLinux
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param str base_url: Service URL
    """

    def __init__(self, base_url=None):

        if not base_url:
            base_url = "https://maqtextnalyticssdk.azure-api.net/text"

        super(MAQTextAnalyticsLinuxConfiguration, self).__init__(base_url)

        self.add_user_agent("maqtextanalyticslinux/{}".format(VERSION))


class MAQTextAnalyticsLinux(SDKClient):
    """Import from "MAQTextAnalyticsLinux" Function App

    :ivar config: Configuration for client.
    :vartype config: MAQTextAnalyticsLinuxConfiguration

    :param str base_url: Service URL
    """

    def __init__(self, base_url=None):

        self.config = MAQTextAnalyticsLinuxConfiguration(base_url)
        super(MAQTextAnalyticsLinux, self).__init__(None, self.config)

        client_models = {
            k: v for k, v in models.__dict__.items() if isinstance(v, type)
        }
        self.api_version = "1.0"
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    def post_sentimentclassifier(
        self,
        api_key,
        data_input=None,
        custom_headers=None,
        raw=False,
        **operation_config
    ):
        """SentimentClassifier.

        :param api_key: JWT Key
        :type api_key: str
        :param data_input:
        :type data_input: ~maqtextanalyticslinux.models.DataInput
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype: list[~maqtextanalyticslinux.models.ResponseBodyItem] or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.post_sentimentclassifier.metadata["url"]

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters["Accept"] = "application/json"
        header_parameters["Content-Type"] = "application/json; charset=utf-8"
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters["APIKey"] = self._serialize.header("api_key", api_key, "str")

        # Construct body
        inputTransform = BatchSetup(data_input)
        if data_input is not None:
            body_content = self._serialize.body(inputTransform.makeBody(), "DataInput")
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(
            url, query_parameters, header_parameters, body_content
        )
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            if "errors" in json.loads(response.text):
                response.reason = json.loads(response.text)["errors"][0]["message"]
                raise HttpOperationError(self._deserialize, response)
            else:
                response.reason = json.loads(response.text)["message"]
                raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            results = json.loads(response.text)
            for idx, data in enumerate(body_content["data"]):
                results[idx]["text"] = data["text"]
            return results
            deserialized = self._deserialize("[ResponseBodyItem]", response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    post_sentimentclassifier.metadata = {"url": "/SentimentClassifier"}

    def post_piiscrubber(
        self,
        api_key,
        data_input=None,
        custom_headers=None,
        raw=False,
        **operation_config
    ):
        """PIIScrubber.

        :param api_key: JWT Key
        :type api_key: str
        :param data_input:
        :type data_input: ~maqtextanalyticslinux.models.PIIScrubberInput
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype: list[~maqtextanalyticslinux.models.PIIScrubberResponse] or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.post_piiscrubber.metadata["url"]

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters["Accept"] = "application/json"
        header_parameters["Content-Type"] = "application/json; charset=utf-8"
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters["APIKey"] = self._serialize.header("api_key", api_key, "str")

        # Construct data input
        try:
            if data_input["entity_list"] and isinstance(
                data_input["entity_list"], list
            ):
                data_input["entity_list"] = ",".join(data_input["entity_list"])
            else:
                raise Exception
        except:
            raise Exception(
                """InvalidJSONError: Not a valid format. Expected 'entity_list' as a key with list of entities in input json. Please send json in template as such {data: "text here", entity_list: ["entity1", "entity2"]}"""
            )

        # Construct body
        if data_input is not None:
            body_content = self._serialize.body(data_input, "PIIScrubberInput")
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(
            url, query_parameters, header_parameters, body_content
        )
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            if "errors" in json.loads(response.text):
                response.reason = json.loads(response.text)["errors"][0]["message"]
                raise HttpOperationError(self._deserialize, response)
            else:
                response.reason = json.loads(response.text)["message"]
                raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            results = json.loads(response.text)
            return results

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    post_piiscrubber.metadata = {"url": "/PIIScrubber"}

    def post_keyphrase_extractor(
        self,
        api_key,
        data_input=None,
        custom_headers=None,
        raw=False,
        **operation_config
    ):
        """KeyPhrase.

        :param api_key: JWT Key
        :type api_key: str
        :param data_input:
        :type data_input: ~maqtextanalyticslinux.models.KeyPhraseInput
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype: list[~maqtextanalyticslinux.models.KeyPhraseResponseItem] or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.post_keyphrase_extractor.metadata["url"]

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters["Accept"] = "application/json"
        header_parameters["Content-Type"] = "application/json; charset=utf-8"
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters["APIKey"] = self._serialize.header("api_key", api_key, "str")

        # Construct body
        if data_input is not None:
            body_content = self._serialize.body(data_input, "KeyPhraseInput")
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(
            url, query_parameters, header_parameters, body_content
        )
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            if "errors" in json.loads(response.text):
                response.reason = json.loads(response.text)["errors"][0]["message"]
                raise HttpOperationError(self._deserialize, response)
            else:
                response.reason = json.loads(response.text)["message"]
                raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            results = json.loads(response.text)
            return results

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    post_keyphrase_extractor.metadata = {"url": "/KeyPhrase"}
