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


class PrivateAccessSubnet(Model):
    """Description of a Virtual Network subnet that is useable for private site
    access.

    :param name: The name of the subnet.
    :type name: str
    :param key: The key (ID) of the subnet.
    :type key: int
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'key': {'key': 'key', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(PrivateAccessSubnet, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.key = kwargs.get('key', None)
