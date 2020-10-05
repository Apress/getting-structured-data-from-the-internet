# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from chapter_8.items import Chapter8Item

class LinkscraperBasicSpider(scrapy.Spider):
    name = 'linkscraper-basic'
    allowed_domains = ['jaympatel.com']
    start_urls = ['http://jaympatel.com/']

    def parse(self, response):
 
            item = Chapter8Item()
            if response.headers["Content-Type"] == b'text/html; charset=utf-8' or response.headers["Content-Type"] == b'text/html':
                soup = BeautifulSoup(response.text,'html.parser')
                urls = soup.find_all('a', href=True)
                for val in soup.find_all('title'):
                    try:
                        item["url"] = response.url
                        item["title"] = val.get_text()
                        item["depth"] = str(response.meta['depth'])
                        yield item
                    except Exception as E:
                        print(str(E))
                
            else:
                item["title"] = 'title not extracted since content-type is ' + str(response.headers["Content-Type"])
                item["url"] = response.url
                item["depth"] = str(response.meta['depth'])
                urls = []
                yield item
            
            
            
            for url in urls:
                yield response.follow(url['href'], callback=self.parse)
