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


class BEKDetails(Model):
    """BEK is bitlocker encrpytion key.

    :param secret_url: Secret is BEK.
    :type secret_url: str
    :param secret_vault_id: ID of the Key Vault where this Secret is stored.
    :type secret_vault_id: str
    :param secret_data: BEK data.
    :type secret_data: str
    """

    _attribute_map = {
        'secret_url': {'key': 'secretUrl', 'type': 'str'},
        'secret_vault_id': {'key': 'secretVaultId', 'type': 'str'},
        'secret_data': {'key': 'secretData', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(BEKDetails, self).__init__(**kwargs)
        self.secret_url = kwargs.get('secret_url', None)
        self.secret_vault_id = kwargs.get('secret_vault_id', None)
        self.secret_data = kwargs.get('secret_data', None)
