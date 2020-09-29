from scrapy_plus.core.spider import Spider
from scrapy_plus.http.item import Item
from scrapy_plus.http.request import Request


class BaiduSpider(Spider):
    name = "baidu"
    start_urls = ["http://www.baidu.com", "http://news.baidu.com", "http://www.baidu.com"]

    def start_requests(self):
        for start_url in self.start_urls:
            yield Request(start_url, do_filter=False)

    def parse(self, response):
        title = response.xpath("//title/text()")[0]
        yield Item(title)


class DoubanSpider(Spider):
    name = "douban"

    start_urls = ["https://movie.douban.com/top250?start=" + str(i) for i in range(0, 26, 25)]

    def parse(self, response):

        title_list = response.xpath("//div[@class='hd']/a/span[1]/text()")
        yield Item(title_list)
        link_list = response.xpath("//div[@class='hd']/a/@href")
        for link in link_list:
            yield Request(link, callback="parse_page")

    def parse_page(self, response):
        yield Item(response.url)




