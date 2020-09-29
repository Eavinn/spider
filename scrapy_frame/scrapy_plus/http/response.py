"""
三大内置对象：响应对象
"""
import json
import re
from lxml import etree


class Response(object):
    """响应类"""
    def __init__(self, url, status_code, headers, body, encoding, request):
        self.url = url
        self.status_code = status_code
        self.headers = headers
        self.body = body
        self.encoding = encoding
        self.request = request

    def xpath(self, rule=""):
        """复写xpath"""
        html_obj = etree.HTML(self.body)
        return html_obj.xpath(rule)

    def re_findall(self, rule="", string=None):
        """复写正则"""
        if string is None:
            string = self.body
        return re.findall(rule, string)

    @property
    def json(self):
        return json.loads(self.body)



