# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CryptoItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    change_24h = scrapy.Field()
    volume_24h = scrapy.Field()
    market_cap = scrapy.Field()

    pass
