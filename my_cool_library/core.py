# -*- coding: utf-8 -*-
#
from __future__ import unicode_literals

import io
import json


class JSONDatabase(object):
    def __init__(self, filename=None, data={}):
        self.filename = filename
        self.data = data

    def state_to_json(self):
        return json.dumps(self.data)

    def save(self):
        # open file
        fd = io.open(self.filename, 'wb')
        fd.write(self.state_to_json())
        fd.close()
