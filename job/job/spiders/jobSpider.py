from scrapy import Spider
from scrapy.selector import Selector
from job.items import JobItem



class stackSpider(Spider):

    name = "job"
    allowedDomain = ["https://www.naukri.com"]
    start_urls = ["https://www.naukri.com/jobs-in-raipur"]


    def parse(self, response):

        jobs = Selector(response).xpath('//div[@class="row  "]/a')
        for job in jobs:
            item = JobItem()
            item['designation'] = job.xpath(
                'ul/li[@class="desig"]/text()').extract()[0]
            item['company'] = job.xpath(
                'span[@class="org"]/text()').extract()[0]
            item['experience'] = job.xpath(
                'span[@class="exp"]/text()').extract()[0]
            item['location'] = job.xpath(
                'span/span[@class="loc"]/text()').extract()[0]
            item['skill'] = job.xpath(
                'div/div[@class="skill"]/text()').extract()[0]
            item['jobDescription'] = job.xpath(
                'div/span[@class="desc"]/text()').extract()[0]
            yield item
