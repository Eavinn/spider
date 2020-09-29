# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random


class UserAgentMiddleware(object):
    def process_request(self, request, spider):
        """设置User-Agent"""
        user_agent = random.choice(["此处传入User-Agent列表"])
        request.header["User-Agent"] = user_agent


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        """设置代理"""
        proxy = "username:passwd@ip:port"
        request.meta["proxy"] = "http://" + proxy
