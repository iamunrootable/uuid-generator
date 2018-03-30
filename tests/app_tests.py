import unittest
import uuid

import app

# Helper

# adding a test comment
# another test
# another test comment
class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.app.test_client()


    def test_brigade_ci_meetup(self):
        resp = self.client.get('/')
        assert uuid.UUID(resp.data)
