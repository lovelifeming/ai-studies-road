#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/28 10:47
# @Author : zengsm
# @File : day-hot
import requests
import random
import time
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"

}
def get_json(url,ajax):
    # 构建请求信息
    params = {
        'page_size':10,
        'next_offset': ajax,
        'tag':'今日热门',
        'platform':'pc'
    }
    # 防止请求失败
    try:
        html = requests.get(url,params=params,headers=headers).json()
        return html
    except BaseException:
        print('页面加载失败')
def get_video(viedeo_url,path):
    # 取出来视频的名称和地址
    r2 = requests.get(viedeo_url,headers=headers)
    with open(path,'wb')as f:
        f.write(r2.content)
if __name__ == '__main__':
    for i in range(3):
        url='http://api.vc.bilibili.com/board/v1/ranking/top?'
        num=i*10+1
        html=get_json(url,num)
        infos=html['data']['items']
        for info in infos:
            title = info['item']['description'] #小视频的标题
            video_url = info['item']['video_playurl']   #视频地址
            print(title,video_url)
            #为了防止视频没有video_url
            try:
                get_video(video_url,path=r"E:\app\视频\%s.mp4"%title)
                print("成功下载一个")
            except BaseException:
                print("下载失败")
                pass
        # 设置加载时间
        time.sleep(random.random() * 3)