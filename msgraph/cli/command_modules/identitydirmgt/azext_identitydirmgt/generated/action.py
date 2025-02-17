# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=protected-access

import argparse
from collections import defaultdict
from knack.util import CLIError


class AddAddresses(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddAddresses, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'city':
                d['city'] = v[0]
            elif kl == 'country-or-region':
                d['country_or_region'] = v[0]
            elif kl == 'office-location':
                d['office_location'] = v[0]
            elif kl == 'postal-code':
                d['postal_code'] = v[0]
            elif kl == 'state':
                d['state'] = v[0]
            elif kl == 'street':
                d['street'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter addresses. All possible keys are: city, '
                               'country-or-region, office-location, postal-code, state, street'.format(k))
        return d


class AddOnPremisesProvisioningErrors(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddOnPremisesProvisioningErrors, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'category':
                d['category'] = v[0]
            elif kl == 'occurred-date-time':
                d['occurred_date_time'] = v[0]
            elif kl == 'property-causing-error':
                d['property_causing_error'] = v[0]
            elif kl == 'value':
                d['value'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter on_premises_provisioning_errors. All '
                               'possible keys are: category, occurred-date-time, property-causing-error, value'.format(k))
        return d


class AddPhones(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddPhones, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'language':
                d['language'] = v[0]
            elif kl == 'number':
                d['number'] = v[0]
            elif kl == 'region':
                d['region'] = v[0]
            elif kl == 'type':
                d['type'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter phones. All possible keys are: language, '
                               'number, region, type'.format(k))
        return d


class AddDirectReports(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddDirectReports, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter direct_reports. All possible keys are: '
                               'deleted-date-time, id'.format(k))
        return d


class AddManager(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.manager = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter manager. All possible keys are: '
                               'deleted-date-time, id'.format(k))
        return d


class AddContactsOrgcontactMemberOf(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddContactsOrgcontactMemberOf, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter member_of. All possible keys are: '
                               'deleted-date-time, id'.format(k))
        return d


class AddContactsOrgcontactTransitiveMemberOf(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddContactsOrgcontactTransitiveMemberOf, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter transitive_member_of. All possible keys '
                               'are: deleted-date-time, id'.format(k))
        return d


class AddAlternativeSecurityIds(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddAlternativeSecurityIds, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'identity-provider':
                d['identity_provider'] = v[0]
            elif kl == 'key':
                d['key'] = v[0]
            elif kl == 'type':
                d['type'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter alternative_security_ids. All possible '
                               'keys are: identity-provider, key, type'.format(k))
        return d


class AddDevicesDeviceMemberOf(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddDevicesDeviceMemberOf, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter member_of. All possible keys are: '
                               'deleted-date-time, id'.format(k))
        return d


class AddRegisteredOwners(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddRegisteredOwners, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter registered_owners. All possible keys are: '
                               'deleted-date-time, id'.format(k))
        return d


class AddRegisteredUsers(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddRegisteredUsers, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter registered_users. All possible keys are: '
                               'deleted-date-time, id'.format(k))
        return d


class AddDevicesDeviceTransitiveMemberOf(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddDevicesDeviceTransitiveMemberOf, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter transitive_member_of. All possible keys '
                               'are: deleted-date-time, id'.format(k))
        return d


class AddDevicesDeviceExtensions(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddDevicesDeviceExtensions, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter extensions. All possible keys are: id'.
                format(k))
        return d


class AddDeletedItems(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddDeletedItems, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter deleted_items. All possible keys are: '
                               'deleted-date-time, id'.format(k))
        return d


class AddDirectoryMembers(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddDirectoryMembers, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter members. All possible keys are: '
                               'deleted-date-time, id'.format(k))
        return d


class AddDirectoryExtensions(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddDirectoryExtensions, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter extensions. All possible keys are: id'.
                format(k))
        return d


class AddRoleMemberInfo(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.role_member_info = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter role_member_info. All possible keys are: '
                               'display-name, id'.format(k))
        return d


class AddDirectoryrolesDirectoryroleMembers(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddDirectoryrolesDirectoryroleMembers, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter members. All possible keys are: '
                               'deleted-date-time, id'.format(k))
        return d


class AddState(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.state = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'last-action-date-time':
                d['last_action_date_time'] = v[0]
            elif kl == 'operation':
                d['operation'] = v[0]
            elif kl == 'status':
                d['status'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter state. All possible keys are: '
                               'last-action-date-time, operation, status'.format(k))
        return d


class AddDomainNameReferences(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddDomainNameReferences, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter domain_name_references. All possible keys '
                               'are: deleted-date-time, id'.format(k))
        return d


class AddServiceConfigurationRecords(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddServiceConfigurationRecords, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'is-optional':
                d['is_optional'] = v[0]
            elif kl == 'label':
                d['label'] = v[0]
            elif kl == 'record-type':
                d['record_type'] = v[0]
            elif kl == 'supported-service':
                d['supported_service'] = v[0]
            elif kl == 'ttl':
                d['ttl'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter service_configuration_records. All '
                               'possible keys are: is-optional, label, record-type, supported-service, ttl, id'.format(k))
        return d


class AddVerificationDnsRecords(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddVerificationDnsRecords, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'is-optional':
                d['is_optional'] = v[0]
            elif kl == 'label':
                d['label'] = v[0]
            elif kl == 'record-type':
                d['record_type'] = v[0]
            elif kl == 'supported-service':
                d['supported_service'] = v[0]
            elif kl == 'ttl':
                d['ttl'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter verification_dns_records. All possible '
                               'keys are: is-optional, label, record-type, supported-service, ttl, id'.format(k))
        return d


class AddAssignedPlans(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddAssignedPlans, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'assigned-date-time':
                d['assigned_date_time'] = v[0]
            elif kl == 'capability-status':
                d['capability_status'] = v[0]
            elif kl == 'service':
                d['service'] = v[0]
            elif kl == 'service-plan-id':
                d['service_plan_id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter assigned_plans. All possible keys are: '
                               'assigned-date-time, capability-status, service, service-plan-id'.format(k))
        return d


class AddPrivacyProfile(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.privacy_profile = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'contact-email':
                d['contact_email'] = v[0]
            elif kl == 'statement-url':
                d['statement_url'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter privacy_profile. All possible keys are: '
                               'contact-email, statement-url'.format(k))
        return d


class AddProvisionedPlans(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddProvisionedPlans, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'capability-status':
                d['capability_status'] = v[0]
            elif kl == 'provisioning-status':
                d['provisioning_status'] = v[0]
            elif kl == 'service':
                d['service'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter provisioned_plans. All possible keys are: '
                               'capability-status, provisioning-status, service'.format(k))
        return d


class AddVerifiedDomains(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddVerifiedDomains, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'capabilities':
                d['capabilities'] = v[0]
            elif kl == 'is-default':
                d['is_default'] = v[0]
            elif kl == 'is-initial':
                d['is_initial'] = v[0]
            elif kl == 'name':
                d['name'] = v[0]
            elif kl == 'type':
                d['type'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter verified_domains. All possible keys are: '
                               'capabilities, is-default, is-initial, name, type'.format(k))
        return d


class AddExtensions(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddExtensions, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter extensions. All possible keys are: id'.
                format(k))
        return d


class AddPrepaidUnits(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.prepaid_units = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'enabled':
                d['enabled'] = v[0]
            elif kl == 'suspended':
                d['suspended'] = v[0]
            elif kl == 'warning':
                d['warning'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter prepaid_units. All possible keys are: '
                               'enabled, suspended, warning'.format(k))
        return d


class AddServicePlans(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddServicePlans, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'applies-to':
                d['applies_to'] = v[0]
            elif kl == 'provisioning-status':
                d['provisioning_status'] = v[0]
            elif kl == 'service-plan-id':
                d['service_plan_id'] = v[0]
            elif kl == 'service-plan-name':
                d['service_plan_name'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter service_plans. All possible keys are: '
                               'applies-to, provisioning-status, service-plan-id, service-plan-name'.format(k))
        return d
