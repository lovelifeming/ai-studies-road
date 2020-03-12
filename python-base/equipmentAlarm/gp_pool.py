#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/25 14:36
# @Author : zengsm
# @File : gp_pool
from psycopg2.pool import ThreadedConnectionPool, SimpleConnectionPool


class GPPool:
    dbname = 'localhost'
    user = 'gpadmin'
    host = '127.0.0.1'
    password = 'gpadmin'
    port = 5432
    gp_pool = None

    def __init__(self, gp_host, gp_port, gp_dbname, gp_user, password, minconn=1, maxconn=5, multithreading=True):
        self.host = gp_host
        self.port = gp_port
        self.dbname = gp_dbname
        self.user = gp_user
        self.password = password
        if multithreading:
            # 可用在多线程应用程序中
            self.gp_pool = ThreadedConnectionPool(minconn, maxconn, host=gp_host, port=gp_port, dbname=gp_dbname,
                                                  user=gp_user, password=password)
        else:
            # 仅用于单线程应用程序中
            self.gp_pool = SimpleConnectionPool(minconn, maxconn, host=gp_host, port=gp_port, dbname=gp_dbname,
                                                user=gp_user, password=password)

    def exe_conn(self, sql):
        conn = self.gp_pool.getconn()  # 获取连接
        cursor = conn.cursor()  # 获取cursor
        cursor.execute(sql)  # 用于执行SQL语句
        # cursor.mogrify(query)  #返回生成的sql脚本, 用以查看生成的sql是否正确
        conn.commit()  # 没次操作都要提交
        self.gp_pool.putconn(conn)  # 放回连接, 防止其他程序pg无连接可用
        return cursor

    def fetchone_sql(self, sql):
        cursor = self.exe_conn(sql)
        # desc = cursor.description  # cursor 的具体描述信息
        fetchone = cursor.fetchone()  # 获取执行结果中的一条记录
        cursor.close()  # 关闭当前连接的游标
        return fetchone

    def fetchall_sql(self, sql):
        cursor = self.exe_conn(sql)
        fetchall = cursor.fetchall()  # 获取SQL执行结果中的所有记录，返回值是一个元组的列表，每一条记录是一个元组
        cursor.close()
        return fetchall

    def fetchmany_sql(self, sql, size=1):
        cursor = self.exe_conn(sql)
        fetchall = cursor.fetchmany(size)  # 获取SQL执行结果中指定条数的记录，记录数由size指定
        cursor.close()
        return fetchall

    def exe_sql(self, sql):
        cursor = self.exe_conn(sql)
        cursor.close()

    def close_all(self):
        self.gp_pool.closeall()


if __name__ == '__main__':
    gp_pool = GPPool('192.1.1.100', 5432, 'testdb', 'gpadmin', 'gpamdin', multithreading=True)
    sql = "SELECT * FROM mes.user_login;"
    result = gp_pool.fetchone_sql(sql)
    print(result)
