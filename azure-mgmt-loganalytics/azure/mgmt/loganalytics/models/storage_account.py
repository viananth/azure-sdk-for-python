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


class StorageAccount(Model):
    """Describes a storage account connection.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. The Azure Resource Manager ID of the storage account
     resource.
    :type id: str
    :param key: Required. The storage account key.
    :type key: str
    """

    _validation = {
        'id': {'required': True},
        'key': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'key': {'key': 'key', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(StorageAccount, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.key = kwargs.get('key', None)
