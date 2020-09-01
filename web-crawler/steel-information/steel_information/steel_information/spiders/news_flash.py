#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : news_flash
import json
import os
import sys
import time

import scrapy

from items import SteelInfoItem

class NewsFlash(scrapy.Spider):
    name = 'mysteel'
    allowed_domains = ['mysteel.com']
    start_urls = ['https://www.mysteel.com/activity/api/newsflash/flashnews/query_newsflash.htm?'
                  'pageNo=1&sectionId=&categoryId=&pageSize=30']
    website_url = 'https://www.mysteel.com/fastcomment/#/'
    website_name = '我的钢铁'

    def parse(self, response):
        """ yield item  提交给管道文件处理 pipelines
            yield scrapy.Request( next_url, callback=self.parse)   提交子请求，回调递归处理
            response.urljoin()   拼凑成绝对网址
        """
        text_json = json.loads(response.text)
        data_list = text_json['list']
        for it in data_list:
            publisherTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(it['publisherTime'] / 1000)))

            yield SteelInfoItem(news_id=it['id'], title_name=it['categoryName'], notes=it['sectionName'],
                                texts=it['content'], publish_time=publisherTime,
                                website_url=self.website_url, website_name=self.website_name, response=response)
        last_data = data_list[-1]
        second = time.time() - last_data['publisherTime'] / 1000
        page_no = text_json['pageNo']
        if second < 1800:
            next_page = str.replace(self.start_urls[0], 'pageNo=' + str(page_no), 'pageNo=' + str(page_no + 1))
            time.sleep(1000)
            yield scrapy.Request(next_page, self.parse)
