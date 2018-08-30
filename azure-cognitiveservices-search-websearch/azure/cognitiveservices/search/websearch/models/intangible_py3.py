# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .thing import Thing


class Intangible(Thing):
    """Intangible.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: StructuredValue

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar name: The name of the thing represented by this object.
    :vartype name: str
    :ivar url: The URL to get more information about the thing represented by
     this object.
    :vartype url: str
    :ivar image:
    :vartype image:
     ~azure.cognitiveservices.search.websearch.models.ImageObject
    :ivar description: A short description of the item.
    :vartype description: str
    :ivar bing_id: An ID that uniquely identifies this item.
    :vartype bing_id: str
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'web_search_url': {'readonly': True},
        'name': {'readonly': True},
        'url': {'readonly': True},
        'image': {'readonly': True},
        'description': {'readonly': True},
        'bing_id': {'readonly': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'image': {'key': 'image', 'type': 'ImageObject'},
        'description': {'key': 'description', 'type': 'str'},
        'bing_id': {'key': 'bingId', 'type': 'str'},
    }

    _subtype_map = {
        '_type': {'StructuredValue': 'StructuredValue'}
    }

    def __init__(self, **kwargs) -> None:
        super(Intangible, self).__init__(**kwargs)
        self._type = 'Intangible'
