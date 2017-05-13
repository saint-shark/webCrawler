from scrapy import Spider
from scrapy.selector import Selector
from job.items import JobItem



class jobSpider(Spider):

    name = "job"
    allowedDomain = ["https://www.naukri.com"]
    start_urls = ["https://www.naukri.com/jobs-in-raipur","https://www.naukri.com/jobs-in-raipur-2"]


    def parse(self, response):

        jobs = response.css('.content')
        for job in jobs:
            item = JobItem()
            item['designation'] = job.css('.desig::text').extract()[0]
            item['company'] = job.css('.org::text').extract()[0]
            item['skill'] = job.css('.skill::text').extract()[0]
            item['jobDescription'] = job.css('.desc::text').extract()[0]
            yield item
#
# for job in response.css('.content'):
# ...     desig = job.css('.desig::text').extract()
# ...     comp = job.css('.org::text').extract()
# ...     location = job.css('.loc::text').extract()
# ...     skills = job.css('.skill::text').extract()
# ...     description = job.css('.desc::text').extract()
# ...     print(dict(designation = desig, company = comp, location = location, skills = skills, decription = description))
