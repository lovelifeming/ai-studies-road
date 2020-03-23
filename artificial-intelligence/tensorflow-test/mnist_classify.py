#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/14/014 19:36
# @Author : zengsm
# @File : mnist_classify
import keras
import keras.datasets.mnist as  mnist
import matplotlib.pyplot as plt
from keras import layers

""" 手写数字识别 模型  python 3.7  TensorFlow 2.1 keras 2.3.1"""


def run_mnist():
    (train_image, train_label), (test_image, test_lable) = mnist.load_data()
    print(train_image.shape)  # 查看 image 信息
    print(train_label.shape)  # 查看 label 信息
    plt.imshow(train_image[2000])
    print(train_label[2000])
    print(test_image.shape, test_lable.shape)
    model = keras.Sequential()
    model.add(layers.Flatten())  # 展平成二维数据
    model.add(layers.Dense(64, activation='relu'))  # 全连接
    model.add(layers.Dense(10, activation='softmax'))  # 分类
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['acc'])
    model.fit(train_image, train_label, epochs=100, batch_size=512)


if __name__ == '__main__':
    run_mnist()
