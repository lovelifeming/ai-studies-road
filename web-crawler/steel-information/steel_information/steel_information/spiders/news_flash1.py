#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : news_flash
import time

import scrapy

from items import SteelInfoItem


class NewsFlash(scrapy.Spider):
    name = 'ganggu'
    allowed_domains = ['news.gangguwang.com']
    start_urls = ['http://news.gangguwang.com/fastnews/fastnews?typeText=all&city=0']
    website_url = 'http://news.gangguwang.com/fastnews/fastnews?typeText=all&city=0'
    website_name = '钢谷网'

    def parse(self, response):
        """ yield item  提交给管道文件处理 pipelines
            yield scrapy.Request( next_url, callback=self.parse)   提交子请求，回调递归处理
            response.urljoin()   拼凑成绝对网址
        """
        ymd_str = response.xpath('/html/body/div[3]/div[3]/div/div[2]/div[1]/h2/a/text()').extract_first()

        for i in range(1, 200):
            hm_p = '/html/body/div[3]/div[3]/div/div[2]/div[1]/div/ul/li[' + str(i) + ']/p/text()'
            hm = response.xpath(hm_p).extract_first()
            content_p = '/html/body/div[3]/div[3]/div/div[2]/div[1]/div/ul/li[' + str(i) + ']/div/div[2]/p/text()'
            content = response.xpath(content_p).extract_first()
            id_p = '/html/body/div[3]/div[3]/div/div[2]/div[1]/div/ul/li[' + str(i) + ']/div/a/@id';
            news_id = response.xpath(id_p).extract_first()
            if hm is None or content is None or news_id is None:
                break
            ymd = time.strptime(ymd_str + hm, '%Y年%m月%d日%H:%M')
            publisherTime = time.strftime('%Y-%m-%d %H:%M:%S', ymd)
            yield SteelInfoItem(news_id=news_id, title_name=None, notes=None,
                                texts=content, publish_time=publisherTime,
                                website_url=self.website_url, website_name=self.website_name, response=response)
