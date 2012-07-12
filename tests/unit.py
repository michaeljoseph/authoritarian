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
        self.requests.post.return_value = self.response

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
        authoritarian.initialise('api-key')
        authoritarian.search('your country needs you', 'google',
            'en-us')
        self.requests.post.assert_called_once_with(
            'http://api.authoritylabs.com/keywords',
            data={
                'auth_token': 'api-key',
                'keyword': 'your country needs you',
                'engine': 'google',
                'locale': 'en-us',
            }
        )

    def test_search_immediate(self):
        authoritarian.initialise('api-key')
        authoritarian.search('your country needs you', 'google', 
            'en-us', immediate=True)
        self.requests.post.assert_called_once_with(
            'http://api.authoritylabs.com/keywords/priority',
            data={
                'auth_token': 'api-key',
                'keyword': 'your country needs you',
                'engine': 'google',
                'locale': 'en-us',
            }
        )
    def test_results(self):
        authoritarian.initialise('api-key')
        authoritarian.results('your country needs you', 'google', 
            'en-us', '2012-07-12')
        self.requests.get.assert_called_once_with(
            'http://api.authoritylabs.com/keywords/get.json',
            params={
                'auth_token': 'api-key',
                'keyword': 'your country needs you',
                'response_format': 'json',
                'engine': 'google',
                'locale': 'en-us',
                'rank_date': '2012-07-12',
            }
        )
