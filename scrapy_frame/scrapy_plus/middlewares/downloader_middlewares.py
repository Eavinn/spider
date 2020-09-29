"""
两个中间件：下载器中间件
     对请求对象和响应对象进行预处理
"""

from scrapy_plus.utils.log import logger


class DownloadMiddleware(object):
    """下载中间件"""
    def process_request(self, request):
        logger.info("Request经过下载中间件")
        return request

    def process_response(self, response):
        logger.info("Response经过下载中间件")
        return response
