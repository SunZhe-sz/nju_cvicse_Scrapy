# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json
import codecs
from collections import OrderedDict

class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file = codecs.open('newqq.data_utf8.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(OrderedDict(item), ensure_ascii=False, sort_keys=False) + "\n"
        self.file.write(line)
        #print line
        return item
    def close_spider(self, spider):
        self.file.close()
        
from scrapy.exceptions import DropItem            
class DuplicatesPipeline(object):
    def __init__(self):
        self.links_seen = list()
    def process_item(self, item, spider):
        if item['title'] in self.links_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.links_seen.append(item['title'])
            return item
