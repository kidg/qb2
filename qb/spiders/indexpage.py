# -*- coding:utf8 -*-

import scrapy
from qb.items import QbItem

class QiuBaiSpider(scrapy.Spider):
    name ="qb"
    start_urls = ["http://www.qiushibaike.com/", ]

    def parse(self, response):
        #from scrapy.shell import inspect_response
        #inspect_response(response, self)
        pattern1 = '//div[@class="article block untagged mb15"]'
        pattern2 = './div[@class="author clearfix"]/a[2]/h2/text()'
        pattern3 = './a/div[@class="content"]/span/text()'

        for ele in response.xpath(pattern1):
            authors = ele.xpath(pattern2).extract()
            contents = ele.xpath(pattern3).extract()
            yield QbItem(author=authors, content=contents)


