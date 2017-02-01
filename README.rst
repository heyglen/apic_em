===============================
Cisco-EM
===============================

Project

.. highlight:: python
::
    from cisco_em import CiscoEM

    manager = CiscoEM(
        username='user',
        password='pass',
        hostname='127.0.0.1',
    )

    for device in manager.devices:
        print(device.hostname)


.. highlight:: shell
::
    $ cisco_em devices
    hostname01
    hostname02
    hostname03
    ...


Features
--------

* TODO

