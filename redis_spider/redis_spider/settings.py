# Scrapy settings for redis_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'redis_spider'

SPIDER_MODULES = ['redis_spider.spiders']
NEWSPIDER_MODULE = 'redis_spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'redis_spider.middlewares.RedisSpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'redis_spider.middlewares.AqiSeleniumMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# 必须1：表示使用scrapy-redis提供的去重类，也就是在Redis数据库中去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 必须2：表示使用scrapy-redis提供的调度器类，也就是和Redis数据库交互请求数据
SCHEDULER = "scrapy_redis.scheduler.Scheduler"


# 必须3：表示程序可以中途暂停，不清空Redis的请求队列
SCHEDULER_PERSIST = True

# 必须4：表示Redis数据库的IP和PORT
REDIS_HOST = "192.168.49.153"
REDIS_PORT = 6379
REDIS_PARAMS = {
    'db': 3
}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'redis_spider.pipelines.AqiPipeline': 200,
    'redis_spider.pipelines.AqiJsonPipeline': 300,
    'redis_spider.pipelines.AqiCsvPipeline': 400,
    'redis_spider.pipelines.AqiMongoPipeline': 500,
    'scrapy_redis.pipelines.RedisPipeline': 600,
}

