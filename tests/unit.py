import sys
import base64
from testify import TestCase, assert_equal, setup, teardown, assert_raises
from urllib import urlencode
import requests
import authoritarian
from mock import Mock, patch
import omnijson as json

class AuthoritarianTestCase(TestCase): 

    @setup
    def setup(self):
        self.requests_patcher = patch('authoritarian.api._request')
        self.request = self.requests_patcher.start()
        self.response = Mock(spec=requests.Response,
            status_code=200, 
            headers={},
            text='')
        self.request.return_value = self.response

    @teardown
    def teardown(self):
        self.requests_patcher.stop()

    def test_initialise(self):
        pass

    def test_account_status(self):
        pass

    def test_search_delayed(self):
        pass

    def test_search_immediate(self):
        pass

    def test_results(self):
        pass
