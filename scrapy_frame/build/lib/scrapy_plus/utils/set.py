"""
构建指纹保存类
"""


import redis
from scrapy_plus.conf.default_settings import *


class FilterSet(object):
    """用set保存指纹"""
    def __init__(self):
        self._filter_set = set()

    def add_fp(self, fp):
        self._filter_set.add(fp)

    def is_filter(self, fp):
        return True  if fp in self._filter_set else False


class RedisFilterSet(object):
    """用redis保存指纹"""
    def __init__(self):
        self._filter_set = redis.StrictRedis(host=REDIS_QUEUE_HOST, port=REDIS_QUEUE_PORT, db=REDIS_QUEUE_DB)
        self._key_name = REDIS_SET_NAME

    def add_fp(self, fp):
        self._filter_set.sadd(self._key_name, fp)

    def is_filter(self, fp):
        return True if self._filter_set.sismember(self._key_name, fp) else False
