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

from .iaa_svm_protectable_item_py3 import IaaSVMProtectableItem


class AzureIaaSClassicComputeVMProtectableItem(IaaSVMProtectableItem):
    """IaaS VM workload-specific backup item representing the Classic Compute VM.

    All required parameters must be populated in order to send to Azure.

    :param backup_management_type: Type of backup managemenent to backup an
     item.
    :type backup_management_type: str
    :param workload_type: Type of workload for the backup management
    :type workload_type: str
    :param friendly_name: Friendly name of the backup item.
    :type friendly_name: str
    :param protection_state: State of the back up item. Possible values
     include: 'Invalid', 'NotProtected', 'Protecting', 'Protected',
     'ProtectionFailed'
    :type protection_state: str or
     ~azure.mgmt.recoveryservicesbackup.models.ProtectionStatus
    :param protectable_item_type: Required. Constant filled by server.
    :type protectable_item_type: str
    :param virtual_machine_id: Fully qualified ARM ID of the virtual machine.
    :type virtual_machine_id: str
    """

    _validation = {
        'protectable_item_type': {'required': True},
    }

    _attribute_map = {
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
        'workload_type': {'key': 'workloadType', 'type': 'str'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'protection_state': {'key': 'protectionState', 'type': 'str'},
        'protectable_item_type': {'key': 'protectableItemType', 'type': 'str'},
        'virtual_machine_id': {'key': 'virtualMachineId', 'type': 'str'},
    }

    def __init__(self, *, backup_management_type: str=None, workload_type: str=None, friendly_name: str=None, protection_state=None, virtual_machine_id: str=None, **kwargs) -> None:
        super(AzureIaaSClassicComputeVMProtectableItem, self).__init__(backup_management_type=backup_management_type, workload_type=workload_type, friendly_name=friendly_name, protection_state=protection_state, virtual_machine_id=virtual_machine_id, **kwargs)
        self.protectable_item_type = 'Microsoft.ClassicCompute/virtualMachines'
