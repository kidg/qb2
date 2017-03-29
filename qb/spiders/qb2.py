# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Qb2Spider(CrawlSpider):
    name = 'qb2'
    # allowed_domains = ['www.qiushibaike.com']
    start_urls = ["http://www.qiushibaike.com/", ]

    rules = (
        Rule(LinkExtractor(allow=r'/article/*')),
        Rule(LinkExtractor(allow=r'/users/*'),callback='parse_result'),
    )

    def parse_result(self, response):
        print response.xpath('//div[@class="user-header-cover"]/h2/text()').extract()[0]
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i

