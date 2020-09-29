"""
管道、中间件 处理请求、响应、item 不区分爬虫
"""

from spiders import BaiduSpider, DoubanSpider


class BaiduPipeline(object):
    def process_item(self, item, spider):
        if isinstance(spider, BaiduSpider):
            print("这是百度spider的数据: {}".format(item.data))
        return item


class DoubanPipeline(object):
    def process_item(self, item, spider):
        if isinstance(spider, DoubanSpider):
            print("这是豆瓣spider的数据: {}".format(item.data))
        return item
