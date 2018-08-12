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

from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
from scrapy.crawler import Settings as settings
class MysqlPipeline(object):
    def __init__(self):
        dbargs = dict(
            host = '192.168.51.79' ,
            db = 'test',
            user = 'root', #replace with you user name
            passwd = 'sz1544', # replace with you password
            charset = 'utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode = True,
            )    
        self.dbpool = adbapi.ConnectionPool('MySQLdb',**dbargs)
    def process_item(self, item,spider):
        res = self.dbpool.runInteraction(self.insert_into_table,item)
        return item
    def insert_into_table(self,conn,item):
        conn.execute('insert into tencentnews(title,link,descs,timestamps,times) values(%s,%s,%s,%s,%s)', (item['title'],item['link'],item['desc'],item['timestamp'],item['time']))