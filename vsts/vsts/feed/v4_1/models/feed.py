# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class Feed(Model):
    """Feed.

    :param _links:
    :type _links: :class:`ReferenceLinks <packaging.v4_1.models.ReferenceLinks>`
    :param allow_upstream_name_conflict: If set, the feed will allow upload of packages that exist on the upstream
    :type allow_upstream_name_conflict: bool
    :param badges_enabled:
    :type badges_enabled: bool
    :param capabilities:
    :type capabilities: object
    :param default_view_id:
    :type default_view_id: str
    :param deleted_date:
    :type deleted_date: datetime
    :param description:
    :type description: str
    :param fully_qualified_id:
    :type fully_qualified_id: str
    :param fully_qualified_name:
    :type fully_qualified_name: str
    :param hide_deleted_package_versions: If set, feed will hide all deleted/unpublished versions
    :type hide_deleted_package_versions: bool
    :param id:
    :type id: str
    :param is_read_only:
    :type is_read_only: bool
    :param name:
    :type name: str
    :param permissions:
    :type permissions: list of :class:`FeedPermission <packaging.v4_1.models.FeedPermission>`
    :param upstream_enabled: If set, the feed can proxy packages from an upstream feed
    :type upstream_enabled: bool
    :param upstream_enabled_changed_date: If set, time that the UpstreamEnabled property was changed. Will be null if UpstreamEnabled was never changed after Feed creation.
    :type upstream_enabled_changed_date: datetime
    :param upstream_sources:
    :type upstream_sources: list of :class:`UpstreamSource <packaging.v4_1.models.UpstreamSource>`
    :param url:
    :type url: str
    :param view:
    :type view: :class:`FeedView <packaging.v4_1.models.FeedView>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'allow_upstream_name_conflict': {'key': 'allowUpstreamNameConflict', 'type': 'bool'},
        'badges_enabled': {'key': 'badgesEnabled', 'type': 'bool'},
        'capabilities': {'key': 'capabilities', 'type': 'object'},
        'default_view_id': {'key': 'defaultViewId', 'type': 'str'},
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'fully_qualified_id': {'key': 'fullyQualifiedId', 'type': 'str'},
        'fully_qualified_name': {'key': 'fullyQualifiedName', 'type': 'str'},
        'hide_deleted_package_versions': {'key': 'hideDeletedPackageVersions', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'str'},
        'is_read_only': {'key': 'isReadOnly', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'permissions': {'key': 'permissions', 'type': '[FeedPermission]'},
        'upstream_enabled': {'key': 'upstreamEnabled', 'type': 'bool'},
        'upstream_enabled_changed_date': {'key': 'upstreamEnabledChangedDate', 'type': 'iso-8601'},
        'upstream_sources': {'key': 'upstreamSources', 'type': '[UpstreamSource]'},
        'url': {'key': 'url', 'type': 'str'},
        'view': {'key': 'view', 'type': 'FeedView'}
    }

    def __init__(self, _links=None, allow_upstream_name_conflict=None, badges_enabled=None, capabilities=None, default_view_id=None, deleted_date=None, description=None, fully_qualified_id=None, fully_qualified_name=None, hide_deleted_package_versions=None, id=None, is_read_only=None, name=None, permissions=None, upstream_enabled=None, upstream_enabled_changed_date=None, upstream_sources=None, url=None, view=None):
        super(Feed, self).__init__()
        self._links = _links
        self.allow_upstream_name_conflict = allow_upstream_name_conflict
        self.badges_enabled = badges_enabled
        self.capabilities = capabilities
        self.default_view_id = default_view_id
        self.deleted_date = deleted_date
        self.description = description
        self.fully_qualified_id = fully_qualified_id
        self.fully_qualified_name = fully_qualified_name
        self.hide_deleted_package_versions = hide_deleted_package_versions
        self.id = id
        self.is_read_only = is_read_only
        self.name = name
        self.permissions = permissions
        self.upstream_enabled = upstream_enabled
        self.upstream_enabled_changed_date = upstream_enabled_changed_date
        self.upstream_sources = upstream_sources
        self.url = url
        self.view = view
