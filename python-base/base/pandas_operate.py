#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/18 15:50
# @File : pandas_operate
import random

import numpy as np
import pandas as pd
from pandas import datetime


def create_dataframe():
    random.seed(1)
    rnd1 = [random.randrange(1, 20) for x in range(40)]
    rnd2 = [random.randrange(1, 20) for x in range(40)]
    rnd3 = [random.randrange(1, 20) for x in range(40)]
    daytime = pd.date_range('2020-11-09', '2020-12-18')
    data = pd.DataFrame({'daytime': daytime, 'rnd1': rnd1, 'rnd2': rnd2, 'rnd3': rnd3})
    return data


def dataframe_operate():
    """ loc可以按照索引的值来进行行列选择，包含结尾。
        iloc是按照索引的位置来进行选取，不关心索引的具体值是多少，只关心位置是多少，所以使用iloc时方括号中只能使用数值。
        at的使用方法与loc类似，但是比loc有更快的访问数据的速度，只能访问单个元素，不能访问多个元素。
        iat对于iloc的关系就像at对于loc的关系，是一种更快的基于索引位置的选择方法，同at一样只能访问单个元素。
        df[['A列名','B列名']]   #选取列
        df[df['status']=='active']   #选取status列值为active的行数据
        df[df['status'].isnull()]   #选取status列值为空的行数据
        df[df['status'].isin(['waiting', 'running'])]   #选取status列值为waiting 和running的行数据
        df.sort_values(by='active',ascending=False)         # df以active 列降序排序
        gb=df.groupby('active', sort=False)        #df以active 列数据分组
        gy.groups.keys()
        gy.get_group(190)['A']
        g.get_group(k).head(n)

    """
    data = create_dataframe()
    print('DataFrame数据表：\n', data)
    print('DataFrame统计：\n', data.describe())
    print('DataFrame列索引名称：\n', data.columns)
    print('DataFrame行索引名称：\n', data.index)
    print('DataFrame总计行：', len(data), ' 列：', data.columns.size)
    print('DataFrame等于10的数据：\n', data[data == 10])
    print('DataFrame中rnd1大于10的数据：\n', data[data.rnd1 > 10])
    print('DataFrame统计各个值个数：\n', data['rnd2'].value_counts())

    print('DataFrame切取2之5行：\n', data[2:5])  # 前闭后开，包括前不包括后
    print('DataFrame loc取2之5行：\n', data.loc[2:5])
    print('DataFrame提取列[[]]：\n', data[['rnd1', 'rnd3']])  # 返回的是DataFrame属性
    print('DataFrame提取列.：\n', data.rnd1)  # 返回的是Series类型
    print('DataFrame提取列[]：\n', data['rnd1'])  # 返回的是Series类型
    print('DataFrame提取列[[]]：\n', data[['rnd1']])
    print('DataFrame提取前3行：\n', data.head(3))
    print('DataFrame提取后3行：\n', data.tail(3))
    print('DataFrame区块选择：\n', data[3:6][['rnd1', 'rnd3']])
    print('DataFrame loc区块选择：\n', data.loc[3:6, ['rnd1', 'rnd3']])
    print('DataFrame提取第四行二列：\n', data.iat[3, 2])

    index = data.set_index('daytime')  # 将行索引设定为日期
    print('设置日期列为索引：\n', index.head())
    # 生成两个特定日期
    startday = datetime(2020, 11, 12)
    endday = datetime(2020, 11, 16)
    print('DataFrame loc建索引切取：\n', index.loc[startday:endday])
    print('DataFrame iloc行选择最后一行：', type(index.iloc[-1]), '\n', index.iloc[-1])  # 选取DataFrame最后一行，返回的是Series
    print('DataFrame iloc行选择最后一行：', type(index.iloc[-1:]), '\n', index.iloc[-1:])  # 选取DataFrame最后一行，返回的是DataFrame
    print('DataFrame iloc行选择：\n', index.iloc[2:5, :])
    print('DataFrame iloc列选择：\n', index.iloc[:, [1, 2]].head())
    print('DataFrame iloc区块选择：\n', index.iloc[[1, 2, 2], [1, 2]])
    dt = data[data['rnd1'].isin([2, 6, 8, 10])]
    print('DataFrame选取特定行：\n', dt)
    dt = data[~data['rnd1'].isin([2, 6, 8, 10])]
    print('DataFrame排除特定行：\n', dt)

    # 选取某行含有特定数值的列
    cols = [x for i, x in enumerate(data.columns) if len(set([13]) & set(data.iloc[:, i].values.tolist())) > 0]
    # 利用enumerate对row0进行遍历，将含有数字3的列放入cols中
    print('选取列：', cols)
    # df1=data[cols]   选取含有特定数值的列
    df1 = data.drop(cols, axis=1)  # 利用drop方法将含有特定数值的列删除
    print('排除特定数值列', df1)


def dataframe_groupby():
    df = create_dataframe()
    gb = df.groupby(by='rnd1')
    print('DataFrame.groupby()求最大值：\n', gb.max())
    print('DataFrame.groupby()求最小值：\n', gb.min())
    print('DataFrame.groupby()分组keys：\n', gb.keys)
    print('DataFrame.groupby()分组keys值：\n', gb.groups.keys())
    print('DataFrame.groupby()分组rnd1统计：\n', gb['rnd1'].value_counts())
    print('DataFrame.groupby()统计：\n', gb.describe)
    print('DataFrame.groupby()选择最后一行值分组的daytime：\n', gb.get_group(int(df.iloc[-1]['rnd1']))['daytime'])
    print('DataFrame.groupby()选择第一个分组的前三行：\n', gb.get_group(list(gb.groups.keys())[3]).head(3))


def dataframe_query_eval():
    """DataFrame.query(expr, inplace=False, **kwargs)参数说明：
        expr：引用字符串形式的表达式以过滤数据。
        inplace：如果该值为True, 它将在原始DataFrame中进行更改。
        kwargs：引用其他关键字参数。
        Pandas.eval()与DataFrame.eval()类似，都支持表达式操作，注意操作是否符合表达式的数据类型，运算操作只能是数字。
        Pandas.eval()支持多个DataFrame操作，DataFrame.eval()是对自身的数据做操作。
    """
    keys = [10, 12, 16]
    df = create_dataframe()
    sv = df.sort_values(by='rnd2', ascending=True)
    print('DataFrame求个列总和：\n', sv.sum())
    print('DataFrame.sort_values()统计：\n', sv.describe())
    print('DataFrame.query()筛选过滤：\n', sv.query('rnd1 > @keys[0] and rnd2 < @keys[1]'))
    print('DataFrame.query()筛选过滤：\n', sv.query('rnd1 > 10 and rnd2 < 12'))
    print('DataFrame.eval()算术运算：\n', sv.eval('-rnd1 * rnd2 / rnd3 + ( rnd2 + rnd3 )'))
    print('DataFrame.eval()比较运算：\n', sv.eval('rnd1 <= rnd2 !=rnd3'))
    print('DataFrame.eval()位运算：\n', sv.eval('(rnd1< @keys[0]) &(rnd2 < @keys[1]) | (rnd3 < @keys[2])'))
    print('DataFrame.eval()列计算：\n', sv.eval('(rnd1 + rnd2 + rnd3)/3'))
    print('DataFrame.eval()新增列：\n', sv.eval('rowmean = (rnd1 + rnd2 + rnd3)/3', inplace=True))
    print('DataFrame.eval()列操作：\n', sv.eval('rnd1+10'))
    df1 = pd.DataFrame(np.random.randint(0, 20, (100, 3)))
    df2 = pd.DataFrame(np.random.randint(0, 20, (100, 3)))
    df3 = pd.DataFrame(np.random.randint(0, 20, (100, 3)))
    print('Pandas.eval()算术运算：\n', pd.eval('(df1 + df2) / df3'))


if __name__ == '__main__':
    print('......start......')
    # dataframe_operate()
    # dataframe_groupby()
    dataframe_query_eval()
    print('......end......')
