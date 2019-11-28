#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/8 10:05
# @Author : zengsm
# @File : time-convertor

import time
# %a 星期的简写。如 星期三为Web
# %A 星期的全写。如 星期三为Wednesday
# %b 月份的简写。如4月份为Apr
# %B 月份的全写。如4月份为April
# %c:  日期时间的字符串表示。（如： 11/29/2019 10:43:39）
# %d:  日在这个月中的天数（是这个月的第几天）
# %f:  微秒（范围[0,999999]）
# %H:  小时（24小时制，[0, 23]）
# %I:  小时（12小时制，[0, 11]）
# %j:  日在年中的天数 [001,366]（是当年的第几天）
# %m:  月份（[01,12]）
# %M:  分钟（[00,59]）
# %p:  AM或者PM
# %S:  秒（范围为[00,61]，为什么不是[00, 59]）
# %U:  周在当年的周数当年的第几周），星期天作为周的第一天
# %w:  今天在这周的天数，范围为[0, 6]，6表示星期天
# %W:  周在当年的周数（是当年的第几周），星期一作为周的第一天
# %x:  日期字符串（如：11/29/19）
# %X:  时间字符串（如：10:43:39）
# %y:  2个数字表示的年份
# %Y:  4个数字表示的年份
# %z:  与utc时间的间隔 （如果是本地时间，返回空字符串）
# %Z:  时区名称（如果是本地时间，返回空字符串）
# %c	转换成字符（ASCII 码值，或者长度为一的字符串）
# %r	优先用repr()函数进行字符串转换
# %s	优先用str()函数进行字符串转换
# %d / %i	转成有符号十进制数
# %u	转成无符号十进制数
# %o	转成无符号八进制数
# %x / %X	转成无符号十六进制数（x / X 代表转换后的十六进制字符的大小写）
# %e / %E	转成科学计数法（e / E控制输出e / E）
# %f / %F	转成浮点数（小数部分自然截断）
# %g / %G	%e和%f / %E和%F 的简写
# %%	输出% （格式化字符串里面包括百分号，那么必须使用%%）

#<editor-fold desc="时间转换器">

class Converter(object):
    def __init__(self):
        self = self

    @staticmethod
    def convertStringToNumber(str='2019-11-29 23:40:00'):
        """ 将字符串的时间转换为时间戳，例如  2019-11-29 23:40:00 转换 1575042000"""
        #time.struct_time(tm_year=2019, tm_mon=11, tm_mday=29, tm_hour=23, tm_min=40, tm_sec=0, tm_wday=4, tm_yday=333,
        #                 tm_isdst=-1)
        structTime = time.strptime(str, "%Y-%m-%d %H:%M:%S")
        # timestamp = 1575042000
        timestamp = int(time.mktime(structTime))
        return timestamp
    def convert(self):

        return ""

#如a = "2019-11-29 23:40:00",想改为 a = "2019/11/29 23:40:00"
    #方法:先转换为时间数组,然后转换为其他格式
a = "2019-11-29 23:40:00"
timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
print(timeArray)
otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
print(otherStyleTime)

# </editor-fold>
