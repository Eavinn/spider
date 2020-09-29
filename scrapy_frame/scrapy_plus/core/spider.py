"""
五大核心组件：爬虫组件
    构建请求信息(初始的)，也就是生成请求对象(Request)
    解析响应对象，返回数据对象(Item)或者新的请求对象(Request)
"""

from scrapy_plus.http.request import Request


class Spider(object):
    """spider类作为程序入口"""
    start_urls = []

    def start_requests(self):
        if not self.start_urls:
            raise Exception("start_urls list cannot be empty")
        for start_url in self.start_urls:
            yield Request(start_url)

    def parse(self, response):
        raise Exception("parse function cannot be empty")

