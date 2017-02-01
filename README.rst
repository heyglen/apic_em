===============================
Apic-EM
===============================

Pythonic wrapper to the Apic-EM REST API

Python API

.. code-block:: python
::

    from apic_em import ApicEM

    manager = ApicEM(
        username='user',
        password='pass',
        hostname='127.0.0.1',
    )

    for device in manager.devices.list():
        print(device.hostname)

    for credential in manager.credentials.list(credential_type='CLI'):
        print(credential.username)


Command Line

.. code-block:: shell
::

    $ apic_em devices
    hostname01
    hostname02
    hostname03

    $ apic_em credentials
    admin
    root
    ...


Config File
-----------

.. code-block:: shell
::

    cd $HOME
    vim .apic_emrc

.. code-block:: ini
::

    [system]
    hostname = 127.0.0.1

    [credentials]
    username = user
    password = pass


Install
-------

.. code-block:: shell
::
    pip3 install git+https://github.com/heyglen/apic_em.git
