import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class BCorpItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    website = scrapy.Field()
    bscore = scrapy.Field()
    location = scrapy.Field()
    description = scrapy.Field()


class BCorpSpider(CrawlSpider):
    name = 'bcorp'
    allowed_domains = ['bcorporation.net']
    start_urls = ['https://www.bcorporation.net/community/find-a-b-corp?page=1']
    rules = (Rule(LinkExtractor(allow=['/community/'], deny=['find-a-b-corp']), 'parse_bcorp'),
            Rule(LinkExtractor(allow=['/community/find-a-b-corp']), follow=True))

    def parse_bcorp(self, response):
        bcorp = BCorpItem()
        bcorp['url'] = response.url
        bcorp['name'] = response.xpath('//*[@id="page-title"]/text()').extract()[0].strip()
        bcorp['website'] = response.xpath('//*[contains(concat( " ", @class, " "  ), concat( " ", "company-desc-inner", " "  ))]//a/text()').extract()[0].strip()
        bcorp['bscore'] = int(response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "field-name-field-overall-b-score", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "even", " " ))]/text()').extract()[0].strip())
        temp_desc = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "field-label-hidden", " " ))]//p/text()').extract()
        if temp_desc:
            bcorp['description'] = temp_desc[0].strip()

        return bcorp
