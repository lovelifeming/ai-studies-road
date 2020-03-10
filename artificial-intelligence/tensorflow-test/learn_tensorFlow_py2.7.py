#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/4/004 11:32
# @Author : zengsm
# @File : learn_tensorFlow_py2.7

import tensorflow as tf

""" 示例TensorFlow基本操作
    深度学习开发流程：准备数据 -》搭建模型-》迭代训练-》使用模型
    tensorFlow 1.8 python 2.7 """


def example_constant():
    # 常量计算示例
    a = tf.constant(3)  # 定义一个常量
    b = tf.constant(4)
    with tf.Session() as sess:
        print("相加：%i" % sess.run(a + b))
        print("相乘：%i" % sess.run(a * b))
    # 注入示例
    c = tf.placeholder(tf.int32)
    d = tf.placeholder(tf.int32)
    add = tf.add(c, d)
    mul = tf.multiply(c, d)
    with tf.Session() as sess:
        print("相加：%i" % sess.run(add, feed_dict={c: 3, d: 4}))
        print("相乘：%i" % sess.run(mul, feed_dict={c: 3, d: 4}))
        print(sess.run([add, mul], feed_dict={c: 3, d: 4}))


def example_variable():
    # 局部变量可以重复赋值，全局变量不可以重复赋值。
    var1 = tf.Variable(1.0, name='firstvar')
    print("var1:", var1.name)
    var1 = tf.Variable(2.0, name='firstvar')
    print("var1:", var1.name)
    var2 = tf.Variable(3.0)
    print("var2:", var2.name)
    var2 = tf.Variable(4.0)
    print("var2:", var2.name)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        print("var1=", var1.eval())
        print("var2=", var2.eval())
    get_var1 = tf.get_variable("firstvar", [1], initializer=tf.constant_initializer(0.3))
    print("get_var1:", get_var1.name)
    get_var1 = tf.get_variable("firstvar1", [1], initializer=tf.constant_initializer(0.4))
    print("get_var1:", get_var1.name)


def example_graph():
    """ 建立图 -》 获取张量 -》 获取节点操作 -》 获取元素列表 -》 获取对象"""
    # 1.创建图的方法
    const = tf.constant(0.0)
    graph = tf.Graph()  # 重新定义一个图
    with graph.as_default():
        const1 = tf.constant(0.0)
        print("const1", const1.graph)
        print("graph", graph)
        print("const.graph", const.graph)
    tf.reset_default_graph()  # 重新生成新图，把旧图销毁
    graph1 = tf.get_default_graph()
    print("graph1", graph1)
    print(const.name)
    t = graph.get_tensor_by_name(name="Const:0")
    print(t)


if __name__ == '__main__':
    # example_variable()  # TensorFlow 变量示例
    # example_constant()  # TensorFlow 常量示例
    example_graph()
