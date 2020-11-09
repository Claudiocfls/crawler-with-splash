
TARGET_DIR = '{{TARGET_DIR}}/{{TAG}}'
ALLOWED_DOMAIN = '{{ALLOWED_DOMAIN}}'
INITIAL_URL = '{{INITIAL_URL}}'
DEPTH_LIMIT = {{DEPTH_LIMIT}}

BOT_NAME = 'generic_crawler'

SPIDER_MODULES = ['generic_crawler.spiders']
NEWSPIDER_MODULE = 'generic_crawler.spiders'

# necessary to use BFO (scrapy use DFO by default)
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'

# LOG LEVEL: DEBUG < INFO < WARNING < ERROR < CRITICAL
LOG_LEVEL = 'ERROR'
LOG_FILE = '{}/logs.txt'.format(TARGET_DIR)

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'generic_crawler (+http://www.yourdomain.com)'
#USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:23.0) Gecko/20100101 Firefox/23.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 45
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 1
CONCURRENT_REQUESTS_PER_IP = 1

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = True
TELNETCONSOLE_USERNAME="scrapy"
TELNETCONSOLE_PASSWORD="1234"
TELNETCONSOLE_PORT=[6023]

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
  "Accept-Encoding": "gzip, deflate, br", 
  "Accept-Language": "en-US,en;q=0.9", 
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'generic_crawler.middlewares.GenericCrawlerSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'generic_crawler.middlewares.downloader_middlewares.drop_query_strings.DropQueryStringsMiddleware': 70,
    'generic_crawler.middlewares.downloader_middlewares.save_on_database.SaveOnDatabaseMiddleware': 91,
    'generic_crawler.middlewares.downloader_middlewares.ua_rotation.RotateUserAgentMiddleware': 510,
}

USER_AGENT_CHOICES = [
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:23.0) Gecko/20100101 Firefox/23.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20140205 Firefox/24.0 Iceweasel/24.3.0',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:28.0) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
]

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
    'generic_crawler.extensions.save_stats.SaveStatsExtension': 100,
    'generic_crawler.extensions.initial_setup.InitialSetupExtension': 90,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False
