# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from twisted.enterprise import adbapi


class SteelInformation1Pipeline:
    @classmethod
    def from_crawler(self, crawler):
        # 从项目的配置文件中读取相应的参数
        self.MYSQL_DB_NAME = crawler.settings.get("MYSQL_DB_NAME", 'test_db')
        self.HOST = crawler.settings.get("MYSQL_HOST", 'localhost')
        self.PORT = crawler.settings.get("MYSQL_PORT", 3306)
        self.USER = crawler.settings.get("MYSQL_USER", 'root')
        self.PASSWD = crawler.settings.get("MYSQL_PASSWORD", '123456')
        return self()

    def open_spider(self, spider):
        self.dbpool = adbapi.ConnectionPool('pymysql', host=self.HOST, port=self.PORT, user=self.USER,
                                            passwd=self.PASSWD, db=self.MYSQL_DB_NAME, charset='utf8')

    def close_spider(self, spider):
        self.dbpool.close()

    def process_item(self, item, spider):
        self.dbpool.runInteraction(self.insert_db, item)
        return item

    def insert_db(self, tx, item):
        values = (
            item['news_id'],
            item['title_name'],
            item['type_id'],
            item['signs'],
            item['info_channel'],
            item['audio_path'],
            item['img_path'],
            item['notes'],
            item['texts'],
            item['zan_count'],
            item['publish_time'],
            item['source'],
            item['bottom_source'],
            item['bottom_url'],
            item['summary'],
            item['website'],
            item['website_name'],
            item['child_topic'],
            item['child_topic_url'],
            item['keyword_type']
        )
        # sql = 'INSERT INTO `p_ifm_news_bigdata` (`news_id`,`title_name`,`type_id`,`signs`,`info_channel`,`audio_path`,' \
        #       '`img_path`,`notes`,`texts`,`create_time`,`zan_count`,`publish_time`,`source`,`bottom_source`,' \
        #       '`bottom_url`,`summary`,`website`,`website_name`,`child_topic`,`child_topic_url`,`keyword_type`) ' \
        #       'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ' \
        #       'ON DUPLICATE KEY UPDATE modify_time= CURRENT_TIMESTAMP();'
        sql = item['sql']
        tx.execute(sql, values)


class SaveImagePipeline:
    def process_item(self, item, spider):
        return item
