#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/27 10:27
# @File : main
import os
import sys

from scrapy.cmdline import execute

if __name__ == '__main__':
    """ scrapy crawl spider_name -o file_name.txt   输出结果到文件里
    scrapy crawl spider_name -s JOBDIR=crawls/somespider-1  缓存中间数据，重启继续运行
    """
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    # execute(['scrapy', 'crawl', 'mysteel'])
    execute(['scrapy', 'crawl', 'ganggu'])
