import scrapy
from ..items import CryptoItem

class CryptoSpiderSpider(scrapy.Spider):
    name = "crypto_spider"
    start_urls = [
        "https://crypto.com/price"
    ]

    def parse(self, response):
        items = CryptoItem()

        name = response.css('.ot-close-icon , .css-rkws3').css('::text').extract()
        price = response.css('.css-13hqrwd::text').extract()
        change_24h = response.css('.css-vtw5vj .chakra-text').css('::text').extract()
        volume_24h = response.css('.css-vtw5vj+ .css-15lyn3l').css('::text').extract()
        market_cap = response.css('.css-15lyn3l+ .css-15lyn3l').css('::text').extract()

        for n, p, c, v, m in zip(name, price, change_24h, volume_24h, market_cap):
            items['name'] = n
            items['price'] = p
            items['change_24h'] = c
            items['volume_24h'] = v
            items['market_cap'] = m
            yield items

        # Handle pagination
        current_page = response.url.split("=")[-1] if "=" in response.url else "1"
        next_page_number = int(current_page) + 1
        next_page = f"https://crypto.com/price?page={next_page_number}"

        # Check if the next page link exists by making a request and checking the response status
        yield scrapy.Request(next_page, callback=self.parse, dont_filter=True)
