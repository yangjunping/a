# -*- coding: utf-8 -*-
import scrapy


class FriendSpider(scrapy.Spider):
    name = 'friend'
    allowed_domains = ['https://www.toutiao.com/c/user/5394099443/#mid=5394099443']
    start_urls = ['http://https://www.toutiao.com/c/user/5394099443/#mid=5394099443/']

    def parse(self, response):
        pass
