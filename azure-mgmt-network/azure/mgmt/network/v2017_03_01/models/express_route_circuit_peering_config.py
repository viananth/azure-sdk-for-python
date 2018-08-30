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


class ExpressRouteCircuitPeeringConfig(Model):
    """Specifies the peering configuration.

    :param advertised_public_prefixes: The reference of
     AdvertisedPublicPrefixes.
    :type advertised_public_prefixes: list[str]
    :param advertised_public_prefixes_state: AdvertisedPublicPrefixState of
     the Peering resource. Possible values are 'NotConfigured', 'Configuring',
     'Configured', and 'ValidationNeeded'. Possible values include:
     'NotConfigured', 'Configuring', 'Configured', 'ValidationNeeded'
    :type advertised_public_prefixes_state: str or
     ~azure.mgmt.network.v2017_03_01.models.ExpressRouteCircuitPeeringAdvertisedPublicPrefixState
    :param customer_asn: The CustomerASN of the peering.
    :type customer_asn: int
    :param routing_registry_name: The RoutingRegistryName of the
     configuration.
    :type routing_registry_name: str
    """

    _attribute_map = {
        'advertised_public_prefixes': {'key': 'advertisedPublicPrefixes', 'type': '[str]'},
        'advertised_public_prefixes_state': {'key': 'advertisedPublicPrefixesState', 'type': 'str'},
        'customer_asn': {'key': 'customerASN', 'type': 'int'},
        'routing_registry_name': {'key': 'routingRegistryName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ExpressRouteCircuitPeeringConfig, self).__init__(**kwargs)
        self.advertised_public_prefixes = kwargs.get('advertised_public_prefixes', None)
        self.advertised_public_prefixes_state = kwargs.get('advertised_public_prefixes_state', None)
        self.customer_asn = kwargs.get('customer_asn', None)
        self.routing_registry_name = kwargs.get('routing_registry_name', None)
