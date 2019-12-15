#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/14 11:41
# @Author : zengsm
# @File : logging_config
import json
import logging
import logging.config
import os
import sys
import time
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

import yaml


class LoggingFactory(object):
    """logging中可以选择很多消息级别，如debug、info、warning、error、critical。
        logging.basicConfig函数各参数：
            filename：指定日志文件名；
            filemode：和file函数意义相同，指定日志文件的打开模式，'w'或者'a'；
            format：指定输出的格式和内容，format可以输出很多有用的信息，
            参数： 作用
            %(levelno)s：打印日志级别的数值
            %(levelname)s：打印日志级别的名称
            %(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
            %(filename)s：打印当前执行程序名
            %(funcName)s：打印日志的当前函数
            %(lineno)d：打印日志的当前行号
            %(asctime)s：打印日志的时间
            %(thread)d：打印线程ID
            %(threadName)s：打印线程名称
            %(process)d：打印进程ID
            %(message)s：打印日志信息
        datefmt：指定时间格式，同time.strftime()；
        level：设置日志级别，默认为logging.WARNNING；
        stream：指定将日志的输出流，可以指定输出到sys.stderr，sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略；
    """
    """ logging有一个日志处理的主对象，其他处理方式都是通过addHandler添加进去,
            handler名称：  位置；                 作用
            StreamHandler：logging.StreamHandler；日志输出到流，可以是sys.stderr，sys.stdout或者文件
            FileHandler：logging.FileHandler；日志输出到文件
            BaseRotatingHandler：logging.handlers.BaseRotatingHandler；基本的日志回滚方式
            RotatingHandler：logging.handlers.RotatingHandler；日志回滚方式，支持日志文件最大数量和日志文件回滚
            TimeRotatingHandler：logging.handlers.TimeRotatingHandler；日志回滚方式，在一定时间区域内回滚日志文件
            SocketHandler：logging.handlers.SocketHandler；远程输出日志到TCP/IP sockets
            DatagramHandler：logging.handlers.DatagramHandler；远程输出日志到UDP sockets
            SMTPHandler：logging.handlers.SMTPHandler；远程输出日志到邮件地址
            SysLogHandler：logging.handlers.SysLogHandler；日志输出到syslog
            NTEventLogHandler：logging.handlers.NTEventLogHandler；远程输出日志到Windows NT/2000/XP的事件日志
            MemoryHandler：logging.handlers.MemoryHandler；日志输出到内存中的指定buffer
            HTTPHandler：logging.handlers.HTTPHandler；通过"GET"或者"POST"远程输出到HTTP服务器"""
    """ 日志等级：使用范围
        FATAL：致命错误，与 CRITICAL 一致
        CRITICAL：特别糟糕的事情，如内存耗尽、磁盘空间为空，一般很少使用
        ERROR：发生错误时，如IO操作失败或者连接问题
        WARNING：发生很重要的事件，但是并不是错误时，如用户登录密码错误，与WARNING 一致
        INFO：处理请求或者状态变化等日常事务
        DEBUG：调试过程中使用DEBUG等级，如算法中每个循环的中间状态
    """

    def __init__(self, **arg):
        level = arg.pop('level', None)
        self.name = arg

    def buildLogger_FileHandler(self, name='logging_fh', level=logging.DEBUG, fileName='logging_fh.log'):
        """ 将日志写入到文件中 """
        logging.basicConfig(level=level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logger1 = logging.getLogger(name)
        logger1.setLevel(level=level)
        handler = logging.FileHandler(fileName)
        handler.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger1.addHandler(handler)
        return logger1

    def buildLogger_sh(self, name='logging_sh', level=logging.DEBUG, fileName='logging_sh.log'):
        """ 将日志同时输出到屏幕和日志文件"""
        logger1 = logging.getLogger(name)
        logger1.setLevel(level=level)
        handler = logging.FileHandler(fileName)
        handler.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s:')
        handler.setFormatter(formatter)
        console = logging.StreamHandler()
        console.setLevel(level)

        logger1.addHandler(handler)
        logger1.addHandler(console)
        return logger1

    def buildLogger_TimedRotatingFileHandler(self, name='logging_trf', level=logging.DEBUG, fileName='logging_rf.log'):
        """ 配置日志文件按照时间切分，日志文件保存个数
            创建一个handler，用于写入日志文件，按天保存日志
            filename：日志文件名的prefix
            when：是一个字符串，用于描述滚动周期的基本单位，字符串的值及意义如下：
            "S": Seconds "M": Minutes "H": Hours "D": Days "W": Week day (0=Monday) "midnight": Roll over at midnight
            interval: 滚动周期，单位有when指定，比如：when=’D’,interval=1，表示每天产生一个日志文件；
            backupCount: 表示日志文件的保留个数； 不写则全保存
            suffix中通常带有格式化的时间字符串
        """
        logger1 = logging.getLogger(name)
        logger1.setLevel(level)
        formatter_str = '[%(asctime)s][%(thread)d][%(filename)s][line: %(lineno)d][%(levelname)s] ## %(message)s'
        datefmt = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter(formatter_str, datefmt)

        rf = TimedRotatingFileHandler(filename=fileName, when="M", interval=1, backupCount=7,
                                      encoding='utf-8')
        rf.suffix = "%Y-%m-%d_%H-%M.log"
        rf.setFormatter(formatter)
        rf.setLevel(level)
        logger1.addHandler(rf)

        # 再创建一个handler，用于输出到控制台
        sh = logging.StreamHandler(sys.stdout)
        sh.setLevel(level)
        # 定义handler的输出格式
        sh.setFormatter(formatter)
        # 给logger添加handler
        logger1.addHandler(sh)
        return logger1

    def buildLogger_RotatingFileHandler(self, name='logging_rf', level=logging.DEBUG, fileName='logging_rf.log'):
        """ 配置日志文件大小，日志文件保存个数"""
        logger1 = logging.getLogger(name)
        logger1.setLevel(level=level)
        # 定义一个RotatingFileHandler，最多备份3个日志文件，每个日志文件最大1K(1*1024)
        rHandler = RotatingFileHandler(fileName, maxBytes=1 * 1024, backupCount=3, encoding='utf-8')
        rHandler.setLevel(level)
        format_str = '[%(asctime)s][%(thread)d][%(filename)s][line: %(lineno)d][%(levelname)s] ## %(message)s'
        formatter = logging.Formatter(format_str)
        rHandler.setFormatter(formatter)

        console = logging.StreamHandler()
        console.setLevel(level)
        console.setFormatter(formatter)

        logger1.addHandler(rHandler)
        logger1.addHandler(console)
        return logger1

    def buildLogger_json(self, config_path="./resources/logging_config.json", level=logging.DEBUG, env_key="LOG_CFG"):
        """ json配置文件配置logging日志"""
        path = config_path
        value = os.getenv(env_key, None)
        if value:
            path = value
        if os.path.exists(path):
            with open(path, "r") as f:
                config = json.load(f)
                logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=level)
        return logging

    def buildLogger_yaml(self, config_path="./resources/logging_config.yml", level=logging.DEBUG, env_key="LOG_CFG"):
        """ yaml配置文件配置logging日志"""
        path = config_path
        value = os.getenv(env_key, None)
        if value:
            path = value
        if os.path.exists(path):
            with open(path, "r") as f:
                config = yaml.load(f)
                logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=level)
        return logging


if __name__ == '__main__':
    lf = LoggingFactory()
    # logger1 = lf.buildLogger_FileHandler(level=logging.NOTSET, fileName='./logs/logging_fh.log')
    # logger1 = lf.buildLogger_sh(level=logging.DEBUG, fileName='./logs/logging_sh.log')
    # logger1 = lf.buildLogger_TimedRotatingFileHandler(level=logging.DEBUG, fileName='./logs/logging_trf.log')
    logger1 = lf.buildLogger_RotatingFileHandler(level=logging.DEBUG, fileName='./logs/logging_rf.log')
    # logger1 = lf.buildLogger_json('./resources/logging_config.json', level=logging.DEBUG)
    # logger1 = lf.buildLogger_yaml('./resources/logging_config.yml', level=logging.DEBUG)
    logger1.info("start print log...")
    for i in range(10):
        logger1.log(logging.DEBUG, time.strftime('%Y-%m-%d %H:%M:%S') + ' this is log method ' + str(i))
        logger1.debug('this is debug method ' + str(i))
        logger1.warning('this is warning method ' + str(i))
        logger1.exception('this is exception method ' + str(i))
        logger1.error('this is error method ' + str(i))
        time.sleep(1)

    logger1.info("finish print log.")
