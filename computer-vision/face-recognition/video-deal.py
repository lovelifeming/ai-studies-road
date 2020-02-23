#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/20/020 11:10
# @Author : zengsm
# @File : video-deal.py
import time

import cv2


def get_video_frame(source_url, target_url):
    """ """
    capture = cv2.VideoCapture(source_url)
    start = time.time()
    ret, frame = capture.read()
    flag = 0;
    while capture.isOpened() and ret:
        current = time.time()
        if flag%100 == 0:
            time_str = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(current))
            # start = current
            # cv2.imwrite(target_url + "\\images\\{}.jpg".format(time_str), frame)
            cv2.imwrite(target_url + "\\1468070-{}.jpg".format(flag), frame)
        flag += 1
        ret, frame = capture.read()


if __name__ == '__main__':
    get_video_frame("E:\\19074000-20235959\\IP监控点22_大运村_大运村_20200219102206_20200219155334_1468070.mp4"
                    , "E:\\19074000-20235959\\images")

