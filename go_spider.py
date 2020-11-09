from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from generic_crawler.spiders.generic_spider import GenericSpider

process = CrawlerProcess(get_project_settings())
process.crawl(GenericSpider)
process.start()