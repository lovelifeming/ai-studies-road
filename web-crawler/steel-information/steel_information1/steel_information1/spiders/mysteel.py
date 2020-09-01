#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/31 16:25
# @File : mysteel
import json
import re
import time

import scrapy

from items import SteelInfo1Item
from settings import STEEL_KEYWORD, METAL_KEYWORD


class MySteel(scrapy.Spider):
    name = 'mysteel'
    allowed_domains = ['mysteel.com']
    start_urls = ['https://list1.mysteel.com/article/p-3817-------------1.html']
    website_url = 'http://list1.mysteel.com/article/p-318-------------1.html'
    website_name = '我的钢铁-综合资讯-宏观'
    custom_settings = {'ITEM_PIPELINES': {'steel_information1.pipelines.SteelInformation1Pipeline': 300,
                                          'steel_information1.pipelines.SaveImagePipeline': 500, }}

    def parse(self, response):
        """ yield item  提交给管道文件处理 pipelines
            yield scrapy.Request( next_url, callback=self.parse)   提交子请求，回调递归处理
            response.urljoin()   拼凑成绝对网址
        """
        print(response)
        text_json = json.loads(response.text)
        url = response.url
        if 'list1' in url:
            last_ts = None
            for i in range(1, 100):
                title = response.xpath('/html/body/div[2]/div[1]/ul[1]/li['+i+']/h3/a/@title').extract_first()
                notes = response.xpath('/html/body/div[2]/div[1]/ul[1]/li['+i+']/div/text()').extract_first()
                last_ts = response.xpath('/html/body/div[2]/div[1]/ul[1]/li['+i+']/p/text()').extract_first()
                source_url = response.xpath('/html/body/div[2]/div[1]/ul[1]/li['+i+']/div/a/@href').extract_first()
                if (len(re.findall(STEEL_KEYWORD, title)) > 0 or len(re.findall(STEEL_KEYWORD, notes)) > 0 or
                        len(re.findall(METAL_KEYWORD, notes)) > 0 or len(re.findall(METAL_KEYWORD, notes)) > 0):
                    time.sleep(3)
                    yield scrapy.Request(source_url, callback=self.parse)
                    yield SteelInfo1Item()
            if last_ts is not None and (time.time() - time.mktime(time.strptime(last_ts, '%Y-%m-%d %H:%M'))) < 3600:
                next_url = response.xpath('/html/body/div[2]/div[1]/div[1]/div[1]/a[8]/@href').extract_first()
                yield scrapy.Request(next_url, callback=self.parse)
        else:
            yield SteelInfo1Item()

