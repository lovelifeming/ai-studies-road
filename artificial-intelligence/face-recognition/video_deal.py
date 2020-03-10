#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/20/020 11:10
# @Author : zengsm
# @File : video_deal.py
import os
import time

import cv2


def get_video_frame(source_url, target_dir):
    """ 读取视频流，截取视频图片"""
    capture = cv2.VideoCapture(source_url)
    start = time.time()
    ret, frame = capture.read()
    flag = 0
    while capture.isOpened() and ret:
        current = time.time()
        if flag % 100 == 0:
            time_str = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(current))
            # start = current
            # cv2.imwrite(target_url + "\\images\\{}.jpg".format(time_str), frame)
            cv2.imwrite(target_dir + "\\test-{}.jpg".format(flag), frame)
        flag += 1
        ret, frame = capture.read()


def cut_picture(source_dir, target_dir):
    """ 截取图片的部分内容 """
    files = os.listdir(source_dir)
    for file in files:
        img = cv2.imread(os.path.join(source_dir, file))
        # 截取图片纵坐标范围，横坐标范围
        img = img[231:1080, 947:1920, :]
        cv2.imwrite(os.path.join(target_dir, file), img)


if __name__ == '__main__':
    get_video_frame("D:\\test.mp4", "E:\\images")
    cut_picture(r"D:\\labelImg-target", "D:\\labelImg-source")
