#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/9/28 10:56
# @Author : zengsm
# @File : test.py


import json
import sys




class People(object):
    #构造函数，不明确定义参数个数
    def __init__(self, *arg):
        self.age = arg

    def sayAge(self):
        print(str(self.age))
#调用方式
p1 = People()
p2 = People('charlie')
p3 = People('charlie', 22)

p1.sayAge()
p2.sayAge()
p3.sayAge()
