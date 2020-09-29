
"""
五大核心组件：引擎组件
     负责驱动各大组件，通过调用各自对外提供的API接口，实现它们之间的交互和协作
     提供整个框架的启动入口
"""


import importlib
import time
from datetime import datetime

from scrapy_plus.conf.default_settings import *

if ASYNC_TYPE == "coroutine":
    from scrapy_plus.utils.coroutine import Pool
elif ASYNC_TYPE == "thread":
    from multiprocessing.dummy import Pool
else:
    raise TypeError("ASYNC_TYPE must be 'thread' or 'coroutine', %s is not supported !!" % str(ASYNC_TYPE))

from .scheduler import Scheduler
from .downloader import Downloader
from scrapy_plus.utils.log import logger
from scrapy_plus.http.request import Request


class Engine(object):
    """引擎"""
    def __init__(self):
        self.spiders = self._auto_import_instances(SPIDERS, True)
        self.scheduler = Scheduler()
        self.downloader = Downloader()
        self.pipelines = self._auto_import_instances(PIPELINES)
        self.spider_mids = self._auto_import_instances(SPIDER_MIDDLEWARES)
        self.downloader_mids = self._auto_import_instances(DOWNLOADER_MIDDLEWARES)
        self.pool = Pool()
        self.total_response = 0
        self.is_running = True

    @staticmethod
    def _auto_import_instances(path, isspider=False):
        """使用importlib导入模块，完成从配置导入类对象的功能"""
        instances = dict() if isspider else list()
        for s in path:
            module_name, class_name = s.rsplit(".", 1)
            classes = importlib.import_module(module_name)
            obj = getattr(classes, class_name)()
            if isspider:
                instances[obj.name] = obj
            else:
                instances.append(obj)
        return instances

    def start(self):
        """程序主入口"""
        start = datetime.now()
        logger.info("开始运行时间：%s" % start)
        self._start_engine()
        stop = datetime.now()
        logger.info("运行结束时间：%s" % stop)
        logger.info("耗时：%.2f" % (stop - start).total_seconds())

    def _start_engine(self):
        """启动引擎"""
        # 分布式、多线程处理
        if ROLE == "master" or ROLE is None:
            self.pool.apply_async(self._execute_start_request)
        if ROLE == "slave" or ROLE is None:
            for i in range(ASYNC_COUNT):
                self.pool.apply_async(self._execute_request_response_item, callback=self._callback)
        while True:
            time.sleep(0.01)
            if self.total_response != 0 and self.total_response == self.scheduler.total_request:
                self.is_running = False
                break
        self.pool.close()
        self.pool.join()
        logger.info("Main Thread is over!")

    def _callback(self, _):
        """循环调用自身"""
        if self.is_running:
            self.pool.apply_async(self._execute_request_response_item, callback=self._callback)

    def _execute_start_request(self):
        """添加请求"""
        for spider in self.spiders.values():
            for start_request in spider.start_requests():
                start_request.spider = spider
                for spider_mid in self.spider_mids:
                    start_request = spider_mid.process_request(start_request)
                self.scheduler.add_request(start_request)

    def _execute_request_response_item(self):
        """发送请求处理响应"""
        request = self.scheduler.get_request()
        if not request:
            return
        spider = request.spider
        for downloader_mid in self.downloader_mids:
            request = downloader_mid.process_request(request)

        response = self.downloader.get_response(request)

        for downloader_mid in self.downloader_mids:
            response = downloader_mid.process_response(response)

        for item_or_request in getattr(spider, request.callback)(response):
            if isinstance(item_or_request, Request):
                item_or_request.spider = request.spider
                for spider_mid in self.spider_mids:
                    item_or_request = spider_mid.process_request(item_or_request)
                self.scheduler.add_request(item_or_request)
            else:
                for spider_mid in self.spider_mids:
                    item_or_request = spider_mid.process_item(item_or_request)
                for pipeline in self.pipelines:
                    item_or_request = pipeline.process_item(item_or_request, spider)
        self.total_response += 1
