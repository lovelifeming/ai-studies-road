#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : news_flash
import json
import time

import pymysql
import scrapy

from items import SteelInformationItem


class NewsFlash(scrapy.Spider):
    name = 'ganggu'
    allowed_domains = ['news.gangguwang.com']
    start_urls = ['http://news.gangguwang.com/fastnews/fastnews?typeText=all&city=0']

    def parse(self, response):
        print(response)
        ymd = response.xpath('/html/body/div[3]/div[3]/div/div[2]/div[1]/h2/a/text()')
        val_map = []
        for i in 1000:
            tm = response.xpath('/html/body/div[3]/div[3]/div/div[2]/div[1]/div/ul/li['+i+']/p/text()').extract_first()
            content = response.xpath('/html/body/div[3]/div[3]/div/div[2]/div[1]/div/ul/li['+i+']/div/div[2]/p/text()').extract_first()
            if(tm is None or content is None):
                break
            val_map.append()

        sql_many = "replace  INTO `jiwei_xn_index_test`.`p_ifm_announce_bigdata`" \
                   "(`news_id`, `title_name`, `notes`, `texts`,`publish_time`, `website`, `website_name`,create_time)" \
                   " VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "


        for i in item['notes_list']:
            publisherTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(i['publisherTime'] / 1000)))
            tp = (i['id'], i['inArticleTitle'], i['inArticleTitle'], i['content'], publisherTime, item['website_url'],
                  item['website_name'], publisherTime)
            val_map.append(tp)
        # self.save_mysql(sql_many, val_map)

        # def save_mysql(self, sql_many, val_map):
        db = pymysql.connect(host="192.168.1.100", port=3306, user="root", password="123456",
                             db="index_test", charset="utf8")
        cursor = db.cursor()
        try:
            cursor.executemany(sql_many, val_map)
            db.commit()
            print("数据批量插入成功啦！！")
        except Exception as e:
            db.rollback()
            e.with_traceback()
            print("数据批量插入失败！")
        # 关闭游标
        cursor.close()
        # 关闭数据库连接
        db.close()

    def save_to_txt(self, file_name, content):
        with open(file_name, 'w', encoding='utf-8') as fn:
            fn.writelines(content)
