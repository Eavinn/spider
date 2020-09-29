# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from PIL import Image
from io import BytesIO
from scrapy.pipelines.images import ImagesPipeline

from myspider.items import ItcastItem, TencentItem

from itemadapter import ItemAdapter


class ItcastPipeline(object):

    def open_spider(self, spider):
        """爬虫启动时执行一次"""
        self.f = open("./data/itcast.json", "w")

    def process_item(self, item, spider):
        """处理每一个item数据"""
        if isinstance(item, ItcastItem):
            content = json.dumps(dict(item), ensure_ascii=False) + ',\n'
            self.f.write(content)
        return item

    def close_spider(self, spider):
        """爬虫关闭时执行一次"""
        self.f.close()


class TencentPipeline(object):

    def open_spider(self, spider):
        """爬虫启动时执行一次"""
        self.f = open("./data/tencent.json", "w")

    def process_item(self, item, spider):
        """处理每一个item数据"""
        if isinstance(item, TencentItem):
            content = json.dumps(dict(item), ensure_ascii=False) + ',\n'
            self.f.write(content)
        return item

    def close_spider(self, spider):
        """爬虫关闭时执行一次"""
        self.f.close()


class XiurenPipeline(ImagesPipeline):

    def __init__(self, store_uri, download_func=None, settings=None):
        super().__init__(store_uri, download_func, settings)
        self.dir_name = None

    def get_media_requests(self, item, info):
        self.dir_name = item["title"]
        return super().get_media_requests(item, info)

    def convert_image(self, image, size=None):
        if image.format == 'PNG' and image.mode == 'RGBA':
            background = Image.new('RGBA', image.size, (255, 255, 255))
            background.paste(image, image)
            image = background.convert('RGB')
        elif image.mode == 'P':
            image = image.convert("RGBA")
            background = Image.new('RGBA', image.size, (255, 255, 255))
            background.paste(image, image)
            image = background.convert('RGB')
        elif image.mode != 'RGB':
            image = image.convert('RGB')

        if size:
            image = image.copy()
            image.thumbnail(size, Image.ANTIALIAS)

        buf = BytesIO()
        # 复写方法，修改图片质量，dpi=(300.0, 300.0)
        image.save(buf, 'JPEG', quality=95)
        return image, buf

    def file_path(self, request, response=None, info=None):
        """复写方法修改存储路径"""
        img_path = super().file_path(request, response, info)
        return img_path.replace("full",  self.dir_name)

    def item_completed(self, results, item, info):
        return super().item_completed(results, item, info)




