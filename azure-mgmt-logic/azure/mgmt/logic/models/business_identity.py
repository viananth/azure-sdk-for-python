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


class BusinessIdentity(Model):
    """The integration account partner's business identity.

    All required parameters must be populated in order to send to Azure.

    :param qualifier: Required. The business identity qualifier e.g.
     as2identity, ZZ, ZZZ, 31, 32
    :type qualifier: str
    :param value: Required. The user defined business identity value.
    :type value: str
    """

    _validation = {
        'qualifier': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'qualifier': {'key': 'qualifier', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(BusinessIdentity, self).__init__(**kwargs)
        self.qualifier = kwargs.get('qualifier', None)
        self.value = kwargs.get('value', None)
