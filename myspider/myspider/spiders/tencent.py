import json
import scrapy

from myspider.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = "tencent"
    allowed_domains = ["careers.tencent.com"]

    base_url = "https://careers.tencent.com/tencentcareer/api/post/Query?pageSize=10&pageIndex="
    set_pageindex = 1
    start_urls = [base_url + str(set_pageindex)]

    def parse(self, response, **kwargs):

        content = json.loads(response.body.decode())
        jobs = content["Data"]["Posts"]
        if not jobs:
            return
        for job in jobs:
            item = TencentItem()
            item["title"] = job["RecruitPostName"]
            item["position"] = job["CategoryName"]
            item["publish_date"] = job["LastUpdateTime"]
            yield item
        self.set_pageindex += 1
        next_url = self.base_url + str(self.set_pageindex)
        yield scrapy.Request(next_url, callback=self.parse)
