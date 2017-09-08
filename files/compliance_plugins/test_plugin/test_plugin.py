#!/usr/bin/python
'''
@since: 09 Sep 2017
@author: Prashant Bhosale <pbhosale@lenovo.com>
@license: Lenovo License
@copyright: Copyright 2017, Lenovo
@organization: Lenovo
@summary: This module provides command class implementation for PyLXCA
'''

import sys
import os
sys.path.insert(0, '..')
from compliance_plugin_base.compliance_plugin_base import *

class test_plugin(compliance_plugin_base):
    def load_facts(self):
        return

    def validate_complaince(self):
        return True
