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

from msrest.serialization import Model


class Query(Model):
    """Defines a search query.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param text: Required. The query string. Use this string as the query term
     in a new search request.
    :type text: str
    :ivar display_text: The display version of the query term. This version of
     the query term may contain special characters that highlight the search
     term found in the query string. The string contains the highlighting
     characters only if the query enabled hit highlighting
    :vartype display_text: str
    :ivar web_search_url: The URL that takes the user to the Bing search
     results page for the query.Only related search results include this field.
    :vartype web_search_url: str
    :ivar search_link:
    :vartype search_link: str
    :ivar thumbnail:
    :vartype thumbnail:
     ~azure.cognitiveservices.search.websearch.models.ImageObject
    """

    _validation = {
        'text': {'required': True},
        'display_text': {'readonly': True},
        'web_search_url': {'readonly': True},
        'search_link': {'readonly': True},
        'thumbnail': {'readonly': True},
    }

    _attribute_map = {
        'text': {'key': 'text', 'type': 'str'},
        'display_text': {'key': 'displayText', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'search_link': {'key': 'searchLink', 'type': 'str'},
        'thumbnail': {'key': 'thumbnail', 'type': 'ImageObject'},
    }

    def __init__(self, *, text: str, **kwargs) -> None:
        super(Query, self).__init__(**kwargs)
        self.text = text
        self.display_text = None
        self.web_search_url = None
        self.search_link = None
        self.thumbnail = None
