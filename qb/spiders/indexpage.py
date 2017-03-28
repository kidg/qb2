# -*- coding:utf8 -*-

import scrapy


class QiuBaiSpider(scrapy.Spider):
    name ="qb"
    start_urls = ["http://www.qiushibaike.com/", ]

    def parse(self, response):
        from scrapy.shell import inspect_response
        inspect_response(self, response)
        print response.xpath('//div[@class="content"]').extract()
