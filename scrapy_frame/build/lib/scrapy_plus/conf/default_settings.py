"""
配置信息
"""

# log配置
import logging
DEFAULT_LOG_LEVEL = logging.INFO
DEFAULT_LOG_FMT = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s'
DEFUALT_LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'
DEFAULT_LOG_FILENAME = 'scrapy_plus.log'

SPIDERS = []

PIPELINES = []

SPIDER_MIDDLEWARES = []

DOWNLOADER_MIDDLEWARES = []

# 异步数量
ASYNC_COUNT = 5

# 开协程还是多线程
ASYNC_TYPE = "coroutine"
# ASYNC_TYPE = "thread"

# 非分布式
ROLE = None
# 分布式模式
# ROLE = "slave"
# ROLE = "master"

# redis配置
REDIS_QUEUE_NAME = 'request_queue'
REDIS_SET_NAME = "fingerprint_set"
REDIS_QUEUE_HOST = '192.168.49.154'
REDIS_QUEUE_PORT = 6379
REDIS_QUEUE_DB = 4

from settings import *
