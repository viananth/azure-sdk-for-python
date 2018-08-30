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


class EdifactProcessingSettings(Model):
    """The Edifact agreement protocol settings.

    All required parameters must be populated in order to send to Azure.

    :param mask_security_info: Required. The value indicating whether to mask
     security information.
    :type mask_security_info: bool
    :param preserve_interchange: Required. The value indicating whether to
     preserve interchange.
    :type preserve_interchange: bool
    :param suspend_interchange_on_error: Required. The value indicating
     whether to suspend interchange on error.
    :type suspend_interchange_on_error: bool
    :param create_empty_xml_tags_for_trailing_separators: Required. The value
     indicating whether to create empty xml tags for trailing separators.
    :type create_empty_xml_tags_for_trailing_separators: bool
    :param use_dot_as_decimal_separator: Required. The value indicating
     whether to use dot as decimal separator.
    :type use_dot_as_decimal_separator: bool
    """

    _validation = {
        'mask_security_info': {'required': True},
        'preserve_interchange': {'required': True},
        'suspend_interchange_on_error': {'required': True},
        'create_empty_xml_tags_for_trailing_separators': {'required': True},
        'use_dot_as_decimal_separator': {'required': True},
    }

    _attribute_map = {
        'mask_security_info': {'key': 'maskSecurityInfo', 'type': 'bool'},
        'preserve_interchange': {'key': 'preserveInterchange', 'type': 'bool'},
        'suspend_interchange_on_error': {'key': 'suspendInterchangeOnError', 'type': 'bool'},
        'create_empty_xml_tags_for_trailing_separators': {'key': 'createEmptyXmlTagsForTrailingSeparators', 'type': 'bool'},
        'use_dot_as_decimal_separator': {'key': 'useDotAsDecimalSeparator', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(EdifactProcessingSettings, self).__init__(**kwargs)
        self.mask_security_info = kwargs.get('mask_security_info', None)
        self.preserve_interchange = kwargs.get('preserve_interchange', None)
        self.suspend_interchange_on_error = kwargs.get('suspend_interchange_on_error', None)
        self.create_empty_xml_tags_for_trailing_separators = kwargs.get('create_empty_xml_tags_for_trailing_separators', None)
        self.use_dot_as_decimal_separator = kwargs.get('use_dot_as_decimal_separator', None)
