#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/24/024 20:48
# @Author : zengsm
# @File : recongnition-number

import os

import cv2
import numpy as np
import tensorflow as tf
from keras import layers, optimizers, datasets
from keras.models import load_model
from matplotlib import pyplot as plt
from tensorflow import keras

""" 识别手写数字图像 tensorFlow 2.1 python 3.7"""

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# 下载训练数据集
(x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()
# 数据集格式转换
# 将图像转化为tensor的float32数据类型，并进行归一化处理
x_train, x_val = x_train / 255.0.x_test / 255.0
y_train = tf.cast(y_train, dtype=tf.int32)
y_test = tf.cast(y_test, dtype=tf.int32)

# 查看数据集的形状，60000张图片的训练集，图片大小为 28*28
# 打印训练集形状
print(x_train.shape, y_train.shape)
# 打印测试集形状
print(x_test.shape, y_test.shape)

# 生成测试集和训练集对象
# 通过使用tf.data.Dataset.from_tensor_slices(),把训练集直接转换成Dataset类的对象
train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
# batch设置为128 ，一次加载128张图片
train_dataset = train_dataset.shuffle(10000).batch(128)

## 测试集
test_dataset = tf.data.Dataset.from_tensor_slices((x_val, y_test))
# batch设置为128，一次加载128张图片
test_dataset = train_dataset.batch(128)
# 生成一个迭代器，作为sample 来查看每次迭代的batch
db_iter = iter(train_dataset)
sample = next(db_iter)
print('batch:', sample[0].shape, sample[1].shape)

## 建立模型
# 创建模型，模型包括5个卷积层和RELU激活函数，一个全连接输出层并使用softmax
model = keras.models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(512, activation='relu'),
    layers.Dense(256, activation='relu'),
    layers.Dense(128, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(10, activation='softmax')])
# 打印网络结构，调试的功能
print(model.summary())

# 设置模型的学习率参数
# 给出学习率(步长)进行更新
optimizser = optimizers.Adam(lr=0.001)
model.compile(optimizser=optimizser, loss='sparse_categorical_crossentropy',
              metrics='accuracy')
# 训练模型
model.fit(x_train, y_train, epochs=50)
# 保存模型，通常保存模型的权重
model.save('mnist.h5')

# 测试集验证模型
model1 = load_model('mnist.h5')
loss, acc = model1.evaluate(x_test, y_test, batch_size=128)
print("loss:", loss)
print("accuarcy:", acc)

## 识别数字图像
# 读取灰度图
img = cv2.imread('test.PNG')
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
plt.gray()
img = cv2.resize(img, (28, 28)) / 255
img = np.asanyarray(img, np.float32)
plt.imshow(img)
pred = model1.predict_classess(img.reshape(1, 28, 28))
print(pred)
