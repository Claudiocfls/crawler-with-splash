import logging
from scrapy import signals
from ..settings import TARGET_DIR
import os
from ..services.DatabaseService import DatabaseService

class InitialSetupExtension:
    def __init__(self):
        pass

    @classmethod
    def from_crawler(cls, crawler):
        ext = cls()

        # connect the extension object to signals
        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)

        # return the extension object
        return ext

    def spider_opened(self, spider):
        try:
            os.makedirs(TARGET_DIR)
        except:
            pass
        DatabaseService.get_instance()
