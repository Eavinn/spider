import scrapy
from redis_spider.items import AqiItem
from scrapy_redis.spiders import RedisSpider


class AqiSpider(RedisSpider):
    name = "aqispider"
    allowed_domains = ["aqistudy.cn"]

    base_url = "https://www.aqistudy.cn/historydata/"
    # start_urls = [base_url]
    redis_key = "aqispider:start_urls"

    def parse(self, response, **kwargs):
        """
            解析响应，提取所有城市链接，并发送请求，由parse_month解析
        """
        city_link_list = response.xpath("//div[@class='all']//a/@href").extract()
        city_name_list = response.xpath("//div[@class='all']//a/text()").extract()

        for link, name in list(zip(city_link_list, city_name_list))[10:11]:
            yield scrapy.Request(self.base_url + link, meta={"city": name}, callback=self.parse_month)

    def parse_month(self, response, **kwargs):
        """
            解析每个城市响应，提取所有月份的链接，并发送请求，由parse_day解析
        """
        month_link_list = response.xpath("//tbody//a/@href").extract()

        for link in month_link_list[10:11]:
            yield scrapy.Request(self.base_url + link, meta=response.meta, callback=self.parse_day)

    def parse_day(self, response, **kwargs):

        city_name = response.meta['city']
        node_list = response.xpath("//tbody/tr")
        node_list.pop(0)

        for node in node_list:
            item = AqiItem()
            item['city'] = city_name
            item['date'] = node.xpath("./td[1]/text()").extract_first()
            item['aqi'] = node.xpath("./td[2]/text()").extract_first()
            item['level'] = node.xpath("./td[3]/span/text()").extract_first()
            item['pm2_5'] = node.xpath("./td[4]/text()").extract_first()
            item['pm10'] = node.xpath("./td[5]/text()").extract_first()
            item['so2'] = node.xpath("./td[6]/text()").extract_first()
            item['co'] = node.xpath("./td[7]/text()").extract_first()
            item['no2'] = node.xpath("./td[8]/text()").extract_first()
            item['o3'] = node.xpath("./td[9]/text()").extract_first()
            yield item








