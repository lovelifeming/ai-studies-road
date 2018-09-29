#-*-coding:utf-8-*-


import sys


class People(object):
    #构造函数，不明确定义参数个数
    def __init__(self, *arg):
        self.age = arg
    def sayAge(self):
        print(str(self.age))
