import scrapy
from ..settings import ALLOWED_DOMAIN
from ..settings import INITIAL_URL
import re
from scrapy_splash import SplashRequest

class GenericSpider(scrapy.Spider):
    name = "generic_spider"
    rotate_user_agent = True
    allowed_domains = [ALLOWED_DOMAIN]
    script = '''
        function main(splash)
        local url = splash.args.url
        assert(splash:go(url))
        assert(splash:wait(0.5))
        return {
            html = splash:html(),
            png = splash:png(),
            har = splash:har(),
        }
        end
    '''

    def start_requests(self):
        urls = [INITIAL_URL]
        for url in urls:
            yield SplashRequest(url, self.parse, args={'lua_source': self.script}, endpoint='execute')

    def parse(self, response):
        self.crawler.stats.inc_value('generic_spider/parse_calls')
        next_pages = response.css('a').xpath('@href').getall()
        next_pages = self.filter_urls(next_pages)
        for link in next_pages:
            with open('links.txt', 'a+') as file:
                file.write(link + '\n')
            next_link = response.urljoin(link)
            yield SplashRequest(next_link, self.parse, args={'lua_source': self.script}, endpoint='execute')
    
    def filter_urls(self, list_of_urls_extracted):
        def should_follow(link):
            if re.search('^(javascript)|(mailto)', link):
                return False
            return True
        return filter(should_follow, list_of_urls_extracted)
