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


class JobStepExecutionOptions(Model):
    """The execution options of a job step.

    :param timeout_seconds: Execution timeout for the job step. Default value:
     43200 .
    :type timeout_seconds: int
    :param retry_attempts: Maximum number of times the job step will be
     reattempted if the first attempt fails. Default value: 10 .
    :type retry_attempts: int
    :param initial_retry_interval_seconds: Initial delay between retries for
     job step execution. Default value: 1 .
    :type initial_retry_interval_seconds: int
    :param maximum_retry_interval_seconds: The maximum amount of time to wait
     between retries for job step execution. Default value: 120 .
    :type maximum_retry_interval_seconds: int
    :param retry_interval_backoff_multiplier: The backoff multiplier for the
     time between retries. Default value: 2 .
    :type retry_interval_backoff_multiplier: float
    """

    _attribute_map = {
        'timeout_seconds': {'key': 'timeoutSeconds', 'type': 'int'},
        'retry_attempts': {'key': 'retryAttempts', 'type': 'int'},
        'initial_retry_interval_seconds': {'key': 'initialRetryIntervalSeconds', 'type': 'int'},
        'maximum_retry_interval_seconds': {'key': 'maximumRetryIntervalSeconds', 'type': 'int'},
        'retry_interval_backoff_multiplier': {'key': 'retryIntervalBackoffMultiplier', 'type': 'float'},
    }

    def __init__(self, *, timeout_seconds: int=43200, retry_attempts: int=10, initial_retry_interval_seconds: int=1, maximum_retry_interval_seconds: int=120, retry_interval_backoff_multiplier: float=2, **kwargs) -> None:
        super(JobStepExecutionOptions, self).__init__(**kwargs)
        self.timeout_seconds = timeout_seconds
        self.retry_attempts = retry_attempts
        self.initial_retry_interval_seconds = initial_retry_interval_seconds
        self.maximum_retry_interval_seconds = maximum_retry_interval_seconds
        self.retry_interval_backoff_multiplier = retry_interval_backoff_multiplier
