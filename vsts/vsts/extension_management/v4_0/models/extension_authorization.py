# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ExtensionAuthorization(Model):
    """ExtensionAuthorization.

    :param id:
    :type id: str
    :param scopes:
    :type scopes: list of str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'scopes': {'key': 'scopes', 'type': '[str]'}
    }

    def __init__(self, id=None, scopes=None):
        super(ExtensionAuthorization, self).__init__()
        self.id = id
        self.scopes = scopes
