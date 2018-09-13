#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import unittest
from jsonschema import validate


class TestJsonschema(unittest.TestCase):

    with open('/src/tests/schema.json', 'r') as f:
        schema = json.load(f)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_jsonschema(self):
        for _, _, files in os.walk('/src/stable', followlinks=False):
            file_path_list = ['/src/stable/'+item for item in files]

        for _, _, files in os.walk('/src/incubator', followlinks=False):
            file_path_list.extend(['/src/incubator/'+item for item in files])

        for item in file_path_list:
            with open(item, 'r') as f:
                validate(json.load(f), self.schema)

if __name__ == '__main__':
    unittest.main()
