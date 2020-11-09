import logging
from scrapy import signals
from ..settings import TARGET_DIR

logger = logging.getLogger(__name__)

class SaveStatsExtension:
    def __init__(self, stats):
        self.stats = stats

    @classmethod
    def from_crawler(cls, crawler):
        ext = cls(crawler.stats)

        # connect the extension object to signals
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)

        # return the extension object
        return ext

    def spider_closed(self, spider):
        logger.info("closed spider %s", spider.name)
        keys = self.stats.get_stats().keys()
        keys = sorted([c for c in keys])
        with open('/'.join([TARGET_DIR, 'stats.txt']), 'w+') as file:
            for key in keys:
                file.write("'{}': {}\n".format(key, self.stats.get_stats()[key]))
