#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/28 10:21
# @Author : zengsm
# @File : review-algorithm300
import requests

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}
def get_json(url):
    try:
        html=requests.get(url).json()
        return html
    except BaseException as e:
        print(e)
        print('获取网页失败')

def get_video(video_url,path):
    resouce=requests.get(video_url,headers=headers)
    with open(path,'wb')as f:
        f.write(resouce.content)

if __name__ == '__main__':
    for i in  range(2,4):
        url='https://www.ibilibili.com/video/av61259949?p=%s' % (i)
        html=get_json(url)
        print(html)


