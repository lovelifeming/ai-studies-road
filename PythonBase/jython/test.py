#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/9/28 10:56
# @Author : zengsm
# @File : test.py
import datetime
import time
import redis


# class People(object):
#     # 构造函数，不明确定义参数个数
#     def __init__(self, *arg):
#         self.age = arg
#
#     def sayAge(self):
#         print(str(self.age))
#
# # 调用方式
# p1 = People()
# p2 = People('charlie')
# p3 = People('charlie', 22)
#
# p1.sayAge()
# p2.sayAge()
# p3.sayAge()

def utcTime_To_StandardTime(utc_str: str, utc_format: str, hours_i: int):
    """
    UTC时间字符串转换为时间戳 ("2019-11-11T12:15:05.786Z","%Y-%m-%dT%H:%M:%S.%fZ",8) return:2019-11-11 20:15:05.786000
    ("2019-11-11 12:15:05.786","%Y-%m-%dT%H:%M:%S.%fZ",0) return: 2019-11-11 12:15:05.786000
    """
    try:
        utcTime = datetime.datetime.strptime(utc_str, utc_format)  # "%Y-%m-%dT%H:%M:%S.%fZ"   "%Y-%m-%d %H:%M:%S.%f"
        standard = utcTime + datetime.timedelta(hours=hours_i)
        return standard
    except Exception as e:
        # logger.exception(e)
        return utc_str


def format_To_UTCTime(standardstr: str,standard_format:str, target_format: str, hours_i: int=0,second_i:int=0):
    """
    UTC时间字符串转换为时间戳 ("2019-11-11 12:15:05.786","%Y-%m-%d %H:%M:%S.%f","%Y-%m-%dT%H:%M:%S.%fZ",hours_i=8)
        return:2019-11-11T20:15:05.786000Z
    ("2019-11-11 12:15:05.786","%Y-%m-%d %H:%M:%S.%f","%Y/%m/%d %H:%M:%S",hours_i=-1,second_i=30) return: 2019/11/11 11:15:35
    """
    try:
        standTime=datetime.datetime.strptime(standardstr, standard_format)
        standardStr = standTime + datetime.timedelta(hours=hours_i,seconds=second_i)
        utcTime = datetime.datetime.strftime(standardStr,target_format)  # "%Y-%m-%dT%H:%M:%S.%fZ"   "%Y-%m-%d %H:%M:%S.%f"
        return utcTime
    except Exception as e:
        # logger.exception(e)
        print(e)
        return standardstr


if __name__ == '__main__':
    print("test start ..... ")
    # conn = redis.Redis(host="192.168.3.107", port=6379,password="")
    conn = redis.Redis(host="222.212.94.62", port=6666, password="")
    # conn.set("P_Dephosphorization_U1", "123.22")  # ex=5代表seconds，px=1000 代表ms
    val = conn.hget("P_Dephosphorization_U1", 'timeStamp')
    print(val)
    datetime.datetime.now().timestamp()


