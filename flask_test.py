import my_app
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        my_app.app.testing = True
        self.app = my_app.app.test_client()

    def test_home(self):
        result = self.app.get('/')
        # asseertions here

# exec test w/ python -m unittest discover
