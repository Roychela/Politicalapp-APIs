import unittest
from app import politicoapp

class ApiRouteTests(unittest.TestCase):
    def setUp(self):
        self.app = politicoapp()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app.testing = False    