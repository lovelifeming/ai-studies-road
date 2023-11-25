#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/2/7
# @Author : zengsm
# @File : mysql @Description:
import datetime

import mysql


class mysqlOperate():
    mydb = None

    def __init__(self, host, user, passwd, database):
        self.host = host
        self.passwd = user
        self.passwd = passwd
        self.database = database
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=database
        )

    def executeUpdate(self, *args):
        mycursor = self.mydb.cursor()
        tmp = []
        if len(args[0]) != 0 or datetime.datetime.now().hour == 11:
            mycursor.execute("SELECT * FROM `user_tb` where id in ("+args[0]+")")
            res = mycursor.fetchall()
            for i in res:
                tmp.add({i[0], i[1]})
        if args[0] not in tmp:
            sql = "INSERT into `user_tb`(id,user_name,update_time) values (%s,%s,%s)"
            val = (args[0], "", datetime.datetime.now().__str__())
            mycursor.execute(sql, val)
            self.mydb.commit()
