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

from .update_resource_py3 import UpdateResource


class AvailabilitySetUpdate(UpdateResource):
    """Specifies information about the availability set that the virtual machine
    should be assigned to. Only tags may be updated.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param tags: Resource tags
    :type tags: dict[str, str]
    :param platform_update_domain_count: Update Domain count.
    :type platform_update_domain_count: int
    :param platform_fault_domain_count: Fault Domain count.
    :type platform_fault_domain_count: int
    :param virtual_machines: A list of references to all virtual machines in
     the availability set.
    :type virtual_machines:
     list[~azure.mgmt.compute.v2018_06_01.models.SubResource]
    :ivar statuses: The resource status information.
    :vartype statuses:
     list[~azure.mgmt.compute.v2018_06_01.models.InstanceViewStatus]
    :param sku: Sku of the availability set
    :type sku: ~azure.mgmt.compute.v2018_06_01.models.Sku
    """

    _validation = {
        'statuses': {'readonly': True},
    }

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'platform_update_domain_count': {'key': 'properties.platformUpdateDomainCount', 'type': 'int'},
        'platform_fault_domain_count': {'key': 'properties.platformFaultDomainCount', 'type': 'int'},
        'virtual_machines': {'key': 'properties.virtualMachines', 'type': '[SubResource]'},
        'statuses': {'key': 'properties.statuses', 'type': '[InstanceViewStatus]'},
        'sku': {'key': 'sku', 'type': 'Sku'},
    }

    def __init__(self, *, tags=None, platform_update_domain_count: int=None, platform_fault_domain_count: int=None, virtual_machines=None, sku=None, **kwargs) -> None:
        super(AvailabilitySetUpdate, self).__init__(tags=tags, **kwargs)
        self.platform_update_domain_count = platform_update_domain_count
        self.platform_fault_domain_count = platform_fault_domain_count
        self.virtual_machines = virtual_machines
        self.statuses = None
        self.sku = sku
