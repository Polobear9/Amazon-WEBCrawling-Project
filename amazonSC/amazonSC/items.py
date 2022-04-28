# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonscItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Amazon_Brand = scrapy.Field()
    Amazon_Title = scrapy.Field()
    Amazon_Price = scrapy.Field()
    Amazon_Star = scrapy.Field()
    Amazon_review = scrapy.Field()
    Amazon_asin = scrapy.Field()

