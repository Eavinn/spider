# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import json
import pymongo
from datetime import datetime
from scrapy.exporters import CsvItemExporter


class AqiPipeline(object):
    def process_item(self, item, spider):
        item['time'] = str(datetime.utcnow())
        item['source'] = spider.name
        return item


class AqiJsonPipeline(object):
    """item转存为json文化部"""
    def open_spider(self, spider):
        self.f = open("aqi.json", "a")

    def process_item(self, item, spider):
        content = json.dumps(dict(item)) + ",\n"
        self.f.write(content)
        return item

    def close_spider(self, spider):
        self.f.close()


class AqiCsvPipeline(object):
    """item转存为csv文件"""
    def open_spider(self, spider):
        self.f = open("aqi.csv", "ab")
        self.csv_exporter = CsvItemExporter(self.f)
        self.csv_exporter.start_exporting()

    def process_item(self, item, spider):
        self.csv_exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.csv_exporter.finish_exporting()
        self.f.close()


class AqiMongoPipeline(object):
    """item转存为MongoDB文件"""
    def open_spider(self, spider):
        self.client = pymongo.MongoClient('mongodb://meng:ml6666@192.168.49.153:27017')
        self.collection = self.client['AQI_DATA']['aqi']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
