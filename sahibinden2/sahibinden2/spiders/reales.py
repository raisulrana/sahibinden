import scrapy
from scrapy.http.request import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule



class RealesSpider(CrawlSpider):
    name = 'reales'
    allowed_domains = ['www.sahibinden.com']
    start_urls = ['https://www.sahibinden.com/satilik/istanbul-eyupsultan?pagingOffset=220']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//td[@class='searchResultsTitleValue ']/a[1]"), callback='parse_item'),    
    )
    # Rule(LinkExtractor(restrict_xpaths="//div[@class='pageNavTable']/ul/li[15]/a"), callback='parse_item', follow=True),

    def parse_item(self, response):
        yield {
            'URL': response.url,
            # 'Response': response,
            # 'Response Text': response.text,
            'City': response.xpath("normalize-space(//div[@class='classifiedInfo ']/h2/a[1]/text())").get(),
            'County': response.xpath("normalize-space(//div[@class='classifiedInfo ']/h2/a[2]/text())").get(),
            'District': response.xpath("normalize-space(//div[@class='classifiedInfo ']/h2/a[3]/text())").get(),
            'Listing Date': response.xpath("normalize-space(//div[@class='classifiedInfo ']/ul/li[2]/span/text())").get(),
            'Gross': response.xpath("normalize-space(//div[@class='classifiedInfo ']/ul/li[4]/span/text())").get(),
            'Net': response.xpath("normalize-space(//div[@class='classifiedInfo ']/ul/li[5]/span/text())").get(),
            '# Rooms': response.xpath("normalize-space(//div[@class='classifiedInfo ']/ul/li[6]/span/text())").get(),
            '# Living Rooms': response.xpath("normalize-space(//div[@class='classifiedInfo ']/ul/li[6]/span/text())").get(),
            'Building Age': response.xpath("normalize-space(//div[@class='classifiedInfo ']/ul/li[7]/span/text())").get(),
            'Floor': response.xpath("normalize-space(//div[@class='classifiedInfo ']/ul/li[9]/span/text())").get(),
            '# Floors': response.xpath("normalize-space(//div[@class='classifiedInfo ']/ul/li[9]/span/text())").get(),
            '# Bathrooms': response.xpath("normalize-space(//div[@class='classifiedInfo ']/ul/li[11]/span/text())").get(),
            'Type of Property': response.xpath("normalize-space(//div[@class='classifiedInfo ']/ul/li[3]/span/text())").get(),
            'From Who?': response.xpath("normalize-space(//div[@class='classifiedInfo ']/ul/li[20]/span/text())").get(),
            'Title Deed': response.xpath("normalize-space(//div[@class='classifiedInfo ']/ul/li[19]/span/text())").get(),
            'Price': response.xpath("normalize-space(//div[@class='classifiedInfo ']/h3/text())").get()
        }
