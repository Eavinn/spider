

class SpiderMiddlewareFirst(object):
    def process_request(self, request):
        print("Request经过爬虫中间件1")
        return request

    def process_item(self, item):
        print("Item经过爬虫中间件1")
        return item


class SpiderMiddlewareSecond(object):
    def process_request(self, request):
        print("Request经过爬虫中间件2")
        return request

    def process_item(self, item):
        print("Item经过爬虫中间件2")
        return item


class DownloadMiddlewareFirst(object):
    def process_request(self, request):
        print("Request经过下载中间件1")
        return request

    def process_response(self, response):
        print("Response经过下载中间件1")
        return response


class DownloadMiddlewareSecond(object):
    def process_request(self, request):
        print("Request经过下载中间件2")
        return request

    def process_response(self, response):
        print("Response经过下载中间件2")
        return response