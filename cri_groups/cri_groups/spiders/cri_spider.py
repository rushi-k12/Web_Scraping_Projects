import scrapy
from ..items import CriGroupsItem

class CriSpiderSpider(scrapy.Spider):
    name = 'cri_spider'
    start_urls = [
        'http://www.crigroups.com/'
    ]

    def parse(self, response):
        items = CriGroupsItem()

        products = response.css('#welcome-wrapper a::text').extract()
        contact = response.css('h5 , span , #foot-top h2::text').extract()

        for products, contact in zip(products, contact):
            items['products'] = products
            items['contact'] = contact

            yield items
