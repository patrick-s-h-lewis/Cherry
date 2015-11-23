# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


import scrapy


class DoiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    doi = scrapy.Field()
    cross_ref_doi = scrapy.Field()
    title = scrapy.Field()