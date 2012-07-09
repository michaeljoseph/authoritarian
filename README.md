# authoritarian

Python API for the [AuthorityLabs Partner API](http://authoritylabs.com/api/partner-api/).

This is a light [requests](https://github.com/kennethreitz/requests)-based wrapper over the API that provides the following features:

* validation of supported AuthorityLabs [search engines](http://authoritylabs.com/api/reference/#engines)
* validation of support AuthorityLabs [locales](http://authoritylabs.com/api/reference/#countries)

## Installation

    pip install authoritarian

## Usage

    import authoritarian
    api_key = 'da39a3ee5e6b4b0d3255'
    authoritarian.initialise(api_key)

    status = authoritarian.account_status()
	
    keyword = 'your country needs you'
    engine = 'google'
    locale = 'en-us'
    response = authoritarian.search(keyword, engine, locale)
      
    response = authoritarian.search(keyword, engine, locale, immediate=True)

    rank_date = '2012-07-07'
    response = authoritarian.results(keyword, engine, locale, rank_date)
