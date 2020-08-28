#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : news_flash
import json
import time

import pymysql
import scrapy

from items import SteelInformationItem


class NewsFlash(scrapy.Spider):
    name = 'mysteel'
    allowed_domains = ['mysteel.com']
    start_urls = ['https://www.mysteel.com/activity/api/newsflash/flashnews/query_newsflash.htm?'
                  'pageNo=1&sectionId=&categoryId=&pageSize=30']

    def parse(self, response):
        """ yield item  提交给管道文件处理 pipelines
            yield scrapy.Request( next_url, callback=self.parse)   提交子请求，回调递归处理
        """
        print(response)
        body = response.body.decode('utf-8')
        list_data = json.loads(body)['list']
        item = SteelInformationItem(title='', notes_list=list_data,
                                    website_url='https://www.mysteel.com/fastcomment/#/', website_name='我的钢铁',
                                    response=response)
        # self.save_data(item)

        # def save_data(self, item: SteelInformationItem):

        sql_many = "replace  INTO `jiwei_xn_index_test`.`p_ifm_announce_bigdata`" \
                   "(`news_id`, `title_name`, `notes`, `texts`,`publish_time`, `website`, `website_name`,create_time)" \
                   " VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "

        val_map = []
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
