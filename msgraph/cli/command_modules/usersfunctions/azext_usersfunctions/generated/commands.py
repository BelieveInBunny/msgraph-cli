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
from azext_usersfunctions.generated._client_factory import (
    cf_usersactivity,
    cf_userscalendarviewcalendar,
    cf_userscalendarviewinstance,
    cf_userscalendarview,
    cf_userscalendareventscalendar,
    cf_userscalendareventsinstance,
    cf_userscalendarevent,
    cf_userscalendar,
    cf_userscalendargroupscalendarscalendarviewcalendar,
    cf_userscalendargroupscalendarscalendarviewinstance,
    cf_userscalendargroupscalendarscalendarview,
    cf_userscalendargroupscalendarseventscalendar,
    cf_userscalendargroupscalendarseventsinstance,
    cf_userscalendargroupscalendarsevent,
    cf_userscalendargroupscalendar,
    cf_userscalendarscalendarviewcalendar,
    cf_userscalendarscalendarviewinstance,
    cf_userscalendarscalendarview,
    cf_userscalendarseventscalendar,
    cf_userscalendarseventsinstance,
    cf_userscalendarsevent,
    cf_userscalendar,
    cf_userscalendarviewcalendarview,
    cf_userscalendarviewcalendarevent,
    cf_userscalendarviewcalendar,
    cf_userscalendarviewinstance,
    cf_userscalendarview,
    cf_userscontactfolderschildfolder,
    cf_userscontactfolderscontact,
    cf_userscontactfolder,
    cf_userscontact,
    cf_userseventscalendarview,
    cf_userseventscalendarevent,
    cf_userseventscalendar,
    cf_userseventsinstance,
    cf_usersevent,
    cf_usersmailfolderschildfolder,
    cf_usersmailfoldersmessage,
    cf_usersmailfolder,
    cf_usersmanagedappregistration,
    cf_usersmessage,
    cf_user,
    cf_usersonenotenotebookssectiongroupssectionspage,
    cf_usersonenotenotebookssectionspage,
    cf_usersonenotenotebook,
    cf_usersonenotepage,
    cf_usersonenotepagesparentnotebooksectiongroupssectionspage,
    cf_usersonenotepagesparentnotebooksectionspage,
    cf_usersonenotepagesparentsectionpage,
    cf_usersonenotesectiongroupsparentnotebooksectionspage,
    cf_usersonenotesectiongroupssectionspage,
    cf_usersonenotesectionspage,
    cf_usersoutlook,
)


usersfunctions_user = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._users_operations#usersOperations.{}',
    client_factory=cf_user,
)


usersfunctions_usersactivity = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._usersactivities_operations#usersactivitiesOperations.{}',
    client_factory=cf_usersactivity,
)


usersfunctions_userscalendar = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendar_operations#userscalendarOperations.{}',
    client_factory=cf_userscalendar,
)


usersfunctions_userscalendar = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendars_operations#userscalendarsOperations.{}',
    client_factory=cf_userscalendar,
)


usersfunctions_userscalendarevent = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendarevents_operations#userscalendareventsOperations.{}',
    client_factory=cf_userscalendarevent,
)


usersfunctions_userscalendareventscalendar = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendareventscalendar_operations#userscalendareventscalendarOperations.{}',
    client_factory=cf_userscalendareventscalendar,
)


usersfunctions_userscalendareventsinstance = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendareventsinstances_operations#userscalendareventsinstancesOperations.{}',
    client_factory=cf_userscalendareventsinstance,
)


usersfunctions_userscalendargroupscalendar = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendargroupscalendars_operations#userscalendargroupscalendarsOperations.{}',
    client_factory=cf_userscalendargroupscalendar,
)


usersfunctions_userscalendargroupscalendarscalendarview = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendargroupscalendarscalendarview_operations#userscalendargroupscalendarscalendarviewOperations.{}',
    client_factory=cf_userscalendargroupscalendarscalendarview,
)


usersfunctions_userscalendargroupscalendarscalendarviewcalendar = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendargroupscalendarscalendarviewcalendar_operations#userscalendargroupscalendarscalendarviewcalendarOperations.{}',
    client_factory=cf_userscalendargroupscalendarscalendarviewcalendar,
)


usersfunctions_userscalendargroupscalendarscalendarviewinstance = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendargroupscalendarscalendarviewinstances_operations#userscalendargroupscalendarscalendarviewinstancesOperations.{}',
    client_factory=cf_userscalendargroupscalendarscalendarviewinstance,
)


usersfunctions_userscalendargroupscalendarsevent = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendargroupscalendarsevents_operations#userscalendargroupscalendarseventsOperations.{}',
    client_factory=cf_userscalendargroupscalendarsevent,
)


usersfunctions_userscalendargroupscalendarseventscalendar = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendargroupscalendarseventscalendar_operations#userscalendargroupscalendarseventscalendarOperations.{}',
    client_factory=cf_userscalendargroupscalendarseventscalendar,
)


usersfunctions_userscalendargroupscalendarseventsinstance = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendargroupscalendarseventsinstances_operations#userscalendargroupscalendarseventsinstancesOperations.{}',
    client_factory=cf_userscalendargroupscalendarseventsinstance,
)


usersfunctions_userscalendarscalendarview = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendarscalendarview_operations#userscalendarscalendarviewOperations.{}',
    client_factory=cf_userscalendarscalendarview,
)


usersfunctions_userscalendarscalendarviewcalendar = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendarscalendarviewcalendar_operations#userscalendarscalendarviewcalendarOperations.{}',
    client_factory=cf_userscalendarscalendarviewcalendar,
)


usersfunctions_userscalendarscalendarviewinstance = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendarscalendarviewinstances_operations#userscalendarscalendarviewinstancesOperations.{}',
    client_factory=cf_userscalendarscalendarviewinstance,
)


usersfunctions_userscalendarsevent = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendarsevents_operations#userscalendarseventsOperations.{}',
    client_factory=cf_userscalendarsevent,
)


usersfunctions_userscalendarseventscalendar = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendarseventscalendar_operations#userscalendarseventscalendarOperations.{}',
    client_factory=cf_userscalendarseventscalendar,
)


usersfunctions_userscalendarseventsinstance = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendarseventsinstances_operations#userscalendarseventsinstancesOperations.{}',
    client_factory=cf_userscalendarseventsinstance,
)


usersfunctions_userscalendarview = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendarcalendarview_operations#userscalendarcalendarviewOperations.{}',
    client_factory=cf_userscalendarview,
)


usersfunctions_userscalendarview = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendarview_operations#userscalendarviewOperations.{}',
    client_factory=cf_userscalendarview,
)


usersfunctions_userscalendarviewcalendar = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendarcalendarviewcalendar_operations#userscalendarcalendarviewcalendarOperations.{}',
    client_factory=cf_userscalendarviewcalendar,
)


usersfunctions_userscalendarviewcalendar = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendarviewcalendar_operations#userscalendarviewcalendarOperations.{}',
    client_factory=cf_userscalendarviewcalendar,
)


usersfunctions_userscalendarviewcalendarevent = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendarviewcalendarevents_operations#userscalendarviewcalendareventsOperations.{}',
    client_factory=cf_userscalendarviewcalendarevent,
)


usersfunctions_userscalendarviewcalendarview = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendarviewcalendarcalendarview_operations#userscalendarviewcalendarcalendarviewOperations.{}',
    client_factory=cf_userscalendarviewcalendarview,
)


usersfunctions_userscalendarviewinstance = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendarcalendarviewinstances_operations#userscalendarcalendarviewinstancesOperations.{}',
    client_factory=cf_userscalendarviewinstance,
)


usersfunctions_userscalendarviewinstance = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscalendarviewinstances_operations#userscalendarviewinstancesOperations.{}',
    client_factory=cf_userscalendarviewinstance,
)


usersfunctions_userscontact = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscontacts_operations#userscontactsOperations.{}',
    client_factory=cf_userscontact,
)


usersfunctions_userscontactfolder = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscontactfolders_operations#userscontactfoldersOperations.{}',
    client_factory=cf_userscontactfolder,
)


usersfunctions_userscontactfolderschildfolder = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscontactfolderschildfolders_operations#userscontactfolderschildfoldersOperations.{}',
    client_factory=cf_userscontactfolderschildfolder,
)


usersfunctions_userscontactfolderscontact = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userscontactfolderscontacts_operations#userscontactfolderscontactsOperations.{}',
    client_factory=cf_userscontactfolderscontact,
)


usersfunctions_usersevent = CliCommandType(
    operations_tmpl=(
        'azext_usersfunctions.vendored_sdks.usersfunctions.operations._usersevents_operations#userseventsOperations.{}'
    ),
    client_factory=cf_usersevent,
)


usersfunctions_userseventscalendar = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userseventscalendar_operations#userseventscalendarOperations.{}',
    client_factory=cf_userseventscalendar,
)


usersfunctions_userseventscalendarevent = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userseventscalendarevents_operations#userseventscalendareventsOperations.{}',
    client_factory=cf_userseventscalendarevent,
)


usersfunctions_userseventscalendarview = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userseventscalendarcalendarview_operations#userseventscalendarcalendarviewOperations.{}',
    client_factory=cf_userseventscalendarview,
)


usersfunctions_userseventsinstance = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._userseventsinstances_operations#userseventsinstancesOperations.{}',
    client_factory=cf_userseventsinstance,
)


usersfunctions_usersmailfolder = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._usersmailfolders_operations#usersmailfoldersOperations.{}',
    client_factory=cf_usersmailfolder,
)


usersfunctions_usersmailfolderschildfolder = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._usersmailfolderschildfolders_operations#usersmailfolderschildfoldersOperations.{}',
    client_factory=cf_usersmailfolderschildfolder,
)


usersfunctions_usersmailfoldersmessage = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._usersmailfoldersmessages_operations#usersmailfoldersmessagesOperations.{}',
    client_factory=cf_usersmailfoldersmessage,
)


usersfunctions_usersmanagedappregistration = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._usersmanagedappregistrations_operations#usersmanagedappregistrationsOperations.{}',
    client_factory=cf_usersmanagedappregistration,
)


usersfunctions_usersmessage = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._usersmessages_operations#usersmessagesOperations.{}',
    client_factory=cf_usersmessage,
)


usersfunctions_usersonenotenotebook = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._usersonenotenotebooks_operations#usersonenotenotebooksOperations.{}',
    client_factory=cf_usersonenotenotebook,
)


usersfunctions_usersonenotenotebookssectiongroupssectionspage = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._usersonenotenotebookssectiongroupssectionspages_operations#usersonenotenotebookssectiongroupssectionspagesOperations.{}',
    client_factory=cf_usersonenotenotebookssectiongroupssectionspage,
)


usersfunctions_usersonenotenotebookssectionspage = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._usersonenotenotebookssectionspages_operations#usersonenotenotebookssectionspagesOperations.{}',
    client_factory=cf_usersonenotenotebookssectionspage,
)


usersfunctions_usersonenotepage = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._usersonenotepages_operations#usersonenotepagesOperations.{}',
    client_factory=cf_usersonenotepage,
)


usersfunctions_usersonenotepagesparentnotebooksectiongroupssectionspage = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._usersonenotepagesparentnotebooksectiongroupssectionspages_operations#usersonenotepagesparentnotebooksectiongroupssectionspagesOperations.{}',
    client_factory=cf_usersonenotepagesparentnotebooksectiongroupssectionspage,
)


usersfunctions_usersonenotepagesparentnotebooksectionspage = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._usersonenotepagesparentnotebooksectionspages_operations#usersonenotepagesparentnotebooksectionspagesOperations.{}',
    client_factory=cf_usersonenotepagesparentnotebooksectionspage,
)


usersfunctions_usersonenotepagesparentsectionpage = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._usersonenotepagesparentsectionpages_operations#usersonenotepagesparentsectionpagesOperations.{}',
    client_factory=cf_usersonenotepagesparentsectionpage,
)


usersfunctions_usersonenotesectiongroupsparentnotebooksectionspage = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._usersonenotesectiongroupsparentnotebooksectionspages_operations#usersonenotesectiongroupsparentnotebooksectionspagesOperations.{}',
    client_factory=cf_usersonenotesectiongroupsparentnotebooksectionspage,
)


usersfunctions_usersonenotesectiongroupssectionspage = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._usersonenotesectiongroupssectionspages_operations#usersonenotesectiongroupssectionspagesOperations.{}',
    client_factory=cf_usersonenotesectiongroupssectionspage,
)


usersfunctions_usersonenotesectionspage = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._usersonenotesectionspages_operations#usersonenotesectionspagesOperations.{}',
    client_factory=cf_usersonenotesectionspage,
)


usersfunctions_usersoutlook = CliCommandType(
    operations_tmpl='azext_usersfunctions.vendored_sdks.usersfunctions.operations._usersoutlook_operations#usersoutlookOperations.{}',
    client_factory=cf_usersoutlook,
)


def load_command_table(self, _):

    with self.command_group('usersfunctions user', usersfunctions_user, client_factory=cf_user) as g:
        g.custom_command('delta', 'usersfunctions_user_delta')
        g.custom_command('reminder-view', 'usersfunctions_user_reminder_view')
        g.custom_command(
            'show-managed-app-diagnostic-statuses', 'usersfunctions_user_show_managed_app_diagnostic_statuses'
        )
        g.custom_command('show-managed-app-policy', 'usersfunctions_user_show_managed_app_policy')

    with self.command_group(
        'usersfunctions usersactivity', usersfunctions_usersactivity, client_factory=cf_usersactivity
    ) as g:
        g.custom_command('recent', 'usersfunctions_usersactivity_recent')

    with self.command_group(
        'usersfunctions userscalendar', usersfunctions_userscalendar, client_factory=cf_userscalendar
    ) as g:
        g.custom_command('allowed-calendar-sharing-role', 'usersfunctions_userscalendar_allowed_calendar_sharing_role')

    with self.command_group(
        'usersfunctions userscalendar', usersfunctions_userscalendar, client_factory=cf_userscalendar
    ) as g:
        g.custom_command('allowed-calendar-sharing-role', 'usersfunctions_userscalendar_allowed_calendar_sharing_role')

    with self.command_group(
        'usersfunctions userscalendarevent', usersfunctions_userscalendarevent, client_factory=cf_userscalendarevent
    ) as g:
        g.custom_command('delta', 'usersfunctions_userscalendarevent_delta')

    with self.command_group(
        'usersfunctions userscalendareventscalendar',
        usersfunctions_userscalendareventscalendar,
        client_factory=cf_userscalendareventscalendar,
    ) as g:
        g.custom_command(
            'allowed-calendar-sharing-role', 'usersfunctions_userscalendareventscalendar_allowed_calendar_sharing_role'
        )

    with self.command_group(
        'usersfunctions userscalendareventsinstance',
        usersfunctions_userscalendareventsinstance,
        client_factory=cf_userscalendareventsinstance,
    ) as g:
        g.custom_command('delta', 'usersfunctions_userscalendareventsinstance_delta')

    with self.command_group(
        'usersfunctions userscalendargroupscalendar',
        usersfunctions_userscalendargroupscalendar,
        client_factory=cf_userscalendargroupscalendar,
    ) as g:
        g.custom_command(
            'allowed-calendar-sharing-role', 'usersfunctions_userscalendargroupscalendar_allowed_calendar_sharing_role'
        )

    with self.command_group(
        'usersfunctions userscalendargroupscalendarscalendarview',
        usersfunctions_userscalendargroupscalendarscalendarview,
        client_factory=cf_userscalendargroupscalendarscalendarview,
    ) as g:
        g.custom_command('delta', 'usersfunctions_userscalendargroupscalendarscalendarview_delta')

    with self.command_group(
        'usersfunctions userscalendargroupscalendarscalendarviewcalendar',
        usersfunctions_userscalendargroupscalendarscalendarviewcalendar,
        client_factory=cf_userscalendargroupscalendarscalendarviewcalendar,
    ) as g:
        g.custom_command(
            'allowed-calendar-sharing-role',
            'usersfunctions_userscalendargroupscalendarscalendarviewcalendar_allowed_calendar_sharing_role',
        )

    with self.command_group(
        'usersfunctions userscalendargroupscalendarscalendarviewinstance',
        usersfunctions_userscalendargroupscalendarscalendarviewinstance,
        client_factory=cf_userscalendargroupscalendarscalendarviewinstance,
    ) as g:
        g.custom_command('delta', 'usersfunctions_userscalendargroupscalendarscalendarviewinstance_delta')

    with self.command_group(
        'usersfunctions userscalendargroupscalendarsevent',
        usersfunctions_userscalendargroupscalendarsevent,
        client_factory=cf_userscalendargroupscalendarsevent,
    ) as g:
        g.custom_command('delta', 'usersfunctions_userscalendargroupscalendarsevent_delta')

    with self.command_group(
        'usersfunctions userscalendargroupscalendarseventscalendar',
        usersfunctions_userscalendargroupscalendarseventscalendar,
        client_factory=cf_userscalendargroupscalendarseventscalendar,
    ) as g:
        g.custom_command(
            'allowed-calendar-sharing-role',
            'usersfunctions_userscalendargroupscalendarseventscalendar_allowed_calendar_sharing_role',
        )

    with self.command_group(
        'usersfunctions userscalendargroupscalendarseventsinstance',
        usersfunctions_userscalendargroupscalendarseventsinstance,
        client_factory=cf_userscalendargroupscalendarseventsinstance,
    ) as g:
        g.custom_command('delta', 'usersfunctions_userscalendargroupscalendarseventsinstance_delta')

    with self.command_group(
        'usersfunctions userscalendarscalendarview',
        usersfunctions_userscalendarscalendarview,
        client_factory=cf_userscalendarscalendarview,
    ) as g:
        g.custom_command('delta', 'usersfunctions_userscalendarscalendarview_delta')

    with self.command_group(
        'usersfunctions userscalendarscalendarviewcalendar',
        usersfunctions_userscalendarscalendarviewcalendar,
        client_factory=cf_userscalendarscalendarviewcalendar,
    ) as g:
        g.custom_command(
            'allowed-calendar-sharing-role',
            'usersfunctions_userscalendarscalendarviewcalendar_allowed_calendar_sharing_role',
        )

    with self.command_group(
        'usersfunctions userscalendarscalendarviewinstance',
        usersfunctions_userscalendarscalendarviewinstance,
        client_factory=cf_userscalendarscalendarviewinstance,
    ) as g:
        g.custom_command('delta', 'usersfunctions_userscalendarscalendarviewinstance_delta')

    with self.command_group(
        'usersfunctions userscalendarsevent', usersfunctions_userscalendarsevent, client_factory=cf_userscalendarsevent
    ) as g:
        g.custom_command('delta', 'usersfunctions_userscalendarsevent_delta')

    with self.command_group(
        'usersfunctions userscalendarseventscalendar',
        usersfunctions_userscalendarseventscalendar,
        client_factory=cf_userscalendarseventscalendar,
    ) as g:
        g.custom_command(
            'allowed-calendar-sharing-role', 'usersfunctions_userscalendarseventscalendar_allowed_calendar_sharing_role'
        )

    with self.command_group(
        'usersfunctions userscalendarseventsinstance',
        usersfunctions_userscalendarseventsinstance,
        client_factory=cf_userscalendarseventsinstance,
    ) as g:
        g.custom_command('delta', 'usersfunctions_userscalendarseventsinstance_delta')

    with self.command_group(
        'usersfunctions userscalendarview', usersfunctions_userscalendarview, client_factory=cf_userscalendarview
    ) as g:
        g.custom_command('delta', 'usersfunctions_userscalendarview_delta')

    with self.command_group(
        'usersfunctions userscalendarview', usersfunctions_userscalendarview, client_factory=cf_userscalendarview
    ) as g:
        g.custom_command('delta', 'usersfunctions_userscalendarview_delta')

    with self.command_group(
        'usersfunctions userscalendarviewcalendar',
        usersfunctions_userscalendarviewcalendar,
        client_factory=cf_userscalendarviewcalendar,
    ) as g:
        g.custom_command(
            'allowed-calendar-sharing-role', 'usersfunctions_userscalendarviewcalendar_allowed_calendar_sharing_role'
        )

    with self.command_group(
        'usersfunctions userscalendarviewcalendar',
        usersfunctions_userscalendarviewcalendar,
        client_factory=cf_userscalendarviewcalendar,
    ) as g:
        g.custom_command(
            'allowed-calendar-sharing-role', 'usersfunctions_userscalendarviewcalendar_allowed_calendar_sharing_role'
        )

    with self.command_group(
        'usersfunctions userscalendarviewcalendarevent',
        usersfunctions_userscalendarviewcalendarevent,
        client_factory=cf_userscalendarviewcalendarevent,
    ) as g:
        g.custom_command('delta', 'usersfunctions_userscalendarviewcalendarevent_delta')

    with self.command_group(
        'usersfunctions userscalendarviewcalendarview',
        usersfunctions_userscalendarviewcalendarview,
        client_factory=cf_userscalendarviewcalendarview,
    ) as g:
        g.custom_command('delta', 'usersfunctions_userscalendarviewcalendarview_delta')

    with self.command_group(
        'usersfunctions userscalendarviewinstance',
        usersfunctions_userscalendarviewinstance,
        client_factory=cf_userscalendarviewinstance,
    ) as g:
        g.custom_command('delta', 'usersfunctions_userscalendarviewinstance_delta')

    with self.command_group(
        'usersfunctions userscalendarviewinstance',
        usersfunctions_userscalendarviewinstance,
        client_factory=cf_userscalendarviewinstance,
    ) as g:
        g.custom_command('delta', 'usersfunctions_userscalendarviewinstance_delta')

    with self.command_group(
        'usersfunctions userscontact', usersfunctions_userscontact, client_factory=cf_userscontact
    ) as g:
        g.custom_command('delta', 'usersfunctions_userscontact_delta')

    with self.command_group(
        'usersfunctions userscontactfolder', usersfunctions_userscontactfolder, client_factory=cf_userscontactfolder
    ) as g:
        g.custom_command('delta', 'usersfunctions_userscontactfolder_delta')

    with self.command_group(
        'usersfunctions userscontactfolderschildfolder',
        usersfunctions_userscontactfolderschildfolder,
        client_factory=cf_userscontactfolderschildfolder,
    ) as g:
        g.custom_command('delta', 'usersfunctions_userscontactfolderschildfolder_delta')

    with self.command_group(
        'usersfunctions userscontactfolderscontact',
        usersfunctions_userscontactfolderscontact,
        client_factory=cf_userscontactfolderscontact,
    ) as g:
        g.custom_command('delta', 'usersfunctions_userscontactfolderscontact_delta')

    with self.command_group('usersfunctions usersevent', usersfunctions_usersevent, client_factory=cf_usersevent) as g:
        g.custom_command('delta', 'usersfunctions_usersevent_delta')

    with self.command_group(
        'usersfunctions userseventscalendar', usersfunctions_userseventscalendar, client_factory=cf_userseventscalendar
    ) as g:
        g.custom_command(
            'allowed-calendar-sharing-role', 'usersfunctions_userseventscalendar_allowed_calendar_sharing_role'
        )

    with self.command_group(
        'usersfunctions userseventscalendarevent',
        usersfunctions_userseventscalendarevent,
        client_factory=cf_userseventscalendarevent,
    ) as g:
        g.custom_command('delta', 'usersfunctions_userseventscalendarevent_delta')

    with self.command_group(
        'usersfunctions userseventscalendarview',
        usersfunctions_userseventscalendarview,
        client_factory=cf_userseventscalendarview,
    ) as g:
        g.custom_command('delta', 'usersfunctions_userseventscalendarview_delta')

    with self.command_group(
        'usersfunctions userseventsinstance', usersfunctions_userseventsinstance, client_factory=cf_userseventsinstance
    ) as g:
        g.custom_command('delta', 'usersfunctions_userseventsinstance_delta')

    with self.command_group(
        'usersfunctions usersmailfolder', usersfunctions_usersmailfolder, client_factory=cf_usersmailfolder
    ) as g:
        g.custom_command('delta', 'usersfunctions_usersmailfolder_delta')

    with self.command_group(
        'usersfunctions usersmailfolderschildfolder',
        usersfunctions_usersmailfolderschildfolder,
        client_factory=cf_usersmailfolderschildfolder,
    ) as g:
        g.custom_command('delta', 'usersfunctions_usersmailfolderschildfolder_delta')

    with self.command_group(
        'usersfunctions usersmailfoldersmessage',
        usersfunctions_usersmailfoldersmessage,
        client_factory=cf_usersmailfoldersmessage,
    ) as g:
        g.custom_command('delta', 'usersfunctions_usersmailfoldersmessage_delta')

    with self.command_group(
        'usersfunctions usersmanagedappregistration',
        usersfunctions_usersmanagedappregistration,
        client_factory=cf_usersmanagedappregistration,
    ) as g:
        g.custom_command(
            'show-user-id-with-flagged-app-registration',
            'usersfunctions_usersmanagedappregistration_show_user_id_with_flagged_app_registration',
        )

    with self.command_group(
        'usersfunctions usersmessage', usersfunctions_usersmessage, client_factory=cf_usersmessage
    ) as g:
        g.custom_command('delta', 'usersfunctions_usersmessage_delta')

    with self.command_group(
        'usersfunctions usersonenotenotebook',
        usersfunctions_usersonenotenotebook,
        client_factory=cf_usersonenotenotebook,
    ) as g:
        g.custom_command('show-recent-notebook', 'usersfunctions_usersonenotenotebook_show_recent_notebook')

    with self.command_group(
        'usersfunctions usersonenotenotebookssectiongroupssectionspage',
        usersfunctions_usersonenotenotebookssectiongroupssectionspage,
        client_factory=cf_usersonenotenotebookssectiongroupssectionspage,
    ) as g:
        g.custom_command('preview', 'usersfunctions_usersonenotenotebookssectiongroupssectionspage_preview')

    with self.command_group(
        'usersfunctions usersonenotenotebookssectionspage',
        usersfunctions_usersonenotenotebookssectionspage,
        client_factory=cf_usersonenotenotebookssectionspage,
    ) as g:
        g.custom_command('preview', 'usersfunctions_usersonenotenotebookssectionspage_preview')

    with self.command_group(
        'usersfunctions usersonenotepage', usersfunctions_usersonenotepage, client_factory=cf_usersonenotepage
    ) as g:
        g.custom_command('preview', 'usersfunctions_usersonenotepage_preview')

    with self.command_group(
        'usersfunctions usersonenotepagesparentnotebooksectiongroupssectionspage',
        usersfunctions_usersonenotepagesparentnotebooksectiongroupssectionspage,
        client_factory=cf_usersonenotepagesparentnotebooksectiongroupssectionspage,
    ) as g:
        g.custom_command('preview', 'usersfunctions_usersonenotepagesparentnotebooksectiongroupssectionspage_preview')

    with self.command_group(
        'usersfunctions usersonenotepagesparentnotebooksectionspage',
        usersfunctions_usersonenotepagesparentnotebooksectionspage,
        client_factory=cf_usersonenotepagesparentnotebooksectionspage,
    ) as g:
        g.custom_command('preview', 'usersfunctions_usersonenotepagesparentnotebooksectionspage_preview')

    with self.command_group(
        'usersfunctions usersonenotepagesparentsectionpage',
        usersfunctions_usersonenotepagesparentsectionpage,
        client_factory=cf_usersonenotepagesparentsectionpage,
    ) as g:
        g.custom_command('preview', 'usersfunctions_usersonenotepagesparentsectionpage_preview')

    with self.command_group(
        'usersfunctions usersonenotesectiongroupsparentnotebooksectionspage',
        usersfunctions_usersonenotesectiongroupsparentnotebooksectionspage,
        client_factory=cf_usersonenotesectiongroupsparentnotebooksectionspage,
    ) as g:
        g.custom_command('preview', 'usersfunctions_usersonenotesectiongroupsparentnotebooksectionspage_preview')

    with self.command_group(
        'usersfunctions usersonenotesectiongroupssectionspage',
        usersfunctions_usersonenotesectiongroupssectionspage,
        client_factory=cf_usersonenotesectiongroupssectionspage,
    ) as g:
        g.custom_command('preview', 'usersfunctions_usersonenotesectiongroupssectionspage_preview')

    with self.command_group(
        'usersfunctions usersonenotesectionspage',
        usersfunctions_usersonenotesectionspage,
        client_factory=cf_usersonenotesectionspage,
    ) as g:
        g.custom_command('preview', 'usersfunctions_usersonenotesectionspage_preview')

    with self.command_group(
        'usersfunctions usersoutlook', usersfunctions_usersoutlook, client_factory=cf_usersoutlook
    ) as g:
        g.custom_command('supported-language', 'usersfunctions_usersoutlook_supported_language')
        g.custom_command('supported-time-zone-ee48', 'usersfunctions_usersoutlook_supported_time_zone_ee48')
        g.custom_command('supported-time-zones51-c6', 'usersfunctions_usersoutlook_supported_time_zones51_c6')

    with self.command_group('usersfunctions', is_experimental=True):
        pass
