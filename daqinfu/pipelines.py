# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter
import json
class DaqinfuPipeline:
    def __init__(self):
        self.fp = open("comments.json", 'w', encoding='utf-8')
    def process_item(self, item, spider):
        self.fp.write(json.dumps(dict(item))+"\n")
        return item
    def close_spider(self,spider):
        self.fp.close()
