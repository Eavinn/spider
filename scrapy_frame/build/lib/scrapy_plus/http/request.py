"""
三大内置对象：请求对象
"""
import random


class Request(object):
    """请求类"""
    def __init__(self, url, method="GET", headers=None, params=None, data=None, callback="parse",
                 spider=None, do_filter=True):
        self.url = url
        self.method = method
        self.headers = headers
        self.params = params
        self.data = data
        self.callback = callback
        self.spider = spider
        self.do_filter = do_filter
        self.change_head()

    def change_head(self):
        """构建请求头避免反扒"""
        user_list = (
            {'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1"},
            {'user-agent': "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1"},
            {'user-agent': "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11"},
            {'user-agent': "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11"},
            {'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
        )
        user_agent = random.choice(user_list)
        self.headers = user_agent


