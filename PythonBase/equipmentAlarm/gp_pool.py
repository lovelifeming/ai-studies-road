#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/25 14:36
# @Author : zengsm
# @File : gp_pool
from psycopg2.pool import SimpleConnectionPool

class GPPool:
    dbname='localhost'
    user='gpadmin'
    host='127.0.0.1'
    password='gpadmin'
    port=5432
    gp_pool=None
    def __init__(self,dbname,user,host,password,port):
        self.dbname=dbname
        self.user=user
        self.host=host
        self.password=password
        self.port=port
        # pgpool = ThreadedConnectionPool(1, 5, dbname=pg_name, user=pg_user, host=pg_host, password=pg_pw, port=pg_port)
        self.gp_pool = SimpleConnectionPool(1, 5, dbname=dbname, user=user, host=host, password=password, port=port)
    def conn_exe(*sp):
        conn = gp_pool.getconn()  # 获取连接
        cursor = conn.cursor()  # 获取cursor
        cursor.execute(*sp)
        conn.commit()  # 没次操作都要提交
        gp_pool.putconn(conn)  # 放回连接, 防止其他程序pg无连接可用
        return cursor

    def fetchone_sql(*sp):
        cursor = conn_exe(*sp)
        # desc = cursor.description  # cursor 的具体描述信息
        fetchone = cursor.fetchone()
        cursor.close()
        return fetchone

    def fetchall_sql(*sp):
        cursor = conn_exe(*sp)
        fetchall = cursor.fetchall()
        cursor.close()
        return fetchall

    def get_insert_id(*sp):
        *sp += " returning id"  # 插入语句这样返回 插入的id(或者其他字段 看上一行的SQL 语句)
        cursor = conn_exe(*sp)
        insert_id = cursor.fetchone()[0]
        cursor.close()
        return insert_id

    def run_sql(*sp):
        cursor = conn_exe(*sp)
        cursor.close()









