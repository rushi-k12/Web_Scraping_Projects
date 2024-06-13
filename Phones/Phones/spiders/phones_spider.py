import scrapy


class PhonesSpiderSpider(scrapy.Spider):
    name = 'phones_spider'
    allowed_domains = ['www.amazon.in']
    start_urls = ['http://www.amazon.in/']

    def parse(self, response):
        pass
