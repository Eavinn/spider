"""
两个中间件：爬虫中间件
     对请求对象和数据对象进行预处理
"""

from scrapy_plus.utils.log import logger


class SpiderMiddleware(object):
    """爬虫中间件"""
    def process_request(self, request):
        logger.info("Request经过爬虫中间件")
        return request

    def process_item(self, item):
        logger.info("Item经过爬虫中间件")
        return item
