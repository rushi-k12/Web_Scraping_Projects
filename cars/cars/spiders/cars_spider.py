import scrapy
from ..items import CarsItem

class CarsSpiderSpider(scrapy.Spider):
    name = 'cars_spider'
    start_urls = ['https://www.cardekho.com/used-cars+in+hyderabad']

    def parse(self, response):
        items = CarsItem()

        name=response.css('#carList-0 a::text').extract()
        price=response.css('#carList-0 p::text').extract()
        image_link=response.css('.imagebox img::attr(src)').extract()
        details=response.css('.dotsDetails::text').extract()

        for name, price, image_link , details in zip(name, price, image_link, details):

            items['name']=name
            items['price']=price
            items['image_link']=image_link
            items['details']=details

            yield items

