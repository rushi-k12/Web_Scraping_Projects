import scrapy
from ..items import PhonesItem

class PhonesSpiderSpider(scrapy.Spider):
    name = 'phones_spider'
    start_urls = [
        'https://www.amazon.in/s?k=phones&crid=22JM18NEVYB24&sprefix=phone%2Caps%2C335&ref=nb_sb_noss_1'
    ]

    def parse(self, response):
        items = PhonesItem()
        products = response.css('.s-main-slot .s-result-item')

        print(f"Found {len(products)} products")  # Debugging statement

        def parse(self, response):
            products = response.css('.s-main-slot .s-result-item')

            print(f"Found {len(products)} products")  # Debugging statement

            for product in products:
                item = PhonesItem()
                item['name'] = product.css('h2 .a-text-normal::text').get()
                item['review'] = product.css('.a-size-base.s-underline-text::text').get() or "No reviews"

                yield item
