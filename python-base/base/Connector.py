#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/3 17:33
# @File : Connector
import pymysql
from twisted.enterprise import adbapi
from twisted.internet import reactor


class TwMysql(object):
    def __init__(self, host="localhost", port=3306, user="root", passwd="123456", db="test_db", charset='utf8'):
        # 连接数据库
        self.dbpool = adbapi.ConnectionPool('pymysql', host=host, port=port, user=user, passwd=passwd,
                                            db=db, charset=charset)

    def run_query(self, query, values):
        res = self.dbpool.runQuery(query, values).addCallback(self._run_query)
        return res

    def _run_query(self, val):
        if val:
            print('data: ', val[0][0])
        else:
            print('No such data.')

    def execute_asyn(self, item):
        res = self.dbpool.runInteraction(self._execute, item)
        # 添加异常处理
        res.addCallback(self._error_call_back)
        # 暂停 2s 之后调用 reactor.stop，用于等待异步调用执行结果
        reactor.callLater(2, reactor.stop)
        reactor.run()
        return res

    def _execute(self, cursor, item):
        res = cursor.execute(item['sql'], item['values'])
        return res

    def _error_call_back(self, failure):
        # 处理异步插入时的异常
        if failure:
            print('error call back:', failure)
        else:
            print('error call back:', failure)
        return failure

    def close_pool(self):
        # 关闭连接
        self.dbpool.close()


class PyMysql(object):
    def __init__(self, host="localhost", port=3306, user="root", passwd="123456", db="test_db", charset='utf8'):
        # 连接数据库
        self.connect = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
        self.cursor = self.connect.cursor()

    def query_one(self, query):
        self.cursor.execute(query)
        res = self.cursor.fetchone()
        return res

    def query_all(self, query):
        self.cursor.execute(query)
        res = self.cursor.fetchall()
        return res

    def execute(self, sql, values=None):
        # 执行数据库数据操作
        self.cursor.execute(sql, values)
        # 提交，不进行提交无法保存到数据库
        self.connect.commit()
        res = self.cursor.fetchall()
        return res

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.connect.close()


if __name__ == '__main__':
    conn_param = {"host": "localhost", "port": 3306, "user": "root", "passwd": "123456",
                  "db": "test_db", "charset": 'utf8'}
    # pm = PyMysql(**conn_param)
    # res = pm.execute("SELECT * FROM `student` WHERE user_sex='男'", None)

    tw = TwMysql(**conn_param)
    item = dict()
    item['sql'] = "SELECT * FROM `student` WHERE user_sex=%s"
    item['values'] = "女"
    res = tw.execute_asyn(item)

    print('last result:', res)
