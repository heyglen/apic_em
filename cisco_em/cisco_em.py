# -*- coding: utf-8 -*-


import pathlib

import logging
from collections import namedtuple
import json

import requests

from .configuration_file import ConfigurationFile

logger = logging.getLogger(__name__)


class CiscoEM(object):
    _default_header = {"content-type": "application/json"}

    def __init__(self, username=None, password=None, hostname=None):
        self.username = username or self._get_config('credentials', 'username')
        self.password = password or self._get_config('credentials', 'password')
        hostname = hostname or self._get_config('system', 'hostname')
        self.url = 'https://{}'.format(
            '/'.join([
                hostname,
                'api',
                'v1',
            ])
        )
        self._header = self._default_header.copy()
        self._get_ticket()

    def _get_config(self, section, value):
        if not hasattr(self, '_config_file'):
            config_file = str(pathlib.Path().home() / '.cisco_emrc')
            self._config_file = ConfigurationFile.get(config_file)
        section = self._config_file.get(section)
        if section is not None:
            return section.get(value)

    def _get_ticket(self):
        if not self._header.get('X-Auth-Token'):
            body = dict(
                username=self.username,
                password=self.password,
            )
            response = requests.post(
                '/'.join([self.url, 'ticket']),
                headers=self._header,
                data=json.dumps(body),
                verify=False,
            )
            data = response.json()
            ticket = data['response']['serviceTicket']
            logger.debug('ticket: {}'.format(ticket))
            self._header.update({
                'X-Auth-Token': ticket,
            })

    def _get_device(self, device_dict):
        class Device(namedtuple('Device', device_dict.keys())):
            def __repr__(self):
                attributes = list()
                for key in device_dict:
                    attributes.append('='.join([
                        key,
                        getattr(self, key)
                    ]))
                return '<Device {}>'.format(
                    ','.join(attributes)
                )
        device = Device(**device_dict)
        return device

    @property
    def topology(self):
        url = '/'.join([self.url, 'network-device'])
        response = requests.get(
            url,
            headers=self._header,
            verify=False,
        )
        data = response.json()['response']
        devices = list()
        logger.debug(data[0].keys())
        for device_dict in data:
            devices.append(self._get_device(device_dict))
        return devices
