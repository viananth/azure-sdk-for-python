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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from .version import VERSION


class DnsManagementClientConfiguration(AzureConfiguration):
    """Configuration for DnsManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(DnsManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-dns/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class DnsManagementClient(MultiApiClientMixin, SDKClient):
    """The DNS Management Client.

    This ready contains multiple API versions, to help you deal with all Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, uses latest API version available on public Azure.
    For production, you should stick a particular api-version and/or profile.
    The profile sets a mapping between the operation group and an API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :ivar config: Configuration for client.
    :vartype config: DnsManagementClientConfiguration

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION = '2018-03-01-preview'
    _PROFILE_TAG = "azure.mgmt.dns.DnsManagementClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(self, credentials, subscription_id, api_version=None, base_url=None, profile=KnownProfiles.default):
        self.config = DnsManagementClientConfiguration(credentials, subscription_id, base_url)
        super(DnsManagementClient, self).__init__(
            credentials,
            self.config,
            api_version=api_version,
            profile=profile
        )

############ Generated from here ############

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2016-04-01: :mod:`v2016_04_01.models<azure.mgmt.dns.v2016_04_01.models>`
           * 2018-03-01-preview: :mod:`v2018_03_01_preview.models<azure.mgmt.dns.v2018_03_01_preview.models>`
           * 2018-05-01: :mod:`v2018_05_01.models<azure.mgmt.dns.v2018_05_01.models>`
        """
        if api_version == '2016-04-01':
            from .v2016_04_01 import models
            return models
        elif api_version == '2018-03-01-preview':
            from .v2018_03_01_preview import models
            return models
        elif api_version == '2018-05-01':
            from .v2018_05_01 import models
            return models
        raise NotImplementedError("APIVersion {} is not available".format(api_version))
    
    @property
    def dns_resource_reference(self):
        """Instance depends on the API version:

           * 2018-05-01: :class:`DnsResourceReferenceOperations<azure.mgmt.dns.v2018_05_01.operations.DnsResourceReferenceOperations>`
        """
        api_version = self._get_api_version('dns_resource_reference')
        if api_version == '2018-05-01':
            from .v2018_05_01.operations import DnsResourceReferenceOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def record_sets(self):
        """Instance depends on the API version:

           * 2016-04-01: :class:`RecordSetsOperations<azure.mgmt.dns.v2016_04_01.operations.RecordSetsOperations>`
           * 2018-03-01-preview: :class:`RecordSetsOperations<azure.mgmt.dns.v2018_03_01_preview.operations.RecordSetsOperations>`
           * 2018-05-01: :class:`RecordSetsOperations<azure.mgmt.dns.v2018_05_01.operations.RecordSetsOperations>`
        """
        api_version = self._get_api_version('record_sets')
        if api_version == '2016-04-01':
            from .v2016_04_01.operations import RecordSetsOperations as OperationClass
        elif api_version == '2018-03-01-preview':
            from .v2018_03_01_preview.operations import RecordSetsOperations as OperationClass
        elif api_version == '2018-05-01':
            from .v2018_05_01.operations import RecordSetsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def zones(self):
        """Instance depends on the API version:

           * 2016-04-01: :class:`ZonesOperations<azure.mgmt.dns.v2016_04_01.operations.ZonesOperations>`
           * 2018-03-01-preview: :class:`ZonesOperations<azure.mgmt.dns.v2018_03_01_preview.operations.ZonesOperations>`
           * 2018-05-01: :class:`ZonesOperations<azure.mgmt.dns.v2018_05_01.operations.ZonesOperations>`
        """
        api_version = self._get_api_version('zones')
        if api_version == '2016-04-01':
            from .v2016_04_01.operations import ZonesOperations as OperationClass
        elif api_version == '2018-03-01-preview':
            from .v2018_03_01_preview.operations import ZonesOperations as OperationClass
        elif api_version == '2018-05-01':
            from .v2018_05_01.operations import ZonesOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))
