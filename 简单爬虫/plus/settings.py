DEFAULT_LOG_FILENAME = 'spider.log'

SPIDERS = [
    "spiders.BaiduSpider",
    "spiders.DoubanSpider",
]

PIPELINES = [
    "pipelines.BaiduPipeline",
    "pipelines.DoubanPipeline"
]

SPIDER_MIDDLEWARES = [
    "middlewares.SpiderMiddlewareFirst",
    "middlewares.SpiderMiddlewareSecond",
]

DOWNLOADER_MIDDLEWARES = [
    "middlewares.DownloadMiddlewareFirst",
    "middlewares.DownloadMiddlewareSecond",
]

ASYNC_COUNT = 5
ASYNC_TYPE = "coroutine"

# redis队列默认配置
ROLE = None
REDIS_QUEUE_NAME = 'request_queue'
REDIS_SET_NAME = "fingerprint_set"
REDIS_QUEUE_HOST = '192.168.49.154'
REDIS_QUEUE_PORT = 6379
REDIS_QUEUE_DB = 4
