# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

import pymysql
# from elasticsearch import Elasticsearch
from twisted.enterprise import adbapi

from scrapy_probe.settings import IMAGES_STORE


class ScrapyDemoPipeline:
    def process_item(self, item, spider):
        return item


# 数据库字段：`unique_key`  `publish_time`    `spider_time`   `area`  `city`  `product_type`  `classified`
#   `price` `source_site`   `version`   `create_time`   `modify_time`

class PipelineMySql:
    """ 爬虫数据保存到 MySQL """

    @classmethod
    def from_crawler(cls, crawler):
        # 从项目的配置文件中读取相应的参数
        cls.mysql_db_name = crawler.settings.get("MYSQL_DB_NAME", 'test_db')
        cls.host = crawler.settings.get("MYSQL_HOST", 'localhost')
        cls.port = crawler.settings.get("MYSQL_PORT", 3306)
        cls.user = crawler.settings.get("MYSQL_USER", 'root')
        cls.password = crawler.settings.get("MYSQL_PASSWORD", '123456')
        return cls()

    def __init__(self):
        # connection database  后面三个依次是数据库连接名、数据库密码、数据库名称
        self.connect = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.password,
                                       db=self.mysql_db_name, charset='utf8')
        # get cursor
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        """ 查询数据库是否已保存"""
        query = "SELECT count(*) FROM scrapy_probe WHERE unique_key= '{}'".format(item['unique_key'])
        self.cursor.execute(query)
        res = self.cursor.fetchone()
        if res is None or res[0] == 0:
            item["version"] = 2
        # 封装入库 item
        values = (item["unique_key"], item["publish_time"], item["spider_time"], item["title"], item["city"],
                  item["area"], item["address"], item["product_type"], item["classified"], item["price"],
                  item["source_site"], item["version"])
        sql = 'INSERT INTO `scrapy_probe` (`unique_key`, `publish_time`, `spider_time`,`title`, `city`, `area`,' \
              ' `address`,`product_type`, `classified`, `price`,`source_site`,`version`,`create_time`) VALUES ' \
              '(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW()) ' \
              'ON DUPLICATE KEY UPDATE modify_time= CURRENT_TIMESTAMP();'
        # 执行插入数据到数据库操作
        self.cursor.execute(sql, values)
        # 提交，不进行提交无法保存到数据库
        self.connect.commit()
        return item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.connect.close()


class PipelineMySqlAsyn:
    """ 爬虫数据保存到 MySQL数据库，采用异步插入数据 """

    def __init__(self):
        self.db_pool = adbapi.ConnectionPool('pymysql', host=self.host, port=self.port, user=self.user,
                                             passwd=self.password, db=self.mysql_db_name, charset='utf8')

    @classmethod
    def from_crawler(self, crawler):
        # 从项目的配置文件中读取相应的参数
        self.mysql_db_name = crawler.settings.get("MYSQL_DB_NAME", 'test_db')
        self.host = crawler.settings.get("MYSQL_HOST", 'localhost')
        self.port = crawler.settings.get("MYSQL_PORT", 3306)
        self.user = crawler.settings.get("MYSQL_USER", 'root')
        self.password = crawler.settings.get("MYSQL_PASSWORD", '123456')
        return self()

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.db_pool.close()

    def process_item(self, item, spider):
        self.db_pool.runInteraction(self.insert_db, item)
        return item

    def insert_db(self, tx, item):
        # 封装入库 item
        values = (item["unique_key"], item["publish_time"], item["spider_time"], item["title"], item["city"],
                  item["area"], item["address"], item["product_type"], item["classified"], item["price"],
                  item["source_site"], item["version"])
        sql = 'INSERT INTO `scrapy_probe` (`unique_key`, `publish_time`, `spider_time`,`title`, `city`, `area`,' \
              ' `address`,`product_type`, `classified`, `price`,`source_site`,`version`,`create_time`) VALUES ' \
              '(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW()) ' \
              'ON DUPLICATE KEY UPDATE modify_time= CURRENT_TIMESTAMP();'
        tx.execute(sql, values)


class PipelineImages:
    """ 爬虫数据图片/文件保存到指定位置，images_urls 是配置自动下载图片的字段 """

    def process_item(self, item, spider):
        for value in item:
            if hasattr(value, 'keys') and 'images_name' in value.keys():
                name = value['images_name']
                abspath = os.path.join(IMAGES_STORE, name)
                item['images_path'] = abspath
        return item


# class PipelineES:
#     """ 爬虫数据保存到 ES """
#
#     def __init__(self):
#         self.es = Elasticsearch(self.es_hosts, http_auth=(self.es_user, self.es_password), port=self.es_port)
#
#     @classmethod
#     def from_crawler(self, crawler):
#         # 从项目的配置文件中读取相应的参数
#         self.es_hosts = crawler.settings.get("ES_HOSTS", 'localhost')
#         self.es_port = crawler.settings.get("ES_PORT", 9201)
#         self.es_user = crawler.settings.get("ES_USER", 'root')
#         self.es_password = crawler.settings.get("ES_PASSWORD", '123456')
#         return self()
#
#     def open_spider(self, spider):
#         pass
#
#     def close_spider(self, spider):
#         self.es.close()
#
#     def process_item(self, item, spider):
#         # 封装入库 item
#         values = {"unique_key": item["unique_key"], "publish_time": item["publish_time"],
#                   "spider_time": item["spider_time"], "area": item["area"], "city": item["city"],
#                   "product_type": item["product_type"], "classified": item["classified"], "price": item["price"],
#                   "source_site": item["source_site"], "version": item["version"]}
#         # 判断是否需要更新
#         query = {
#             "query": {
#                 "bool": {
#                     "must": [
#                         {"match_phrase": {"unique_key": item["unique_key"]}},
#                         {"match_phrase": {"publish_time": item["publish_time"]}},
#                         {"match_phrase": {"area": item["area"]}},
#                         {"match_phrase": {"city": item["city"]}},
#                         {"match_phrase": {"product_type": item["product_type"]}},
#                         {"match_phrase": {"classified": item["classified"]}},
#                         {"match_phrase": {"price": item["price"]}},
#                         {"match_phrase": {"source_site": item["source_site"]}},
#                         {"match_phrase": {"version": item["version"]}}
#                     ]
#                 }
#             }
#         }
#         result = ""
#         try:
#             result = self.es.search(index="spider_es_index", body=query)
#         except Exception as e:
#             print(str(e))
#             if 'index_not_found_exception' in str(e):
#                 self.es.index(index="spider_es_index", doc_type='spider_es_index', body=values)
#         if result is not "" and len(result["hits"]["hits"]) == 0:
#             self.es.index(index="spider_es_index", doc_type='spider_es_index', body=values)
#             print("新增数据：" + str(values))
#         else:
#             print("已有数据：" + str(values))
#         return item


class PipelineFilter:
    def process_item(self, item, spider):
        # todo  Filter item
        return item
