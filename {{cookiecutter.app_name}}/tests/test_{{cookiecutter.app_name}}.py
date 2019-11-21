# -*- coding: utf-8 -*-

import unittest
from {{cookiecutter.app_name}} import ping

class TestPing(unittest.TestCase):

    def test_ping(self):
        self.assertEqual('PONG!', ping())   
