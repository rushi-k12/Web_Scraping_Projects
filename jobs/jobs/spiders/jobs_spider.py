import scrapy
from ..items import JobsItem

class JobsSpiderSpider(scrapy.Spider):
    name = 'jobs_spider'
    start_urls = [
        'https://www.naukri.com/data-scientist-jobs-in-india?k=data%20scientist&l=india&nignbevent_src=jobsearchDeskGNB'
    ]

    def parse(self, response):
        items = JobsItem()

        title = response.css('.title::text').extract()
        company = response.css('.comp-name::text').extract()
        experience = response.css('.expwdth::text').extract()
        location = response.css('.locWdth::text').extract()


        for title, company, experience,location in zip(title, company, experience,location):
            items['title'] = title
            items['company'] = company
            items['experience'] = experience
            items['location'] = location

            yield items