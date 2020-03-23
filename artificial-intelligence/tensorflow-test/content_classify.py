#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/1/001 17:06
# @Author : zengsm
# @File : content-classify

import csv

import tensorflow as tf

""" 根据姓名判别性别 ，文本内容格式是：姓名 性别，例如：张三 男
    利用CNN神经网络训练文本分类
    资源：腾讯课堂 NLP--深度学习
    tensorFlow 1.8 python 2.7   """

tf.reset_default_graph()
name_dataset = "D:\\test.csv"

train_x = []
train_y = []

with open(name_dataset, 'r', encoding='utf-8')as csvfile:
    reader = csv.reader(csvfile)
    for sp in reader:
        if len(sp) == 2:
            train_x.append(sp[0])
            if sp[1] == '男':
                train_y.append([0, 1])
            else:
                train_y.append([1, 0])
# 获取最长内容长度，归一化统一内容长度，后面不空，方便后面
max_name_length = max([len(name) for name in train_x])
print("最长内容字符数：", max_name_length)
max_name_length = 8

counter = 0
# 建立字频表
vocabulary = {}
for name in train_x:
    counter += 1
    tokens = [word for word in name]
    for word in tokens:
        if word in vocabulary:
            vocabulary[word] += 1  # 重复出现则加1
        else:
            vocabulary[word] = 1

# 按照字频排序
vocabulary_list = [' '] + sorted(vocabulary, key=vocabulary.get(), reverse=True)
print(len(vocabulary_list))
print(vocabulary_list)
# 设置字频字典，为每一个字设置唯一标识
vocab = dict([(x, y) for (x, y) in enumerate(vocabulary_list)])
print(vocab)
# 为每一个字建立向量
train_x_vec = []

for name in train_x:
    name_vec = []
    for word in name:
        name_vec.append(vocab.get(word))
    while len(name_vec) < max_name_length:
        name_vec.append(0)
    train_x_vec.append(name_vec)

input_size = max_name_length
num_classes = 2

batch_size = 64
num_batch = len(train_x_vec) // batch_size

x = tf.placeholder(tf.int32, [None, input_size])
y = tf.placeholder(tf.float32, [None, num_classes])
dropout_keep_prob = tf.placeholder(tf.float32)


def neural_network(vocabulary_size, embedding_size=128, num_filters=128):
    # embedding layer
    with tf.name_scope("embdding"):
        w = tf.Variable(tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0))
        # 把名字对应的向量找出来
        embedding_chars = tf.nn.embedding_lookup(w, x)
        # 扩展成 (7,8,128,1) 加一个维度适应卷积网络的要求
        embedding_chars_expanded = tf.expand_dims(embedding_chars, -1)
    # convolution + maxpool layer
    filter_sizes = [1, 2, 3]
    pooled_output = []
    for i, filter_size in enumerate(filter_sizes):
        with tf.name_scope('conv-maxpool-%s' % filter_size):
            filter_shape = [filter_size, embedding_size, 1, num_filters]
            w = tf.Variable(tf.truncated_normal(filter_shape, stddev=0.1))
            print("w", w)
            b = tf.Variable(tf.constant(0.1, shape=[num_filters]))
            print("b", b)
            # 进行神经网络卷积
            conv = tf.nn.conv2d(embedding_chars_expanded, w, strides=[1, 1, 1, 1], padding="VALID")
            print("conv", conv)
            relu = tf.nn.relu(tf.nn.bias_add(conv, b))
            print("relu", relu)
            # 进行池化层
            pooled = tf.nn.max_pool(relu, ksize=[1, input_size - filter_size + 1, 1, 1], strides=[1, 1, 1, 1],
                                    padding="VALID")
            print("pooled", pooled)
            pooled_output.append(pooled)

    num_filters_total = num_filters * len(filter_sizes)
    h_pool = tf.concat(pooled_output, 3)  # 拼接池化层的结果
    h_pool_flat = tf.reshape(h_pool, [-1, num_filters_total])

    with tf.name_scope("dropout"):
        h_drop = tf.nn.dropout(h_pool_flat, dropout_keep_prob)
    # output
    with tf.name_scope("output"):
        w = tf.get_variable('w', shape=[num_filters_total, num_classes],
                            initializer=tf.contrib.layers.xavier_initializer())
        b = tf.Variable(tf.constant(0.1, shape=[num_classes]))
        output = tf.nn.xw_plus_b(h_drop, w, b)
    return output


def train_neural_network():
    output = neural_network(len(vocabulary_list))

    optimizer = tf.train.AdamOptimizer(le - 3)  # 定义一个优化器
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=output, labels=y))
    grads_and_vars = optimizer.compute_gradients(loss)
    train_op = optimizer.apply_gradients(grads_and_vars)

    saver = tf.train.Saver(tf.global_variables())
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for e in range(201):
            for i in range(num_batch):
                batch_x = train_x_vec[i * batch_size:(i + 1) * batch_size]
                batch_y = train_y[i * batch_size:(i + 1) * batch_size]
                _, loss_ = sess.run([train_op, loss], feed_dict={X: batch_x, Y: batch_y, dropout_keep_prob: 0.5})
                if i % 1000 == 0:
                    print("epoch:", e, "iter:", i, "loss:", loss_)
                if e % 100 == 0:
                    saver.save(sess, "./model/name2sex", global_step=e)


if __name__ == '__main__':
    train_neural_network()
