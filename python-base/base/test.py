#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/3 16:01
# @File : test
import time

import pandas as pd

from base import Connector

if __name__ == '__main__':
    print('start ...')
    # pm = Connector.PyMysql('bigdata03', 3306, 'bigdata', 'bigdata', 'restapi')
    # data = pm.query_all('SELECT * FROM `xh_tskhzt_xunhuanads_xh_resource_process_info_api__copy1`')
    # df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])
    # gb = df.groupby(by=['A'])
    # result = []
    # for name, group in gb:
    #     sv = group.sort_values(by="D", ascending=True).values
    #     priceDiff = []
    #     start = list(sv[0])
    #     gp = []
    #     lst = [start]
    #     for i in range(1, len(sv)):
    #         tmp = list(sv[i])
    #         if tmp[3] == start[3]:
    #             lst.append(tmp)
    #         else:
    #             if len(lst) > 1:
    #                 std = sorted(lst, key=lambda x: x[2])
    #                 gpid = '-'.join(str(x[2]) for x in std)
    #                 for x in std:
    #                     x.append(gpid)
    #                     x.append(3)
    #                 gp.append(std)
    #             lst = [tmp]
    #         start = tmp
    #     for n in gp:
    #         for x in n:
    #             result.append(x)
    # print(result)
    # df = pd.DataFrame([x for x in result], columns=['资源id', '报价时间', '报价', '报价公司id', '分组编号', '围标类型'])
    # wt = pd.ExcelWriter('C:\\Users\\Administrator\\Desktop\\清风工程2020-11\\test.xlsx')
    # df.to_excel(wt)
    # wt.save()
    # wt.close()

    rfind = '2020-03-25 11:38:22'.rfind(':')

    print('end ...')
