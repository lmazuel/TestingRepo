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


class OperationDisplay(Model):
    """The object that represents the operation.

    :param provider: The service provider: Microsoft.HDInsight
    :type provider: str
    :param resource: The resource on which the operation is performed:
     Cluster, Capabilities, etc.
    :type resource: str
    :param operation: The operation type: read, write, delete, etc.
    :type operation: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
    }

    def __init__(self, provider=None, resource=None, operation=None):
        self.provider = provider
        self.resource = resource
        self.operation = operation
