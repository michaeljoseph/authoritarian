![authoritarian](https://github.com/michaeljoseph/authoritarian/raw/master/resources/you.jpg)

# authoritarian

Python API for the [AuthorityLabs Partner API](http://authoritylabs.com/api/partner-api/).

[![Build Status](https://secure.travis-ci.org/michaeljoseph/authoritarian.png)](http://travis-ci.org/michaeljoseph/authoritarian)

This is a light [requests](https://github.com/kennethreitz/requests)-based wrapper over the API that provides the following features:

* validation of supported AuthorityLabs [search engines](http://authoritylabs.com/api/reference/#engines)
* validation of support AuthorityLabs [locales](http://authoritylabs.com/api/reference/#countries)

## Installation

    pip install authoritarian

## Usage

    import authoritarian
    api_key = 'da39a3ee5e6b4b0d3255'
    account_id = '123'
    authoritarian.initialise(api_key, account_id)

    # returns https://gist.github.com/1201594#file_al_partner_api_accounts.json
    status_json = authoritarian.account_status()
	
    keyword = 'your country needs you'
    engine = 'google'
    locale = 'en-us'
    success = authoritarian.search(keyword, engine, locale)
      
    success = authoritarian.search(keyword, engine, locale, immediate=True)

    rank_date = '2012-07-07'
    # returns https://gist.github.com/1201614
    response_json = authoritarian.results(keyword, engine, locale, rank_date)
