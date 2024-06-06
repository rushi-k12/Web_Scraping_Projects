import scrapy
from ..items import AmazonItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = [
        'https://www.amazon.in/s?k=milk&crid=EQSX98FFJY75&sprefix=milk%2Caps%2C203&ref=nb_sb_noss_1'
    ]

    def parse(self, response):
        # Extract data points
        names = response.css('.a-color-base.a-text-normal::text').extract()
        prices = response.css('.a-price-whole::text').extract()
        image_links = response.css('.s-image-optimized-rendering::attr(src)').extract()

        # Iterate over the data and yield each item as a separate record
        for name, price, image_link in zip(names, prices, image_links):
            items = AmazonItem()
            items['name'] = name
            items['price'] = price
            items['image_link'] = image_link
            yield items
