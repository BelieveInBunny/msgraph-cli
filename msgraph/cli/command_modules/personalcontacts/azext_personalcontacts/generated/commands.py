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
from azext_personalcontacts.generated._client_factory import (
    cf_user,
    cf_user_contact_folder,
    cf_user_contact_folder_contact,
    cf_user_contact,
)


personalcontacts_user = CliCommandType(
    operations_tmpl=(
        'azext_personalcontacts.vendored_sdks.personalcontacts.operations._users_operations#UsersOperations.{}'
    ),
    client_factory=cf_user,
)


personalcontacts_user_contact_folder = CliCommandType(
    operations_tmpl='azext_personalcontacts.vendored_sdks.personalcontacts.operations._users_contact_folders_operations#UsersContactFoldersOperations.{}',
    client_factory=cf_user_contact_folder,
)


personalcontacts_user_contact_folder_contact = CliCommandType(
    operations_tmpl='azext_personalcontacts.vendored_sdks.personalcontacts.operations._users_contact_folders_contacts_operations#UsersContactFoldersContactsOperations.{}',
    client_factory=cf_user_contact_folder_contact,
)


personalcontacts_user_contact = CliCommandType(
    operations_tmpl='azext_personalcontacts.vendored_sdks.personalcontacts.operations._users_contacts_operations#UsersContactsOperations.{}',
    client_factory=cf_user_contact,
)


def load_command_table(self, _):

    with self.command_group('personalcontacts user', personalcontacts_user, client_factory=cf_user) as g:
        g.custom_command('create-contact', 'personalcontacts_user_create_contact')
        g.custom_command('create-contact-folder', 'personalcontacts_user_create_contact_folder')
        g.custom_command('delete-contact', 'personalcontacts_user_delete_contact')
        g.custom_command('delete-contact-folder', 'personalcontacts_user_delete_contact_folder')
        g.custom_command('list-contact', 'personalcontacts_user_list_contact')
        g.custom_command('list-contact-folder', 'personalcontacts_user_list_contact_folder')
        g.custom_command('show-contact', 'personalcontacts_user_show_contact')
        g.custom_command('show-contact-folder', 'personalcontacts_user_show_contact_folder')
        g.custom_command('update-contact', 'personalcontacts_user_update_contact')
        g.custom_command('update-contact-folder', 'personalcontacts_user_update_contact_folder')

    with self.command_group(
        'personalcontacts user-contact-folder',
        personalcontacts_user_contact_folder,
        client_factory=cf_user_contact_folder,
    ) as g:
        g.custom_command('create-child-folder', 'personalcontacts_user_contact_folder_create_child_folder')
        g.custom_command('create-contact', 'personalcontacts_user_contact_folder_create_contact')
        g.custom_command(
            'create-multi-value-extended-property',
            'personalcontacts_user_contact_folder_create_multi_value_extended_property',
        )
        g.custom_command(
            'create-single-value-extended-property',
            'personalcontacts_user_contact_folder_create_single_value_extended_property',
        )
        g.custom_command('delete-child-folder', 'personalcontacts_user_contact_folder_delete_child_folder')
        g.custom_command('delete-contact', 'personalcontacts_user_contact_folder_delete_contact')
        g.custom_command(
            'delete-multi-value-extended-property',
            'personalcontacts_user_contact_folder_delete_multi_value_extended_property',
        )
        g.custom_command(
            'delete-single-value-extended-property',
            'personalcontacts_user_contact_folder_delete_single_value_extended_property',
        )
        g.custom_command('list-child-folder', 'personalcontacts_user_contact_folder_list_child_folder')
        g.custom_command('list-contact', 'personalcontacts_user_contact_folder_list_contact')
        g.custom_command(
            'list-multi-value-extended-property',
            'personalcontacts_user_contact_folder_list_multi_value_extended_property',
        )
        g.custom_command(
            'list-single-value-extended-property',
            'personalcontacts_user_contact_folder_list_single_value_extended_property',
        )
        g.custom_command('show-child-folder', 'personalcontacts_user_contact_folder_show_child_folder')
        g.custom_command('show-contact', 'personalcontacts_user_contact_folder_show_contact')
        g.custom_command(
            'show-multi-value-extended-property',
            'personalcontacts_user_contact_folder_show_multi_value_extended_property',
        )
        g.custom_command(
            'show-single-value-extended-property',
            'personalcontacts_user_contact_folder_show_single_value_extended_property',
        )
        g.custom_command('update-child-folder', 'personalcontacts_user_contact_folder_update_child_folder')
        g.custom_command('update-contact', 'personalcontacts_user_contact_folder_update_contact')
        g.custom_command(
            'update-multi-value-extended-property',
            'personalcontacts_user_contact_folder_update_multi_value_extended_property',
        )
        g.custom_command(
            'update-single-value-extended-property',
            'personalcontacts_user_contact_folder_update_single_value_extended_property',
        )

    with self.command_group(
        'personalcontacts user-contact-folder-contact',
        personalcontacts_user_contact_folder_contact,
        client_factory=cf_user_contact_folder_contact,
    ) as g:
        g.custom_command('create-extension', 'personalcontacts_user_contact_folder_contact_create_extension')
        g.custom_command(
            'create-multi-value-extended-property',
            'personalcontacts_user_contact_folder_contact_create_multi_value_extended_property',
        )
        g.custom_command(
            'create-single-value-extended-property',
            'personalcontacts_user_contact_folder_contact_create_single_value_extended_property',
        )
        g.custom_command('delete-extension', 'personalcontacts_user_contact_folder_contact_delete_extension')
        g.custom_command(
            'delete-multi-value-extended-property',
            'personalcontacts_user_contact_folder_contact_delete_multi_value_extended_property',
        )
        g.custom_command('delete-photo', 'personalcontacts_user_contact_folder_contact_delete_photo')
        g.custom_command(
            'delete-single-value-extended-property',
            'personalcontacts_user_contact_folder_contact_delete_single_value_extended_property',
        )
        g.custom_command('list-extension', 'personalcontacts_user_contact_folder_contact_list_extension')
        g.custom_command(
            'list-multi-value-extended-property',
            'personalcontacts_user_contact_folder_contact_list_multi_value_extended_property',
        )
        g.custom_command(
            'list-single-value-extended-property',
            'personalcontacts_user_contact_folder_contact_list_single_value_extended_property',
        )
        g.custom_command('show-extension', 'personalcontacts_user_contact_folder_contact_show_extension')
        g.custom_command(
            'show-multi-value-extended-property',
            'personalcontacts_user_contact_folder_contact_show_multi_value_extended_property',
        )
        g.custom_command('show-photo', 'personalcontacts_user_contact_folder_contact_show_photo')
        g.custom_command(
            'show-single-value-extended-property',
            'personalcontacts_user_contact_folder_contact_show_single_value_extended_property',
        )
        g.custom_command('update-extension', 'personalcontacts_user_contact_folder_contact_update_extension')
        g.custom_command(
            'update-multi-value-extended-property',
            'personalcontacts_user_contact_folder_contact_update_multi_value_extended_property',
        )
        g.custom_command('update-photo', 'personalcontacts_user_contact_folder_contact_update_photo')
        g.custom_command(
            'update-single-value-extended-property',
            'personalcontacts_user_contact_folder_contact_update_single_value_extended_property',
        )

    with self.command_group(
        'personalcontacts user-contact', personalcontacts_user_contact, client_factory=cf_user_contact
    ) as g:
        g.custom_command('create-extension', 'personalcontacts_user_contact_create_extension')
        g.custom_command(
            'create-multi-value-extended-property', 'personalcontacts_user_contact_create_multi_value_extended_property'
        )
        g.custom_command(
            'create-single-value-extended-property',
            'personalcontacts_user_contact_create_single_value_extended_property',
        )
        g.custom_command('delete-extension', 'personalcontacts_user_contact_delete_extension')
        g.custom_command(
            'delete-multi-value-extended-property', 'personalcontacts_user_contact_delete_multi_value_extended_property'
        )
        g.custom_command('delete-photo', 'personalcontacts_user_contact_delete_photo')
        g.custom_command(
            'delete-single-value-extended-property',
            'personalcontacts_user_contact_delete_single_value_extended_property',
        )
        g.custom_command('list-extension', 'personalcontacts_user_contact_list_extension')
        g.custom_command(
            'list-multi-value-extended-property', 'personalcontacts_user_contact_list_multi_value_extended_property'
        )
        g.custom_command(
            'list-single-value-extended-property', 'personalcontacts_user_contact_list_single_value_extended_property'
        )
        g.custom_command('show-extension', 'personalcontacts_user_contact_show_extension')
        g.custom_command(
            'show-multi-value-extended-property', 'personalcontacts_user_contact_show_multi_value_extended_property'
        )
        g.custom_command('show-photo', 'personalcontacts_user_contact_show_photo')
        g.custom_command(
            'show-single-value-extended-property', 'personalcontacts_user_contact_show_single_value_extended_property'
        )
        g.custom_command('update-extension', 'personalcontacts_user_contact_update_extension')
        g.custom_command(
            'update-multi-value-extended-property', 'personalcontacts_user_contact_update_multi_value_extended_property'
        )
        g.custom_command('update-photo', 'personalcontacts_user_contact_update_photo')
        g.custom_command(
            'update-single-value-extended-property',
            'personalcontacts_user_contact_update_single_value_extended_property',
        )

    with self.command_group('personalcontacts', is_experimental=True):
        pass
