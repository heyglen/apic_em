# -*- coding: utf-8 -*-


import pathlib

import logging
import json

import requests

from .utilities.configuration_file import ConfigurationFile
from .em_modules.inventory import Inventory
from .em_modules.credentials import Credentials

logger = logging.getLogger(__name__)


class CiscoEM(object):
    _default_header = {"Content-Type": "application/json"}

    def __init__(self, username=None, password=None, hostname=None, verify=None):
        username = username or self._get_config('credentials', 'username')
        password = password or self._get_config('credentials', 'password')
        hostname = hostname or self._get_config('system', 'hostname')
        self._url = 'https://{}'.format(
            '/'.join([
                hostname,
                'api',
                'v1',
            ])
        )
        if verify is None:
            verify = self._get_config('security', 'verify') == 'true'
        if verify is None:
            verify = True
        headers = self._default_header.copy()
        headers['X-Auth-Token'] = self._get_ticket(username, password, verify)
        self._headers = {
            'verify': verify,
            'headers': headers,
        }

    def _get_config(self, section, value):
        if not hasattr(self, '_config_file'):
            config_file = str(pathlib.Path().home() / '.cisco_emrc')
            self._config_file = ConfigurationFile.get(config_file)
        section = self._config_file.get(section)
        if section is not None:
            return section.get(value)

    def _get_ticket(self, username, password, verify):
        body = dict(
            username=username,
            password=password,
        )
        url = '/'.join([self._url, 'ticket'])
        response = requests.post(
            url,
            data=json.dumps(body),
            headers=self._default_header,
            verify=verify,
        )
        data = response.json()
        ticket = data['response']['serviceTicket']
        logger.debug('Got ticket')
        return ticket

    @property
    def inventory(self):
        if not hasattr(self, '_inventory'):
            self._inventory = Inventory(self)
        return self._inventory

    @property
    def credentials(self):
        if not hasattr(self, '_credentials'):
            self._credentials = Credentials(self)
        return self._credentials
