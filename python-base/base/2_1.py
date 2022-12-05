#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/26
# @Author : zengsm
# @File : 2_1 @Description:
import pandas as pd
import numpy as np


if __name__ == '__main__':
    dt = pd.read_csv('C:\\Users\\Administrator\\Desktop\\python教程及工业数据分析\\大数据考试\\实操测试题\\2006.csv', encoding='GB2312')
    dt1 = pd.read_csv('C:\\Users\\Administrator\\Desktop\\python教程及工业数据分析\\大数据考试\\实操测试题\\2007_6.csv', encoding='GB2312')
    print(dt)
    print('丢失条目数量:', end='')
    print(365 * 48 - dt.shape[0])
