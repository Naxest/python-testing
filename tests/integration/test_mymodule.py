import unittest
from project import mymodule

class TestIntegrationMyModule(unittest.TestCase):

    def test_given_url_when_call_get_headers_from_url_then_return_headers_including_content_type(self):
        url = "http://google.com/"
        headers = mymodule.get_headers_from_url(url)

        self.assertIn("Content-Type", headers)