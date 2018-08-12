# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentnewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    #keyword = scrapy.Field()
    timestamp = scrapy.Field()
    #source = scrapy.Field()
    #name = scrapy.Field()
    #content = scrapy.Field()
    #num = scrapy.Field()
    time = scrapy.Field()
    pass
