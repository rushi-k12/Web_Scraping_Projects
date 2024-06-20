import scrapy
from ..items import WorldGdpItem

class WorldGdpSpider(scrapy.Spider):
    name = 'world_gdp'
    start_urls = [
        'https://www.imf.org/external/datamapper/NGDP_RPCH@WEO/OEMDC/ADVEC/WEOWORLD'
    ]

    def parse(self, response):
        items = WorldGdpItem()

        country=response.css('.dm-ranking-value span:nth-child(1)').css('::text').extract()
        value = response.css('.dm-social , .dm-ranking-value span+ span').css('::text').extract()

        for country, value in zip(country,value):
            items['country'] = country
            items['value'] = value

            yield items