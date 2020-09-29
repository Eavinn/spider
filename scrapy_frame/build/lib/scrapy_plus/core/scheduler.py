
"""
五大核心组件：调度器组件
     缓存请求对象(Request)，并为下载器提供请求对象，实现请求的调度
     对请求对象进行去重判断

1.使用six可以有效解决Python2和python3导入模块的兼容性问题
2.使用w3lib对url参数排序
3.使用sha1加密指纹
"""


from w3lib.url import canonicalize_url
from hashlib import sha1
from scrapy_plus.conf.default_settings import *
if ROLE is None:
    from six.moves.queue import Queue
    from scrapy_plus.utils.set import FilterSet as Set
else:
    from scrapy_plus.utils.queue import Queue
    from scrapy_plus.utils.set import RedisFilterSet as Set

from scrapy_plus.utils.log import logger


class Scheduler(object):
    def __init__(self):
        self.queue = Queue()
        self._filter_set = Set()
        self.total_request = 0

    def add_request(self, request):
        """判断请求是否需要去重，并添加到请求队列、指纹"""
        if not request.do_filter:
            logger.info("Add Request(dont filter) [{}] <{}>".format(request.method, request.url))
            self.queue.put(request)
            self.total_request += 1
            return

        fp = self._get_fingerprint(request)
        if not self._filter_request(request, fp):
            logger.info("Add Request [{}] <{}>".format(request.method, request.url))
            self.queue.put(request)
            self.total_request += 1
            self._filter_set.add_fp(fp)

    def get_request(self):
        """获取请求队列中的请求，交给引擎"""
        try:
            return self.queue.get(False)
        except:
            return None

    def _filter_request(self, request, fp):
        """请求去重"""
        if self._filter_set.is_filter(fp):
            logger.warning("去除重复请求：url=%s, fp=%s" % (request.url, fp))
            return True
        else:
            return False

    def _get_fingerprint(self, request):
        """sha1加密组合请求指纹字符串"""
        url = canonicalize_url(request.url)
        method = request.method.upper()
        params = str(sorted(request.params.items(), key=lambda x: x[0])) if request.params else ""
        data = str(sorted(request.data.items(), key=lambda x: x[0])) if request.data else ""

        s1 = sha1()
        s1.update((url + method + params + data).encode("utf-8"))
        fp = s1.hexdigest()
        return fp
