#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/1 14:04
# @File : start
import math
import os
import random
import sys
import uuid

import requests
import urllib3
from scrapy.cmdline import execute

if __name__ == '__main__':
    """ scrapy crawl spider_name -o file_name.txt   输出结果到文件里
        scrapy crawl spider_name -s JOBDIR=job_tmp/spider  缓存中间数据，重启继续运行
    """
    # sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    # try:
    #     execute(['scrapy', 'crawl', 'scrapyProbe'])
    # except Exception as e:
    #     print(e)

    urllib3.disable_warnings()
    header = {'Accept': '*/*',
              'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9',
              'Connection': 'keep-alive',
              'Cookie': "session-sensor=050a5691-7eac-484d-afa4-53c8ac9f5289",
              'Host': '10.130.1.206',
              'Referer': 'https://10.130.1.206/home/rule',
              'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-platform': '"Windows"',
              'Sec-Fetch-Dest': 'empty',
              'Sec-Fetch-Mode': 'cors',
              'Sec-Fetch-Site': 'same-origin',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
              'X-Requested-With': 'XMLHttpRequest'}
    updating_url = 'https://10.130.1.206/skyeye/rules/getRule?rule=&level=all&confidence=1,2,3&category=all&attack_res=0,1,2,3&block=all&state=all&page=2&pagesize=20&order_by=level:0&csrf_token=ef6c5f1d878d15731404ec2d99c89e16&r=' + str(random.random())

    response = requests.get(updating_url,headers=header,verify=False)
    print(response)
    print(response.request.headers)
