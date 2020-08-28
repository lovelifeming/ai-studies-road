#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/28 10:21
# @File : search
import re


def multi_key(keys, content):
    """ 多个关键字筛选"""
    regex = keys  # example: "key|key2|key3"
    findall = re.findall(regex, content)  # 返回可以查询到的key
    print(findall)  # ['策略', '领导', '领导', '领导', '技巧']
    return findall


if __name__ == '__main__':
    key = multi_key("策略|技巧|领导", "批评家应该谈论策略，作为一个领导者，你不能太任性，否则真的没有效果。"
                                "把它轻轻放在不能触及灵魂的地方，而把它认真放在容易产生抵触，如果你不发脾气，你的下属就"
                                "不会记得。如果你发脾气，你的下属会认为领导只是在发泄。因此，领导批评人应注意三个原则："
                                "公开批评，责人先责己；说话一定要有技巧，尝试以人制人；将心比心，一定要走心。")
