# -*- coding: utf-8 -*-
import scrapy
#from example.items import ExampleItem

class WebSpider(scrapy.Spider):
    name = 'web'
    allowed_domains = ['https://www.imdb.com/list/ls002913270/']
    start_urls = ['https://www.imdb.com/list/ls002913270/']

    def parse(self, response):
        #for post in response.css('div.lister list detail sub-list'):
            name = response.css('.lister-item-header a::text').extract()
            name = [names.strip() for names in name]
            name = [names for names in name if name!='\n']

            works = response.css('p.text-muted.text-small::text').extract()
            works = [work.strip() for work in works]
            works = [work for work in works if work != '']

            biography = response.css('.text-small+ p::text').extract()
            biography = [bio.strip() for bio in biography]
            biography = [bio for bio in biography if bio !='\n']

            image = response.css('img').extract()
            image = [images.strip() for images in image]
            image = [images for images in image if image !=["img"]]


            #print(dict(name=name,profession=profession,biography=biography))

            for item in zip(name,works,biography,image):

                info = {
                    'Name' : item[0],
                    'Profession' : item[1],
                    'Biography' : item[2],
                    'Image' : item[3],
                }
                yield info


