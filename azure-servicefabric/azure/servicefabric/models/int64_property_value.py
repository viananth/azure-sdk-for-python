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

from .property_value import PropertyValue


class Int64PropertyValue(PropertyValue):
    """Describes a Service Fabric property value of type Int64.

    :param kind: Polymorphic Discriminator
    :type kind: str
    :param data: The data of the property value.
    :type data: str
    """

    _validation = {
        'kind': {'required': True},
        'data': {'required': True},
    }

    _attribute_map = {
        'kind': {'key': 'Kind', 'type': 'str'},
        'data': {'key': 'Data', 'type': 'str'},
    }

    def __init__(self, data):
        super(Int64PropertyValue, self).__init__()
        self.data = data
        self.kind = 'Int64'
