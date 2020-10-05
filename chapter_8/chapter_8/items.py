# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Chapter8Item(scrapy.Item):
# Listing 8-4: items.py fields
    url = scrapy.Field()
    title = scrapy.Field()
    depth = scrapy.Field()
    
# Listing 8-10: Modifying items.py file to capture raw web crawl data

class Chapter8ItemRaw(scrapy.Item):
    headers = scrapy.Field()
    url = scrapy.Field()
    response = scrapy.Field()
    crawl_date = scrapy.Field()
    