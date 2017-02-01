===============================
Cisco-EM
===============================

Python API

.. code-block:: python
::

    from cisco_em import CiscoEM

    manager = CiscoEM(
        username='user',
        password='pass',
        hostname='127.0.0.1',
    )

    for device in manager.inventory.devices:
        print(device.hostname)

    for credential in manager.credentials.list(credential_type='CLI'):
        print(credential.username)


Command Line

.. code-block:: shell
::

    $ cisco_em devices
    hostname01
    hostname02
    hostname03

    $ cisco_em credentials
    admin
    root
    ...


Config File
-----------

.. code-block:: shell
::

    cd $HOME
    vim .cisco_emrc

.. code-block:: ini
::

    [system]
    hostname = 127.0.0.1

    [credentials]
    username = user
    password = pass
