#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/9/28 10:56
# @Author : zengsm
# @File : test.py
import datetime

if __name__ == '__main__':
    print("test start ..... ")
    year = datetime.datetime(datetime.datetime.today().year)
    month = datetime.datetime.today().month
    t = datetime.date.strftime((year, month, 1) - datetime.timedelta(1), "%Y-%m")
    print(t)
    print(type(t))
