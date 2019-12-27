#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/18 13:44
# @Author : zengsm
# @File : redis_monitor
import logging
import threading
import time
from logging.handlers import TimedRotatingFileHandler
from queue import Queue

import redis


def getLogger(fileName: str, name='mylogger', level=logging.DEBUG):
    logger1 = logging.getLogger(name)
    logger1.setLevel(level)
    formatter_str = '[%(asctime)s][%(thread)d][%(filename)s][line: %(lineno)d][%(levelname)s] ## %(message)s'
    datefmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(formatter_str, datefmt)

    rf = TimedRotatingFileHandler(filename=fileName, when="midnight", interval=1, backupCount=15,
                                  encoding='utf-8')
    rf.suffix = "%Y-%m-%d_%H-%M.log"
    rf.setFormatter(formatter)
    rf.setLevel(level)
    logger1.addHandler(rf)
    return logger1

logger = getLogger('./logs/redis_monitor.log', logging.DEBUG)

# 定义数据查询向前偏移时间（秒）
SJ_XQPY = 2 * 60 * 60
# 定义获取规则数据接口url
HQ_SJGZ = 'http://localhost:8087/digitized/rule/python/param'
# 定义获取规则数据接口参数
PAYLOAD = {'scriptTag': 'XMK'}
PAYLOAD = {'scriptTag': 'FIXED_ALARM_TRUE'}
PAYLOAD = {'scriptTag': 'MOTOR_SM'}
PAYLOAD = {'scriptTag': 'BCK'}
# 定义消费者线程数，报警信息保存线程数，预警值报警测点共 360 个
CUSTOMS_THREAD = 5
# 创建队列
ruleQueue = Queue(720)
alarmQueue = Queue(720)

def createRedisConnect():
    """ 创建 Redis 数据库连接,返回redis 数据库 连接池"""
    count = 0
    redis_conn = None
    while True:
        try:
            if redis_conn is None:
                pool = redis.ConnectionPool(host="192.1.1.100", port=6379, password="", max_connections=20)
                redis_conn = redis.Redis(connection_pool=pool)
            return redis_conn
        except Exception as e:
            logger.exception(e)
            time.sleep(10 * count)
            count += 1
            if count > 100:
                break



if __name__ == '__main__':
    threading.Thread()