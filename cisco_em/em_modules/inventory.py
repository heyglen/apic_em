
import requests

from .em_module_base import EmModuleBase


class Inventory(EmModuleBase):

    @property
    def devices(self):
        url = '/'.join([self._url, 'network-device'])
        response = requests.get(
            url,
            **self._headers
        )
        data = response.json()['response']
        devices = list()
        for device_dict in data:
            value = self._build('Device', device_dict, 'hostname')
            if value is not None:
                devices.append(value)
        return devices
