#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/8 10:05
# @Author : zengsm
# @File : time-convertor
import calendar
import time
from datetime import datetime, timedelta

"""
  %a 星期的简写。如 星期三为Web
  %A 星期的全写。如 星期三为Wednesday
  %b 月份的简写。如4月份为Apr
  %B 月份的全写。如4月份为April
  %c:  日期时间的字符串表示。（如： 11/29/2019 10:43:39）
  %d:  日在这个月中的天数（是这个月的第几天）(0-31)
  %f:  微秒（范围[0,999999]）
  %H:  小时（24小时制，[0, 23]）
  %I:  小时（12小时制，[0, 11]）
  %j:  日在年中的天数 [001,366]（是当年的第几天）
  %m:  月份（[01,12]）
  %M:  分钟（[00,59]）
  %p:  AM或者PM
  %S:  秒（范围为[00,61]，为什么不是[00, 59]）
  %U:  周在当年的周数当年的第几周），星期天作为周的第一天(00-53)
  %w:  今天在这周的天数，范围为[0, 6]，6表示星期天，0是星期天
  %W:  周在当年的周数（是当年的第几周），星期一作为周的第一天(00-53)
  %x:  日期字符串（如：11/29/19）
  %X:  时间字符串（如：10:43:39）
  %y:  2个数字表示的年份 (00-99)
  %Y:  4个数字表示的年份 (000-9999)
  %z:  与utc时间的间隔 （如果是本地时间，返回空字符串）
  %Z:  时区名称（如果是本地时间，返回空字符串）
  %c	转换成字符（ASCII 码值，或者长度为一的字符串）
  %r	优先用repr()函数进行字符串转换
  %s	优先用str()函数进行字符串转换
  %d / %i	转成有符号十进制数
  %u	转成无符号十进制数
  %o	转成无符号八进制数
  %x / %X	转成无符号十六进制数（x / X 代表转换后的十六进制字符的大小写）
  %e / %E	转成科学计数法（e / E控制输出e / E）
  %f / %F	转成浮点数（小数部分自然截断）
  %g / %G	%e和%f / %E和%F 的简写
  %%	输出% （格式化字符串里面包括百分号，那么必须使用%%）
"""


# <editor-fold desc="时间转换器">

class Converter(object):
    def __init__(self):
        self = self

    @staticmethod
    def convertStringToNumber(time_str, format):
        """ 将字符串的时间转换为时间戳，例如  2019-11-29 23:40:00   "%Y-%m-%d %H:%M:%S 转换 1575042000"""
        # time.struct_time(tm_year=2019, tm_mon=11, tm_mday=29, tm_hour=23, tm_min=40, tm_sec=0, tm_wday=4, tm_yday=333,
        #                 tm_isdst=-1)
        structTime = time.strptime(time_str, format)
        # timestamp = 1575042000
        timestamp = int(time.mktime(structTime))
        print('时间戳：' + str(timestamp))
        return timestamp

    def convert_format(self, time_str, source_format, target_format):
        # 如 "2019-11-29 23:40:00"    %Y-%m-%d %H:%M:%S,想改为 "2019/11/29 23:40:00"    %Y/%m/%d %H:%M:%S
        # 方法:先转换为时间数组,然后转换为其他格式
        timeArray = time.strptime(time_str, source_format)
        print('转换前：' + str(time_str))
        otherStyleTime = time.strftime(target_format, timeArray)
        print('转换后：' + otherStyleTime)
        return otherStyleTime

    def convert_format_timeStamp(self):
        # 使用time
        timeStamp = 1575042456
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
        print(otherStyleTime)  # 2019--11--29 23:47:36
        # 使用datetime
        timeStamp = 1575042456
        dateArray = datetime.fromtimestamp(timeStamp)
        otherStyleTime = dateArray.strftime("%Y--%m--%d %H:%M:%S")
        print(otherStyleTime)  # 2019--11--29 23:47:36
        # 使用datetime，指定utc时间，相差8小时
        timeStamp = 1575042456
        dateArray = datetime.utcfromtimestamp(timeStamp)
        otherStyleTime = dateArray.strftime("%Y--%m--%d %H:%M:%S")
        print(otherStyleTime)  # 2019--11--29 15:47:36

    @staticmethod
    def buildTime(year, month, days, hours, minutes, seconds):
        build_time = datetime(year=year, month=month, day=days, hour=hours, minute=minutes, second=seconds)
        print('新建时间：' + str(build_time))  # 新建时间：2019-11-29 18:01:58
        print('时间偏移10s：' + str(build_time + timedelta(seconds=10)))  # 时间偏移10s：2019-11-29 18:02:08
        print('时间偏移-10s：' + str(build_time + timedelta(seconds=-10)))  # 时间偏移-10s：2019-11-29 18:01:48
        print('当前时间：' + str(datetime.today()))  # 当前时间：2019-11-29 19:32:05.026000
        print('当前时间戳：' + str(time.time()))  # 当前时间：2019-11-29 19:32:05.026000

    def get_now_time(self):
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        print(now_time)  # 获取当前时间，精确到秒 2019-12-04 13:57:02
        now_datetime = datetime.now()
        print(now_datetime)  # 获取当前时间，精确到纳秒 2019-12-04 13:57:02.652000
        now_timestamp = time.time()
        print(now_timestamp)  # 获取当前时间戳，精确到纳秒 1575441460.205
        now_datetime_timestamp = datetime.today().timestamp()
        print(now_datetime_timestamp)  # 获取当前时间戳，精确到纳秒 1575441460.205
        return now_datetime

    def get_before_offset(self, day: int = 0, hour: int = 0, minute: int = 0, second: int = 0):
        now_time = datetime.now()
        off_time = now_time + timedelta(days=day, hours=hour, minutes=minute, seconds=second)
        print(off_time)  # 2019-12-04 13:27:40.276000
        return off_time

    def get_day_start_end(self):
        ''' 获取当天开始时间和结束时间 '''
        today = datetime.today()
        start_time = datetime(year=today.year, month=today.month, day=today.day)
        end_time = datetime(year=today.year, month=today.month, day=today.day, hour=23, minute=59, second=59)
        print('start_time：' + str(start_time) + ' end_time：' + str(end_time))
        return [start_time, end_time]

    def get_weekend(self):
        weekend = datetime.today() + timedelta(6 - datetime.today().weekday())
        print('本周最后一天：' + str(weekend))
        return weekend

    def get_current_month_end(self):
        w_num, last_day_num = calendar.monthrange(datetime.today().year, datetime.today().month)
        print('本月第一天周天：' + str(w_num) + ' 本月最后一天日期' + str(last_day_num))
        month_end = datetime(datetime.today().year, datetime.today().month, last_day_num)
        print('本月最后一天：' + str(month_end))
        return month_end

    def get_last_month_end_day(self):
        ''' 获取上一个月最后一天的日期 2019-11-30 00:00:00 '''
        today = datetime.today()
        year = today.year
        month = today.month
        month_one_day = datetime(year, month, 1)
        lastDay = month_one_day - timedelta(1)
        lastDay1 = datetime(today.year, today.month, 1) - timedelta(1)
        print('上月最后一天：' + str(lastDay))
        print('上月最后一天：' + str(lastDay1))
        return lastDay


if __name__ == '__main__':
    start_time = datetime.now()
    converter = Converter()
    converter.convert_format('2019-11-29 23:40:00', '%Y-%m-%d %H:%M:%S', '%Y/%m/%d %H:%M:%S')
    converter.convert_format_timeStamp()
    converter.get_now_time()
    converter.get_before_offset(hour=-1)
    converter.get_day_start_end()
    converter.get_weekend()
    converter.get_current_month_end()
    converter.get_last_month_end_day()

    Converter.convertStringToNumber('2019-11-29 23:40:00','%Y-%m-%d %H:%M:%S')
    Converter.buildTime(2019, 11, 29, 18, 1, 58)
    time.sleep(1)
    end_time = datetime.now()
    print(end_time - start_time)  # 计算秒级别时间差  0:00:01.001000

# </editor-fold>
