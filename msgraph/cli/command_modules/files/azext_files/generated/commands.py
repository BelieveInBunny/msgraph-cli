# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals
# pylint: disable=bad-continuation
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType
from azext_files.generated._client_factory import (
    cf_drive_drive,
    cf_drive,
    cf_drive_list,
    cf_drive_list_content_type,
    cf_drive_list_item,
    cf_drive_list_item_version,
    cf_group,
    cf_share_shared_drive_item,
    cf_share,
    cf_share_list,
    cf_share_list_content_type,
    cf_share_list_item,
    cf_share_list_item_version,
    cf_share_list_item,
    cf_share_list_item_version,
    cf_share_permission,
    cf_user,
)


files_drive_drive = CliCommandType(
    operations_tmpl='azext_files.vendored_sdks.files.operations._drives_drive_operations#DrivesDriveOperations.{}',
    client_factory=cf_drive_drive,
)


files_drive = CliCommandType(
    operations_tmpl='azext_files.vendored_sdks.files.operations._drives_operations#DrivesOperations.{}',
    client_factory=cf_drive,
)


files_drive_list = CliCommandType(
    operations_tmpl='azext_files.vendored_sdks.files.operations._drives_list_operations#DrivesListOperations.{}',
    client_factory=cf_drive_list,
)


files_drive_list_content_type = CliCommandType(
    operations_tmpl='azext_files.vendored_sdks.files.operations._drives_list_content_types_operations#DrivesListContentTypesOperations.{}',
    client_factory=cf_drive_list_content_type,
)


files_drive_list_item = CliCommandType(
    operations_tmpl=(
        'azext_files.vendored_sdks.files.operations._drives_list_items_operations#DrivesListItemsOperations.{}'
    ),
    client_factory=cf_drive_list_item,
)


files_drive_list_item_version = CliCommandType(
    operations_tmpl='azext_files.vendored_sdks.files.operations._drives_list_items_versions_operations#DrivesListItemsVersionsOperations.{}',
    client_factory=cf_drive_list_item_version,
)


files_group = CliCommandType(
    operations_tmpl='azext_files.vendored_sdks.files.operations._groups_operations#GroupsOperations.{}',
    client_factory=cf_group,
)


files_share_shared_drive_item = CliCommandType(
    operations_tmpl='azext_files.vendored_sdks.files.operations._shares_shared_drive_item_operations#SharesSharedDriveItemOperations.{}',
    client_factory=cf_share_shared_drive_item,
)


files_share = CliCommandType(
    operations_tmpl='azext_files.vendored_sdks.files.operations._shares_operations#SharesOperations.{}',
    client_factory=cf_share,
)


files_share_list = CliCommandType(
    operations_tmpl='azext_files.vendored_sdks.files.operations._shares_list_operations#SharesListOperations.{}',
    client_factory=cf_share_list,
)


files_share_list_content_type = CliCommandType(
    operations_tmpl='azext_files.vendored_sdks.files.operations._shares_list_content_types_operations#SharesListContentTypesOperations.{}',
    client_factory=cf_share_list_content_type,
)


files_share_list_item = CliCommandType(
    operations_tmpl=(
        'azext_files.vendored_sdks.files.operations._shares_list_items_operations#SharesListItemsOperations.{}'
    ),
    client_factory=cf_share_list_item,
)


files_share_list_item_version = CliCommandType(
    operations_tmpl='azext_files.vendored_sdks.files.operations._shares_list_items_versions_operations#SharesListItemsVersionsOperations.{}',
    client_factory=cf_share_list_item_version,
)


files_share_list_item = CliCommandType(
    operations_tmpl=(
        'azext_files.vendored_sdks.files.operations._shares_list_item_operations#SharesListItemOperations.{}'
    ),
    client_factory=cf_share_list_item,
)


files_share_list_item_version = CliCommandType(
    operations_tmpl='azext_files.vendored_sdks.files.operations._shares_list_item_versions_operations#SharesListItemVersionsOperations.{}',
    client_factory=cf_share_list_item_version,
)


files_share_permission = CliCommandType(
    operations_tmpl=(
        'azext_files.vendored_sdks.files.operations._shares_permission_operations#SharesPermissionOperations.{}'
    ),
    client_factory=cf_share_permission,
)


files_user = CliCommandType(
    operations_tmpl='azext_files.vendored_sdks.files.operations._users_operations#UsersOperations.{}',
    client_factory=cf_user,
)


def load_command_table(self, _):

    with self.command_group('files drive-drive', files_drive_drive, client_factory=cf_drive_drive) as g:
        g.custom_command('create-drive', 'files_drive_drive_create_drive')
        g.custom_command('delete-drive', 'files_drive_drive_delete_drive')
        g.custom_command('list-drive', 'files_drive_drive_list_drive')
        g.custom_command('show-drive', 'files_drive_drive_show_drive')
        g.custom_command('update-drive', 'files_drive_drive_update_drive')

    with self.command_group('files drive', files_drive, client_factory=cf_drive) as g:
        g.custom_command('create-following', 'files_drive_create_following')
        g.custom_command('create-item', 'files_drive_create_item')
        g.custom_command('create-special', 'files_drive_create_special')
        g.custom_command('delete-following', 'files_drive_delete_following')
        g.custom_command('delete-item', 'files_drive_delete_item')
        g.custom_command('delete-list', 'files_drive_delete_list')
        g.custom_command('delete-root', 'files_drive_delete_root')
        g.custom_command('delete-special', 'files_drive_delete_special')
        g.custom_command('list-following', 'files_drive_list_following')
        g.custom_command('list-item', 'files_drive_list_item')
        g.custom_command('list-special', 'files_drive_list_special')
        g.custom_command('recent', 'files_drive_recent')
        g.custom_command('search', 'files_drive_search')
        g.custom_command('shared-with-me', 'files_drive_shared_with_me')
        g.custom_command('show-following', 'files_drive_show_following')
        g.custom_command('show-item', 'files_drive_show_item')
        g.custom_command('show-list', 'files_drive_show_list')
        g.custom_command('show-root', 'files_drive_show_root')
        g.custom_command('show-special', 'files_drive_show_special')
        g.custom_command('update-following', 'files_drive_update_following')
        g.custom_command('update-item', 'files_drive_update_item')
        g.custom_command('update-list', 'files_drive_update_list')
        g.custom_command('update-root', 'files_drive_update_root')
        g.custom_command('update-special', 'files_drive_update_special')

    with self.command_group('files drive-list', files_drive_list, client_factory=cf_drive_list) as g:
        g.custom_command('create-column', 'files_drive_list_create_column')
        g.custom_command('create-content-type', 'files_drive_list_create_content_type')
        g.custom_command('create-item', 'files_drive_list_create_item')
        g.custom_command('create-subscription', 'files_drive_list_create_subscription')
        g.custom_command('delete-column', 'files_drive_list_delete_column')
        g.custom_command('delete-content-type', 'files_drive_list_delete_content_type')
        g.custom_command('delete-drive', 'files_drive_list_delete_drive')
        g.custom_command('delete-item', 'files_drive_list_delete_item')
        g.custom_command('delete-subscription', 'files_drive_list_delete_subscription')
        g.custom_command('list-column', 'files_drive_list_list_column')
        g.custom_command('list-content-type', 'files_drive_list_list_content_type')
        g.custom_command('list-item', 'files_drive_list_list_item')
        g.custom_command('list-subscription', 'files_drive_list_list_subscription')
        g.custom_command('show-column', 'files_drive_list_show_column')
        g.custom_command('show-content-type', 'files_drive_list_show_content_type')
        g.custom_command('show-drive', 'files_drive_list_show_drive')
        g.custom_command('show-item', 'files_drive_list_show_item')
        g.custom_command('show-subscription', 'files_drive_list_show_subscription')
        g.custom_command('update-column', 'files_drive_list_update_column')
        g.custom_command('update-content-type', 'files_drive_list_update_content_type')
        g.custom_command('update-drive', 'files_drive_list_update_drive')
        g.custom_command('update-item', 'files_drive_list_update_item')
        g.custom_command('update-subscription', 'files_drive_list_update_subscription')

    with self.command_group(
        'files drive-list-content-type', files_drive_list_content_type, client_factory=cf_drive_list_content_type
    ) as g:
        g.custom_command('create-column-link', 'files_drive_list_content_type_create_column_link')
        g.custom_command('delete-column-link', 'files_drive_list_content_type_delete_column_link')
        g.custom_command('list-column-link', 'files_drive_list_content_type_list_column_link')
        g.custom_command('show-column-link', 'files_drive_list_content_type_show_column_link')
        g.custom_command('update-column-link', 'files_drive_list_content_type_update_column_link')

    with self.command_group('files drive-list-item', files_drive_list_item, client_factory=cf_drive_list_item) as g:
        g.custom_command('create-version', 'files_drive_list_item_create_version')
        g.custom_command('delete-drive-item', 'files_drive_list_item_delete_drive_item')
        g.custom_command('delete-field', 'files_drive_list_item_delete_field')
        g.custom_command('delete-ref-analytic', 'files_drive_list_item_delete_ref_analytic')
        g.custom_command('delete-version', 'files_drive_list_item_delete_version')
        g.custom_command('list-version', 'files_drive_list_item_list_version')
        g.custom_command('set-ref-analytic', 'files_drive_list_item_set_ref_analytic')
        g.custom_command('show-activity', 'files_drive_list_item_show_activity')
        g.custom_command('show-analytic', 'files_drive_list_item_show_analytic')
        g.custom_command('show-drive-item', 'files_drive_list_item_show_drive_item')
        g.custom_command('show-field', 'files_drive_list_item_show_field')
        g.custom_command('show-ref-analytic', 'files_drive_list_item_show_ref_analytic')
        g.custom_command('show-version', 'files_drive_list_item_show_version')
        g.custom_command('update-drive-item', 'files_drive_list_item_update_drive_item')
        g.custom_command('update-field', 'files_drive_list_item_update_field')
        g.custom_command('update-version', 'files_drive_list_item_update_version')

    with self.command_group(
        'files drive-list-item-version', files_drive_list_item_version, client_factory=cf_drive_list_item_version
    ) as g:
        g.custom_command('delete-field', 'files_drive_list_item_version_delete_field')
        g.custom_command('restore-version', 'files_drive_list_item_version_restore_version')
        g.custom_command('show-field', 'files_drive_list_item_version_show_field')
        g.custom_command('update-field', 'files_drive_list_item_version_update_field')

    with self.command_group('files group', files_group, client_factory=cf_group) as g:
        g.custom_command('create-drive', 'files_group_create_drive')
        g.custom_command('delete-drive', 'files_group_delete_drive')
        g.custom_command('list-drive', 'files_group_list_drive')
        g.custom_command('show-drive', 'files_group_show_drive')
        g.custom_command('update-drive', 'files_group_update_drive')

    with self.command_group(
        'files share-shared-drive-item', files_share_shared_drive_item, client_factory=cf_share_shared_drive_item
    ) as g:
        g.custom_command('create-shared-drive-item', 'files_share_shared_drive_item_create_shared_drive_item')
        g.custom_command('delete-shared-drive-item', 'files_share_shared_drive_item_delete_shared_drive_item')
        g.custom_command('list-shared-drive-item', 'files_share_shared_drive_item_list_shared_drive_item')
        g.custom_command('show-shared-drive-item', 'files_share_shared_drive_item_show_shared_drive_item')
        g.custom_command('update-shared-drive-item', 'files_share_shared_drive_item_update_shared_drive_item')

    with self.command_group('files share', files_share, client_factory=cf_share) as g:
        g.custom_command('create-item', 'files_share_create_item')
        g.custom_command('delete-drive-item', 'files_share_delete_drive_item')
        g.custom_command('delete-item', 'files_share_delete_item')
        g.custom_command('delete-list', 'files_share_delete_list')
        g.custom_command('delete-list-item', 'files_share_delete_list_item')
        g.custom_command('delete-permission', 'files_share_delete_permission')
        g.custom_command('delete-root', 'files_share_delete_root')
        g.custom_command('delete-site', 'files_share_delete_site')
        g.custom_command('list-item', 'files_share_list_item')
        g.custom_command('show-drive-item', 'files_share_show_drive_item')
        g.custom_command('show-item', 'files_share_show_item')
        g.custom_command('show-list', 'files_share_show_list')
        g.custom_command('show-list-item', 'files_share_show_list_item')
        g.custom_command('show-permission', 'files_share_show_permission')
        g.custom_command('show-root', 'files_share_show_root')
        g.custom_command('show-site', 'files_share_show_site')
        g.custom_command('update-drive-item', 'files_share_update_drive_item')
        g.custom_command('update-item', 'files_share_update_item')
        g.custom_command('update-list', 'files_share_update_list')
        g.custom_command('update-list-item', 'files_share_update_list_item')
        g.custom_command('update-permission', 'files_share_update_permission')
        g.custom_command('update-root', 'files_share_update_root')
        g.custom_command('update-site', 'files_share_update_site')

    with self.command_group('files share-list', files_share_list, client_factory=cf_share_list) as g:
        g.custom_command('create-column', 'files_share_list_create_column')
        g.custom_command('create-content-type', 'files_share_list_create_content_type')
        g.custom_command('create-item', 'files_share_list_create_item')
        g.custom_command('create-subscription', 'files_share_list_create_subscription')
        g.custom_command('delete-column', 'files_share_list_delete_column')
        g.custom_command('delete-content-type', 'files_share_list_delete_content_type')
        g.custom_command('delete-drive', 'files_share_list_delete_drive')
        g.custom_command('delete-item', 'files_share_list_delete_item')
        g.custom_command('delete-subscription', 'files_share_list_delete_subscription')
        g.custom_command('list-column', 'files_share_list_list_column')
        g.custom_command('list-content-type', 'files_share_list_list_content_type')
        g.custom_command('list-item', 'files_share_list_list_item')
        g.custom_command('list-subscription', 'files_share_list_list_subscription')
        g.custom_command('show-column', 'files_share_list_show_column')
        g.custom_command('show-content-type', 'files_share_list_show_content_type')
        g.custom_command('show-drive', 'files_share_list_show_drive')
        g.custom_command('show-item', 'files_share_list_show_item')
        g.custom_command('show-subscription', 'files_share_list_show_subscription')
        g.custom_command('update-column', 'files_share_list_update_column')
        g.custom_command('update-content-type', 'files_share_list_update_content_type')
        g.custom_command('update-drive', 'files_share_list_update_drive')
        g.custom_command('update-item', 'files_share_list_update_item')
        g.custom_command('update-subscription', 'files_share_list_update_subscription')

    with self.command_group(
        'files share-list-content-type', files_share_list_content_type, client_factory=cf_share_list_content_type
    ) as g:
        g.custom_command('create-column-link', 'files_share_list_content_type_create_column_link')
        g.custom_command('delete-column-link', 'files_share_list_content_type_delete_column_link')
        g.custom_command('list-column-link', 'files_share_list_content_type_list_column_link')
        g.custom_command('show-column-link', 'files_share_list_content_type_show_column_link')
        g.custom_command('update-column-link', 'files_share_list_content_type_update_column_link')

    with self.command_group('files share-list-item', files_share_list_item, client_factory=cf_share_list_item) as g:
        g.custom_command('create-version', 'files_share_list_item_create_version')
        g.custom_command('delete-drive-item', 'files_share_list_item_delete_drive_item')
        g.custom_command('delete-field', 'files_share_list_item_delete_field')
        g.custom_command('delete-ref-analytic', 'files_share_list_item_delete_ref_analytic')
        g.custom_command('delete-version', 'files_share_list_item_delete_version')
        g.custom_command('list-version', 'files_share_list_item_list_version')
        g.custom_command('set-ref-analytic', 'files_share_list_item_set_ref_analytic')
        g.custom_command('show-activity', 'files_share_list_item_show_activity')
        g.custom_command('show-analytic', 'files_share_list_item_show_analytic')
        g.custom_command('show-drive-item', 'files_share_list_item_show_drive_item')
        g.custom_command('show-field', 'files_share_list_item_show_field')
        g.custom_command('show-ref-analytic', 'files_share_list_item_show_ref_analytic')
        g.custom_command('show-version', 'files_share_list_item_show_version')
        g.custom_command('update-drive-item', 'files_share_list_item_update_drive_item')
        g.custom_command('update-field', 'files_share_list_item_update_field')
        g.custom_command('update-version', 'files_share_list_item_update_version')

    with self.command_group(
        'files share-list-item-version', files_share_list_item_version, client_factory=cf_share_list_item_version
    ) as g:
        g.custom_command('delete-field', 'files_share_list_item_version_delete_field')
        g.custom_command('restore-version', 'files_share_list_item_version_restore_version')
        g.custom_command('show-field', 'files_share_list_item_version_show_field')
        g.custom_command('update-field', 'files_share_list_item_version_update_field')

    with self.command_group('files share-list-item', files_share_list_item, client_factory=cf_share_list_item) as g:
        g.custom_command('create-version', 'files_share_list_item_create_version')
        g.custom_command('delete-drive-item', 'files_share_list_item_delete_drive_item')
        g.custom_command('delete-field', 'files_share_list_item_delete_field')
        g.custom_command('delete-ref-analytic', 'files_share_list_item_delete_ref_analytic')
        g.custom_command('delete-version', 'files_share_list_item_delete_version')
        g.custom_command('list-version', 'files_share_list_item_list_version')
        g.custom_command('set-ref-analytic', 'files_share_list_item_set_ref_analytic')
        g.custom_command('show-activity', 'files_share_list_item_show_activity')
        g.custom_command('show-analytic', 'files_share_list_item_show_analytic')
        g.custom_command('show-drive-item', 'files_share_list_item_show_drive_item')
        g.custom_command('show-field', 'files_share_list_item_show_field')
        g.custom_command('show-ref-analytic', 'files_share_list_item_show_ref_analytic')
        g.custom_command('show-version', 'files_share_list_item_show_version')
        g.custom_command('update-drive-item', 'files_share_list_item_update_drive_item')
        g.custom_command('update-field', 'files_share_list_item_update_field')
        g.custom_command('update-version', 'files_share_list_item_update_version')

    with self.command_group(
        'files share-list-item-version', files_share_list_item_version, client_factory=cf_share_list_item_version
    ) as g:
        g.custom_command('delete-field', 'files_share_list_item_version_delete_field')
        g.custom_command('restore-version', 'files_share_list_item_version_restore_version')
        g.custom_command('show-field', 'files_share_list_item_version_show_field')
        g.custom_command('update-field', 'files_share_list_item_version_update_field')

    with self.command_group('files share-permission', files_share_permission, client_factory=cf_share_permission) as g:
        g.custom_command('grant', 'files_share_permission_grant')

    with self.command_group('files user', files_user, client_factory=cf_user) as g:
        g.custom_command('create-drive', 'files_user_create_drive')
        g.custom_command('delete-drive', 'files_user_delete_drive')
        g.custom_command('list-drive', 'files_user_list_drive')
        g.custom_command('show-drive', 'files_user_show_drive')
        g.custom_command('update-drive', 'files_user_update_drive')

    with self.command_group('files', is_experimental=True):
        pass
