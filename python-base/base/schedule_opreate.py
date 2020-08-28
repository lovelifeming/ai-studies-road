#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/28 10:53
# @File : schedule_opreate
import datetime
import time


def sleep_time(seconds):
    """ while 循环定时器"""
    while True:
        print('running...')
        print(datetime.datetime.now())
        time.sleep(seconds)


if __name__ == '__main__':
    # sleep_time(10)
    d1 = '2020年08月28日'
    d2 = '15:48';
    d3 = d1 + ' ' + d2
    # s = time.strptime(d3, '%Y年-%m月-%d日 %H:%M')
    s = time.strptime(d3, '%Y-%m-%dT%H:%M')
    print(s)
