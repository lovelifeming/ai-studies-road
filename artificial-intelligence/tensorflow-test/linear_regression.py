#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/9/009 21:38
# @Author : zengsm
# @File : linear_regression

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.python.tools.inspect_checkpoint import print_tensors_in_checkpoint_file as ptf


def linear_regression():
    # 1.生成模拟数据
    plotdata = {"batchsize": [], "loss": []}  # 生成字典记录训练批次及loss值
    train_x = np.linspace(-1, 1, 100)  # 生成100 个 -1到1之间的数据
    train_y = 2 * train_x + np.random.randn(100) * 0.3  # Y=2x ,并加入噪声
    # 显示模拟数据点
    plt.plot(train_x, train_y, "ro", label='Original data')
    plt.legend()
    plt.show()

    # 2.搭建模型
    tf.reset_default_graph()  # 重新初始化图
    X = tf.placeholder('float')  # 初始化占位符
    Y = tf.placeholder('float')
    # 模型参数
    W = tf.Variable(tf.random_normal([1]), name='weight')
    B = tf.Variable(tf.zeros([1]), name='bias')
    Z = tf.multiply(X, W) + B  # 前向结构
    tf.summary.histogram('Z',Z)
    cost = tf.reduce_mean(tf.square(Y - Z))  # 反向优化(均方差)(1,2,3,4)[2,3,3,4]
    tf.summary.scalar('loss_function',cost) #
    learning_rate = 0.01  # 学习率
    # 使用tf的梯度下降优化器设定的学习率不断优化 W 和 b使loss最小化，最终使z 与y的误差最小
    optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

    # 3.迭代训练模型
    init = tf.global_variables_initializer()  # 初始化变量
    training_epochs = 20  # 训练迭代次数
    display_step = 1  # 打印频率，每2步打印输出一次
    # 生成saver  max_to_keep=1只保存一份模型,每一步都可以保存一次
    # saver = tf.train.Saver([W, B], max_to_keep=1)
    saver = tf.train.Saver()  # 生成saver
    save_dir = "resource/model/"
    # 启动 session
    with tf.Session() as sess:
        sess.run(init)
        # Fit all training data
        for epoch in range(training_epochs):
            for (x, y) in zip(train_x, train_y):
                sess.run(optimizer, feed_dict={X: x, Y: y})
            # 打印训练中的详细信息
            if epoch % display_step == 0:
                loss = sess.run(cost, feed_dict={X: train_x, Y: train_y})
                print("Epoch=", epoch + 1, "loss=", loss, "W=", sess.run(W), "B=", B)
                if not (loss == 'NA'):
                    plotdata["batchsize"].append(epoch)
                    plotdata["loss"].append(loss)
                # saver.save(sess, save_dir + "linermodel.cpkt", global_step=epoch)  # 每一步都保存一次
        print("model training finish!")
        saver.save(sess, save_dir + "linermodel.cpkt")  # 保存模型
        print("loss=", sess.run(cost, feed_dict={X: train_x, Y: train_y}), "B=", B)

        # 显示图形
        plt.plot(train_x, train_y, 'ro', label='Original data')
        plt.plot(train_x, sess.run(W) * train_x + sess.run(B), label='Fitted line')
        plt.legend()
        plt.show()

        plotdata["avgloss"] = moving_average(plotdata["loss"])
        plt.figure(1)
        plt.subplot(211)
        plt.plot(plotdata["batchsize"], plotdata["avgloss"], "b--")  # b-- 图形展示样式
        plt.xlabel("Minibatch number")
        plt.ylabel("Loss")
        plt.title("Minibatch run vs.Training loss")
        plt.show()
        print ("x=0.2,2=", sess.run(Z, feed_dict={X: 0.2}))


def moving_average(a, w=10):
    if len(a) < w:
        return a[:]
    return [val if idx < w else sum(a[(idx - w):idx]) / w for idx, val in enumerate(a)]


def restore_session():
    """ 导入训练好的模型 """
    X = tf.placeholder('float')  # 初始化占位符
    # Y = tf.placeholder('float')
    # 模型参数
    W = tf.Variable(tf.random_normal([1], name='weight'))
    B = tf.Variable(tf.zeros([1], name='bias'))
    Z = tf.multiply(X, W) + B  # 前向结构
    saver = tf.train.Saver({'weight': W, 'bias': B})  # 生成saver
    save_dir = r"resource/model/"
    file_path = tf.train.latest_checkpoint(save_dir)  # 获取最新的模型文件
    kpt = tf.train.get_checkpoint_state(save_dir)  # 检查获取可以用的模型文件
    print("kpt=", kpt)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        print("file_path:", file_path)
        if kpt is not None:
            saver.restore(sess, kpt.model_checkpoint_path)
            print("x=0.2,z=", sess.run(Z, feed_dict={X: 0.2}))
        else:
            print("模型文件路径有误")


def check_session_information():
    """ 查看模型里面的参数"""
    save_dir = "resource/model/"
    ptf(save_dir + "linermodel.cpkt", None, True, True)
    W = tf.Variable(1.0, name='weight')
    B = tf.Variable(2.0, name='bias')
    saver = tf.train.Saver({"weight": B, 'bias': W})
    state = tf.train.get_checkpoint_state(save_dir)  # 检查获取可以用的模型文件
    print("state=", state)
    latest = tf.train.latest_checkpoint(save_dir)  # 获取最新的模型文件
    print("latest=", latest)
    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        saver.save(sess, save_dir + 'linermodel.cpkt')
    ptf(save_dir + 'linermodel.cpkt', None, True, True)


if __name__ == '__main__':
    # linear_regression()
    # restore_session()
    check_session_information()

    print('Finished!')
