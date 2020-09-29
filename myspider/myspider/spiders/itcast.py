import scrapy
from myspider.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Host": "www.itcast.cn",
                "Pragma": "no-cache",
                "Referer": "http://www.itcast.cn/channel/teacher.shtml",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}

    # headers里面填写cookie无效需要单独传
    cookies = {"UM_distinctid": "174b0e74dc31a-08c8ad0d0f1cfb-333769-1fa400-174b0e74dc4b21",
                "bad_idb2f10070-624e-11e8-917f-9fb8db4dc43c": "5ec55b51-fc10-11ea-bc6d-950d3b807946",
                "parent_qimo_sid_b2f10070-624e-11e8-917f-9fb8db4dc43c": "62c75b90-fc10-11ea-be8d-c9760f1b6837",
                "CNZZDATA4617777": "cnzz_eid%3D1150870002-1600692223-%26ntime%3D1600874221",
                "Hm_lvt_0cb375a2e834821b74efffa6c71ee607": "1600695783,1600874895",
                "Hm_lpvt_0cb375a2e834821b74efffa6c71ee607": "1600874895",
                "qimo_seosource_b2f10070-624e-11e8-917f-9fb8db4dc43c": "%E7%AB%99%E5%86%85",
                "qimo_seokeywords_b2f10070-624e-11e8-917f-9fb8db4dc43c": "",
                "href": "http%3A%2F%2Fwww.itcast.cn%2Fchannel%2Fteacher.shtml%23ajavaee",
                "accessId": "b2f10070-624e-11e8-917f-9fb8db4dc43c",
                "pageViewNum": "1",
                "nice_idb2f10070-624e-11e8-917f-9fb8db4dc43c": "66d1ddd1-fdb1-11ea-bd67-2bc60c7980d8"}

    def start_requests(self):

        # 使用scrapy发送post请求登录
        # yield scrapy.FormRequest(url='', formdata={}, callback=self.parse)

        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers, cookies=self.cookies, dont_filter=True)

    def parse(self, response, **kwargs):
        node_list = response.xpath("//div[@class='li_txt']")
        for node in node_list:
            item = ItcastItem()
            item['name'] = node.xpath("./h3/text()").extract_first()
            item['title'] = node.xpath("./h4/text()").extract_first()
            item['info'] = node.xpath("./p/text()").extract_first()
            yield item




