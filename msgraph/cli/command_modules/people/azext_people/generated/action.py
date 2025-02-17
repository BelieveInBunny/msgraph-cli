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


class AddPersonType(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.person_type = action

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
            if kl == 'class':
                d['class_property'] = v[0]
            elif kl == 'subclass':
                d['subclass'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter person_type. All possible keys are: '
                               'class, subclass'.format(k))
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


class AddScoredEmailAddresses(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddScoredEmailAddresses, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'address':
                d['address'] = v[0]
            elif kl == 'item-id':
                d['item_id'] = v[0]
            elif kl == 'relevance-score':
                d['relevance_score'] = v[0]
            elif kl == 'selection-likelihood':
                d['selection_likelihood'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter scored_email_addresses. All possible keys '
                               'are: address, item-id, relevance-score, selection-likelihood'.format(k))
        return d


class AddWebsites(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddWebsites, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'address':
                d['address'] = v[0]
            elif kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'type':
                d['type'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter websites. All possible keys are: address, '
                               'display-name, type'.format(k))
        return d


class AddResourceReference(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.resource_reference = action

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
            elif kl == 'type':
                d['type'] = v[0]
            elif kl == 'web-url':
                d['web_url'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter resource_reference. All possible keys '
                               'are: id, type, web-url'.format(k))
        return d


class AddResourceVisualization(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.resource_visualization = action

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
            if kl == 'container-display-name':
                d['container_display_name'] = v[0]
            elif kl == 'container-type':
                d['container_type'] = v[0]
            elif kl == 'container-web-url':
                d['container_web_url'] = v[0]
            elif kl == 'media-type':
                d['media_type'] = v[0]
            elif kl == 'preview-image-url':
                d['preview_image_url'] = v[0]
            elif kl == 'preview-text':
                d['preview_text'] = v[0]
            elif kl == 'title':
                d['title'] = v[0]
            elif kl == 'type':
                d['type'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter resource_visualization. All possible keys '
                               'are: container-display-name, container-type, container-web-url, media-type, '
                               'preview-image-url, preview-text, title, type'.format(k))
        return d


class AddSharedBy(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.shared_by = action

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
            if kl == 'address':
                d['address'] = v[0]
            elif kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter shared_by. All possible keys are: '
                               'address, display-name, id'.format(k))
        return d


class AddLastUsed(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.last_used = action

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
            if kl == 'last-accessed-date-time':
                d['last_accessed_date_time'] = v[0]
            elif kl == 'last-modified-date-time':
                d['last_modified_date_time'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter last_used. All possible keys are: '
                               'last-accessed-date-time, last-modified-date-time'.format(k))
        return d
