"""
五大核心组件：管道组件
     负责处理数据对象(Item)
"""

from scrapy_plus.utils.log import logger


class Pipeline(object):
    """管道"""
    def process_item(self, item, spider):
        logger.info("Item: {}".format(item.data))
