import scrapy
from ..settings import ALLOWED_DOMAIN
from ..settings import INITIAL_URL
import re

class GenericSpider(scrapy.Spider):
    name = "generic_spider"
    rotate_user_agent = True
    allowed_domains = [ALLOWED_DOMAIN]

    def start_requests(self):
        urls = [INITIAL_URL]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.crawler.stats.inc_value('generic_spider/parse_calls')
        next_pages = response.css('a').xpath('@href').getall()
        next_pages = self.filter_urls(next_pages)
        for link in next_pages:
            with open('links.txt', 'a+') as file:
                file.write(link + '\n')
            next_link = response.urljoin(link)
            yield scrapy.Request(next_link, callback=self.parse)
    
    def filter_urls(self, list_of_urls_extracted):
        def should_follow(link):
            if re.search('^javascript', link):
                return False
            return True
        return filter(should_follow, list_of_urls_extracted)
