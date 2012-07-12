import requests

config = {}
BASE = 'http://api.authoritylabs.com'


def initialise(api_key, account_id=None):
    config['api_key'] = api_key
    config['account_id'] = account_id


def account_status():
    response = requests.get(BASE + '/account/%s.json' % config['account_id'],
        params={
            'auth_token': config['api_key']
        }
    )
    if response.ok:
        return response.json


def search(keyword, engine, locale, immediate=False):
    pass


def results(keyword, engine, locale, rank_date):
    pass
