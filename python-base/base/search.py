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


def re_example(**kwargs):
    """ 正则表达式规则：
        ^ 匹配字符串的开始。
        $ 匹配字符串的结尾。
        \b 匹配一个单词的边界。
        \d 匹配任意数字。
        \D 匹配任意非数字字符。
        x? 匹配一个可选的 x 字符 (换言之，它匹配 1 次或者 0 次 x 字符)。
        x* 匹配0次或者多次 x 字符。
        x+ 匹配1次或者多次 x 字符。
        x{n,m} 匹配 x 字符，至少 n 次，至多 m 次。
        (a|b|c) 要么匹配 a，要么匹配 b，要么匹配 c。
        (x) 一般情况下表示一个记忆组 (remembered group)。你可以利用 re.search 函数返回对象的 groups() 函数获取它的值。
        .正则表达式中的点号通常意味着 “匹配任意单字符“ """
    content = kwargs.pop('content')
    # \d+.?\d* 匹配数字，包括整数，小数
    pattern = r'\d+.?\d*'
    digit = re.findall(pattern, content)
    print(digit)  # ['1.8', '2.0', '6 ', '8.8', '0.16', '0.18', '3.141', '592.65']


def html_example(**kwargs):
    """ 移除html 标签，转换特殊符号"""
    exclude_word = ['&nbsp;', '&emsp;', '&ensp;']
    replace_word = {'&lt;': '< ', '&gt;': '>', '&amp;': '&', '&quot;': '"', '&reg;': '®', '&copy;': '©', '&trade;': '™'}
    content = kwargs.pop("content")
    cont = re.sub(r'</?\w+[^>]*>', '', content)
    for x in exclude_word:
        cont = cont.replace(x, '')
    for k, v in replace_word.items():
        cont = cont.replace(k, v)
    return cont


if __name__ == '__main__':
    key = multi_key("策略|技巧|领导", "批评家应该谈论策略，作为一个领导者，你不能太任性，否则真的没有效果。"
                                "把它轻轻放在不能触及灵魂的地方，而把它认真放在容易产生抵触，如果你不发脾气，你的下属就"
                                "不会记得。如果你发脾气，你的下属会认为领导只是在发泄。因此，领导批评人应注意三个原则："
                                "公开批评，责人先责己；说话一定要有技巧，尝试以人制人；将心比心，一定要走心。")
    re_example(content='price a1.8 b2.0 c6 d 8.8 e0.16 f .0.18 3.141.592.65')
