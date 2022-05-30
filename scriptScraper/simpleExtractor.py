import scrapydo
import logging
from .simpleSpider import SimpleBot

main_settings = {
    'USER_AGENT':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'ROBOTSTXT_OBEY': False,
    'DOWNLOAD_DELAY': 3,
    'COOKIES_ENABLED': False,
    'DEFAULT_REQUEST_HEADERS': {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en'
        },
    'FEEDS':{
        './scrape/data.json': {
        'format': 'json',
        'encoding': 'utf8',
        'store_empty': False,
        'fields': None,
        'indent': 2,
        'item_export_kwargs': {
            'export_empty_fields': True
            }
        }
    }
}

def scrape(request, custom_settings={}):
    scrapydo.setup()
    scrapydo.default_settings.update(main_settings)
    scrapydo.default_settings.update(custom_settings)
    logging.basicConfig(level=logging.DEBUG)
    results = scrapydo.run_spider(SimpleBot, request=request)
    data = { 'Massage': 'Scraping complete.', 
    'scraped_data': results
    }
    return data
