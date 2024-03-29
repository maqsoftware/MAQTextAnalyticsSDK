# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.1.3, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import List, Optional

import msrest.serialization


class KeyPhraseInput(msrest.serialization.Model):
    """KeyPhraseInput.

    :ivar text:
    :vartype text: str
    :ivar keyphrases_count:
    :vartype keyphrases_count: int
    :ivar diversity_threshold:
    :vartype diversity_threshold: float
    :ivar alias_threshold:
    :vartype alias_threshold: float
    """

    _attribute_map = {
        'text': {'key': 'text', 'type': 'str'},
        'keyphrases_count': {'key': 'keyphrases_count', 'type': 'int'},
        'diversity_threshold': {'key': 'diversity_threshold', 'type': 'float'},
        'alias_threshold': {'key': 'alias_threshold', 'type': 'float'},
    }

    def __init__(
        self,
        *,
        text: Optional[str] = None,
        keyphrases_count: Optional[int] = None,
        diversity_threshold: Optional[float] = None,
        alias_threshold: Optional[float] = None,
        **kwargs
    ):
        """
        :keyword text:
        :paramtype text: str
        :keyword keyphrases_count:
        :paramtype keyphrases_count: int
        :keyword diversity_threshold:
        :paramtype diversity_threshold: float
        :keyword alias_threshold:
        :paramtype alias_threshold: float
        """
        super(KeyPhraseInput, self).__init__(**kwargs)
        self.text = text
        self.keyphrases_count = keyphrases_count
        self.diversity_threshold = diversity_threshold
        self.alias_threshold = alias_threshold


class KeyPhraseResponseItem(msrest.serialization.Model):
    """KeyPhraseResponseItem.

    All required parameters must be populated in order to send to Azure.

    :ivar key_phrase: Required.
    :vartype key_phrase: str
    :ivar score: Required.
    :vartype score: int
    :ivar similar: Required.
    :vartype similar: list[str]
    """

    _validation = {
        'key_phrase': {'required': True},
        'score': {'required': True},
        'similar': {'required': True},
    }

    _attribute_map = {
        'key_phrase': {'key': 'KeyPhrase', 'type': 'str'},
        'score': {'key': 'Score', 'type': 'int'},
        'similar': {'key': 'Similar', 'type': '[str]'},
    }

    def __init__(
        self,
        *,
        key_phrase: str,
        score: int,
        similar: List[str],
        **kwargs
    ):
        """
        :keyword key_phrase: Required.
        :paramtype key_phrase: str
        :keyword score: Required.
        :paramtype score: int
        :keyword similar: Required.
        :paramtype similar: list[str]
        """
        super(KeyPhraseResponseItem, self).__init__(**kwargs)
        self.key_phrase = key_phrase
        self.score = score
        self.similar = similar


class PIIScrubberInput(msrest.serialization.Model):
    """PIIScrubberInput.

    :ivar data:
    :vartype data: str
    :ivar entity_list:
    :vartype entity_list: str
    """

    _attribute_map = {
        'data': {'key': 'data', 'type': 'str'},
        'entity_list': {'key': 'entity_list', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        data: Optional[str] = None,
        entity_list: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword data:
        :paramtype data: str
        :keyword entity_list:
        :paramtype entity_list: str
        """
        super(PIIScrubberInput, self).__init__(**kwargs)
        self.data = data
        self.entity_list = entity_list


class PIIScrubberResponse(msrest.serialization.Model):
    """PIIScrubberResponse.

    :ivar scrubbed_text:
    :vartype scrubbed_text: str
    """

    _attribute_map = {
        'scrubbed_text': {'key': 'scrubbed_text', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        scrubbed_text: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword scrubbed_text:
        :paramtype scrubbed_text: str
        """
        super(PIIScrubberResponse, self).__init__(**kwargs)
        self.scrubbed_text = scrubbed_text
