# -*- coding: utf-8 -*-
import scrapy
import pytz
import time
import datetime
import re
from Blogcsdn.items import BlogcsdnItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class csdnSpider(CrawlSpider):
    name = "csdn"
    #allowed_domains = ["new.qq.com"]
    #start_urls = [
    #    "https://new.qq.com/ch/tech/"
    #]
    allowed_domains = ["blog.csdn.net"]
    start_urls = [
        "https://blog.csdn.net/slbwgslz/article/details/80493313"
    ]


    rules = (
        Rule(LinkExtractor(
            allow=(r'https://blog.csdn.net/[0-9a-zA-Z_]*?/article/details/[0-9]*?', ),
            #allow=(r'http://new.qq.com/[a-z]*?/2018[0-9]*?/2018[0-9a-zA-Z]*?\.html', ),
            #deny=(r'http://www.mofcom.gov.cn/article/ae/slfw/2018[0-9[0-9]*?/[0-9]*?\.shtml',r'http://www.mofcom.gov.cn/article/ae/ztfbh/2018[0-9]*?/[0-9]*?\.shtml')
            ),
            callback='parse_checktencentnew',follow=True),

        #Rule(LinkExtractor(allow=('http://new.qq.com/[a-z]*?/2018[0-9]*?/2018[0-9a-zA-Z]*?\.html')),
        #     follow=True),
    )

    def parse_checktencentnew(self,response):
        self.tz = pytz.timezone('Asia/Shanghai')
        #item['timestamp'] = datetime.datetime.now(tz=self.tz).strftime('%Y_%m_%d_%H_%M_%S')
        item = BlogcsdnItem()
        item['link'] = response.url
        #item['title'] = response.xpath('//html/body/div[@class="qq_conent clearfix"]/div[@class="LEFT"]/h1/text()').extract_first()
        #sel = response.xpath('//div[@class="content-article"]').xpath('string(.)').extract_first().strip()
        
        item['title'] = response.xpath('//html/body/div[@class="container clearfix"]/main/div[@class="blog-content-box"]/div[@class="article-header-box"]/div[@class="article-header"]/div[@class="article-title-box"]/h1/text()').extract_first()
        sel = response.xpath('//div[@class="markdown_views"]').xpath('string(.)').extract_first().strip()
        
        #contents = response.xpath('//html/body/script').extract()[0].split('\n\t\t')
        #item['timestamp'] = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
        item['timestamp'] = datetime.datetime.now(tz=self.tz).strftime('%Y_%m_%d_%H_%M_%S')
        #for content in contents:
        #    content.strip()
        #    if "var tm" in content:
                #print content
        #        item['time'] = re.findall(r"\"(.*)\"",content)[0].replace('-','_').replace(':','_').replace(' ','_')
                # print item['time']
        #        break
        #    else:
        item['time'] = item['timestamp']

        item['desc'] = sel
        #item['keyword'] = ""
        yield item
