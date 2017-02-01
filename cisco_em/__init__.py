# -*- coding: utf-8 -*-

import requests

from .utilities.log_setup import log_setup

log_setup()

requests.packages.urllib3.disable_warnings()

from .apic_em import ApicEM

__author__ = """Glen Harmon"""
__email__ = 'ghar@nnit.com'
__version__ = '0.1.0'
