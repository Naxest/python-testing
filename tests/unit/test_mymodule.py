import unittest

from mock import patch
from pythontesting import mymodule

class TestUnitMyModule(unittest.TestCase):

    def setUp(self):
        self._requester_patch = patch("pythontesting.mymodule.Requester")
        self._requester_mock = self._requester_patch.start()

    def tearDown(self):
        self._requester_patch.stop()

    def test_given_url_when_get_headers_from_url_then_uses_requester(self):
        url = "http://name.com"
        mymodule.get_headers_from_url(url)

        self._requester_mock.assert_called_once_with(url)
        self._requester_mock.return_value.make_request.assert_called_once_with()

class TestUnitRequester(unittest.TestCase):

    @patch("requests.get")
    def test_given_url_when_creates_requester_and_call_make_request_then_uses_requests_get(self, reqget_mock):
        url = "http://name.com"
        requester = mymodule.Requester(url)
        requester.make_request()

        reqget_mock.assert_called_once_with(url=url)


