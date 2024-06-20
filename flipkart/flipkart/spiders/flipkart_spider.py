import scrapy
from ..items import FlipkartItem

class FlipkartSpiderSpider(scrapy.Spider):
    name = 'flipkart_spider'
    start_urls = [
        'https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    ]


    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'ROBOTSTXT_OBEY': True,
        'RETRY_TIMES': 5,
        'DOWNLOAD_DELAY': 2
    }

    def parse(self, response):
        items = FlipkartItem()

        name = response.css('.KzDlHZ::text').extract()
        price = response.css('._4b5DiR::text').extract()

        for name, price in zip(name, price):
            items['name'] = name
            items['price'] = price

            yield items