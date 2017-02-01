===============================
Cisco-EM
===============================

Project

.. code-block:: python
::

    from cisco_em import CiscoEM

    manager = CiscoEM(
        username='user',
        password='pass',
        hostname='127.0.0.1',
    )

    for device in manager.devices:
        print(device.hostname)


.. code-block:: shell
::

    $ cisco_em devices
    hostname01
    hostname02
    hostname03
    ...


Features
--------

* TODO
