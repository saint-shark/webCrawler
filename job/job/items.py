# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    designation = scrapy.Field()
    company = scrapy.Field()
   #experience = scrapy.Field()
   #location = scrapy.Field()
    skill = scrapy.Field()
    jobDescription = scrapy.Field()
