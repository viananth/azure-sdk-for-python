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


class RankingRankingResponse(Model):
    """Defines where on the search results page content should be placed and in
    what order.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar pole: The search results that should be afforded the most visible
     treatment (for example, displayed above the mainline and sidebar).
    :vartype pole:
     ~azure.cognitiveservices.search.websearch.models.RankingRankingGroup
    :ivar mainline: The search results to display in the mainline.
    :vartype mainline:
     ~azure.cognitiveservices.search.websearch.models.RankingRankingGroup
    :ivar sidebar: The search results to display in the sidebar.
    :vartype sidebar:
     ~azure.cognitiveservices.search.websearch.models.RankingRankingGroup
    """

    _validation = {
        'pole': {'readonly': True},
        'mainline': {'readonly': True},
        'sidebar': {'readonly': True},
    }

    _attribute_map = {
        'pole': {'key': 'pole', 'type': 'RankingRankingGroup'},
        'mainline': {'key': 'mainline', 'type': 'RankingRankingGroup'},
        'sidebar': {'key': 'sidebar', 'type': 'RankingRankingGroup'},
    }

    def __init__(self, **kwargs) -> None:
        super(RankingRankingResponse, self).__init__(**kwargs)
        self.pole = None
        self.mainline = None
        self.sidebar = None
