# -*- coding: utf-8 -*-
import scrapy
from datetime import datetime, timezone
from scrapy.linkextractors import LinkExtractor
from chapter_8.items import Chapter8ItemRaw
#import json

class SecondScraperSpider(scrapy.Spider):
    name = 'second-scraper'
    allowed_domains = ['jaympatel.com']
    start_urls = ['http://jaympatel.com/']

    def parse(self, response):
        
        
        item = Chapter8ItemRaw()
        
        item['headers'] = str(response.headers)
        item['url'] = response.url
        item['response'] = response.text
        item['crawl_date'] = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        yield item
        
        for a in LinkExtractor().extract_links(response):
            yield response.follow(a, callback=self.parse) 

