from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from myspider.items import XiurenItem


class TencentCrawlSpider(CrawlSpider):
    name = "xiuren"
    allowed_domains = ["xiurenji.com"]

    # 第一批从start_urls发送，返回响应默认经过所有的Rule提取，但是没有回调函数解析数据
    start_urls = ['https://www.xiurenji.com/MyGirl/5607.html']

    rules = [Rule(LinkExtractor(allow=r"/MyGirl/5607\w+\.html"), callback="parse_page", follow=True),
             # Rule(LinkExtractor(allow=r"/uploadfile/[\d/]+\.jpg", deny_extensions=['mp4'], tags=['img'], attrs='src'), callback="parse_page", follow=False),
             ]

    def parse_page(self, response, **kwargs):
        node_list = response.xpath("//div[@class='img']/p/img")
        for node in node_list:
            item = XiurenItem()
            item["title"] = node.xpath("./@alt").extract_first()
            src = node.xpath("./@src").extract_first()
            if src:
                item["image_urls"] = ["https://img.xiurenji.com" + src.replace("/uploadfile", "/Uploadfile")]
            yield item


