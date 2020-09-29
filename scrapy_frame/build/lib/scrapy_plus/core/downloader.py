
"""
五大核心组件：下载器组件
     根据请求对象(Request)，发起HTTP、HTTPS网络请求，拿到HTTP、HTTPS响应，构建响应对象(Response)并返回
"""

import requests
import chardet
from scrapy_plus.utils.log import logger
from scrapy_plus.http.response import Response


class Downloader(object):
    """下载器"""
    def get_response(self, request):

        if request.method.upper() == "GET":
            response = requests.get(request.url, headers=request.headers, params=request.params)
        elif request.method.upper() == "POST":
            response = requests.post(request.url, headers=request.headers, data=request.data)
        else:
            raise Exception("Error: wrong request method")
        logger.info("[{}] <{}>".format(response.status_code, response.url))

        # 判断响应编码
        encoding = chardet.detect(response.content)["encoding"]
        return Response(response.url, response.status_code, response.headers,
                        response.content, encoding, request)



