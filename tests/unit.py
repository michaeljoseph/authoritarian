from testify import TestCase, setup, teardown, assert_equal
import requests
import authoritarian
from mock import Mock, patch

class AuthoritarianTestCase(TestCase): 

    @setup
    def setup(self):
        self.requests_patcher = patch('authoritarian.api.requests')
        self.requests = self.requests_patcher.start()
        self.response = Mock(spec=requests.Response,
            status_code=200, 
            headers={},
            json='{}')
        self.requests.get.return_value = self.response

    @teardown
    def teardown(self):
        self.requests_patcher.stop()

    def test_initialise(self):
        authoritarian.initialise('api-key')
        assert_equal(authoritarian.config['api_key'], 'api-key')
        assert_equal(authoritarian.config['account_id'], None)

    def test_account_status(self):
        authoritarian.initialise('api-key', 'account-id')
        expected_response = {'json': 'response'}
        self.response.json = expected_response 
        response = authoritarian.account_status()
        assert_equal(response, expected_response)
        self.requests.get.assert_called_once_with(
            'http://api.authoritylabs.com/account/account-id.json',
            params={'auth_token': 'api-key'})

    def test_search_delayed(self):
        pass

    def test_search_immediate(self):
        pass

    def test_results(self):
        pass
