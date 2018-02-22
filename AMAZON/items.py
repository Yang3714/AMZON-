# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):      #继承scrapy.Item，通过这个Item把爬取的内容发给pipelines
    # define the fields for your item here like:
    #定义字段
    name = scrapy.Field()
    price=scrapy.Field()
    dis=scrapy.Field
