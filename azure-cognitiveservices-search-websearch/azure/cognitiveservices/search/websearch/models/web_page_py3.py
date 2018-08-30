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

from .creative_work import CreativeWork


class WebPage(CreativeWork):
    """Defines a webpage that is relevant to the query.

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
    :ivar thumbnail_url: The URL to a thumbnail of the item.
    :vartype thumbnail_url: str
    :ivar provider: The source of the creative work.
    :vartype provider:
     list[~azure.cognitiveservices.search.websearch.models.Thing]
    :ivar text:
    :vartype text: str
    :ivar display_url: The display URL of the webpage. The URL is meant for
     display purposes only and is not well formed.
    :vartype display_url: str
    :ivar snippet: A snippet of text from the webpage that describes its
     contents.
    :vartype snippet: str
    :ivar deep_links: A list of links to related content that Bing found in
     the website that contains this webpage. The Webpage object in this context
     includes only the name, url, urlPingSuffix, and snippet fields.
    :vartype deep_links:
     list[~azure.cognitiveservices.search.websearch.models.WebPage]
    :ivar date_last_crawled: The last time that Bing crawled the webpage. The
     date is in the form, YYYY-MM-DDTHH:MM:SS. For example,
     2015-04-13T05:23:39.
    :vartype date_last_crawled: str
    :ivar search_tags: A list of search tags that the webpage owner specified
     on the webpage. The API returns only indexed search tags. The name field
     of the MetaTag object contains the indexed search tag. Search tags begin
     with search.* (for example, search.assetId). The content field contains
     the tag's value.
    :vartype search_tags:
     list[~azure.cognitiveservices.search.websearch.models.WebMetaTag]
    :ivar primary_image_of_page:
    :vartype primary_image_of_page:
     ~azure.cognitiveservices.search.websearch.models.ImageObject
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
        'thumbnail_url': {'readonly': True},
        'provider': {'readonly': True},
        'text': {'readonly': True},
        'display_url': {'readonly': True},
        'snippet': {'readonly': True},
        'deep_links': {'readonly': True},
        'date_last_crawled': {'readonly': True},
        'search_tags': {'readonly': True},
        'primary_image_of_page': {'readonly': True},
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
        'thumbnail_url': {'key': 'thumbnailUrl', 'type': 'str'},
        'provider': {'key': 'provider', 'type': '[Thing]'},
        'text': {'key': 'text', 'type': 'str'},
        'display_url': {'key': 'displayUrl', 'type': 'str'},
        'snippet': {'key': 'snippet', 'type': 'str'},
        'deep_links': {'key': 'deepLinks', 'type': '[WebPage]'},
        'date_last_crawled': {'key': 'dateLastCrawled', 'type': 'str'},
        'search_tags': {'key': 'searchTags', 'type': '[WebMetaTag]'},
        'primary_image_of_page': {'key': 'primaryImageOfPage', 'type': 'ImageObject'},
    }

    def __init__(self, **kwargs) -> None:
        super(WebPage, self).__init__(**kwargs)
        self.display_url = None
        self.snippet = None
        self.deep_links = None
        self.date_last_crawled = None
        self.search_tags = None
        self.primary_image_of_page = None
        self._type = 'WebPage'
