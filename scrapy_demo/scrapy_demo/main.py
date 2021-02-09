#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/1 14:04
# @File : start
import os
import sys

from scrapy.cmdline import execute

if __name__ == '__main__':
    """ scrapy crawl spider_name -o file_name.txt   输出结果到文件里
        scrapy crawl spider_name -s JOBDIR=job_tmp/spider  缓存中间数据，重启继续运行
    """
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    try:
        execute(['scrapy', 'crawl', 'scrapyDemo'])
    except Exception as e:
        print(e)
