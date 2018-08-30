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


class JobPreparation(Model):
    """Specifies the settings for job preparation.

    All required parameters must be populated in order to send to Azure.

    :param command_line: Required. The command line to execute. If
     containerSettings is specified on the job, this commandLine will be
     executed in the same container as job. Otherwise it will be executed on
     the node.
    :type command_line: str
    """

    _validation = {
        'command_line': {'required': True},
    }

    _attribute_map = {
        'command_line': {'key': 'commandLine', 'type': 'str'},
    }

    def __init__(self, *, command_line: str, **kwargs) -> None:
        super(JobPreparation, self).__init__(**kwargs)
        self.command_line = command_line
