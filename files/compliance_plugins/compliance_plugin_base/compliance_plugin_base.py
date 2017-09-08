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

class compliance_plugin_base():

    def get_name(self):
        filename = sys.modules[self.__class__.__module__].__file__
        name = os.path.splitext(os.path.basename(filename))[0]
        return name

    def load_facts(self):
        return

    def validate_complaince(self):
        return True