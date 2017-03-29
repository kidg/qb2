# -*- coding:utf8 -*-

import scrapy
from qb.items import QbItem
from scrapy.http import Request

class QiuBaiSpider(scrapy.Spider):
    name ="qb"
    start_urls = ["http://www.qiushibaike.com/", ]

    def parse(self, response):

        pattern4 = '//span[@class="stats-comments"]/a/@href'

        for href in response.xpath(pattern4).extract():    #OK
            full_url = response.urljoin(href)
            # print full_url
            req = Request(full_url, self.parse_detail_page)
            item = QbItem()
            req.meta["item"] = item
            yield req

    def parse_detail_page(self, response):

        pattern1 = '//div[@class="article block untagged mb15"]'
        pattern2 = '//div[@class="author clearfix"]/a[2]/h2/text()'
        pattern3 = '//div[@class="content"]/text()'

        pattern4 = '//span[@class="stats-comments"]/a/@href'

        pattern5 = '//div[starts-with(@class,"comment-block clearfix")]'
        pattern6 = './div[@class="replay"]/a/text()'
        pattern7 = './div[@class="replay"]/span/text()'

        item = response.meta["item"]
        item["author"] = response.xpath(pattern2).extract()[0]   #OK
        item["content"] = response.xpath(pattern3).extract()[0]    #OK
        comments = []
        for comment in response.xpath(pattern5):    #OK
            # print comment
            comment_author = comment.xpath(pattern6).extract()[0]  #OK
            comment_content = comment.xpath(pattern7).extract()[0]  #OK
            # print comment_author, comment_content
            comments.append({"comment_author":comment_author, "comment_content": comment_author})
        item["comments"] = comments
        yield item







