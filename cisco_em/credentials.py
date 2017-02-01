
import logging

import requests

from .em_module import EmModule

logger = logging.getLogger(__name__)


class Credentials(EmModule):
    _default_credential_type = 'CLI'

    def list(self, credential_type=None):
        credential_type = credential_type or self._default_credential_type
        url = '/'.join([self._url, 'global-credential'])
        attributes = {
            'credentialSubType': credential_type
        }
        attribute_str = '&'.join(['{}={}'.format(k, v) for k, v in attributes.items()])
        url = '{}?{}'.format(
            url,
            attribute_str
        )
        logger.debug(url)
        response = requests.get(
            url,
            **self._headers
        )
        data = response.json()['response']
        devices = list()
        for value in data:
            data = self._build('Credential', value, 'username')
            if data is not None:
                devices.append(data)
        return devices
