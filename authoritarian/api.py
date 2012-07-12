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
    # TODO: validate engine + locale
    #path = '/keywords%s' % ('/priority' if immediate else '')
    #response = requests.post(BASE + path,
    response = requests.post(BASE + {
            True: '/keywords/priority',
            False: '/keywords'
        }[immediate],

        data={
            'auth_token': config['api_key'],
            'keyword': keyword,
            'engine': engine,
            'locale': locale,
        }
    )
    if response.ok:
        return response.json


def results(keyword, engine, locale, rank_date):
    response = requests.get(BASE + '/keywords/get.json',
        params={
            'auth_token': config['api_key'],
            'keyword': keyword,
            'response_format': 'json',
            'engine': engine,
            'locale': locale,
            'rank_date': rank_date,
        }
    )
    if response.ok:
        return response.json
