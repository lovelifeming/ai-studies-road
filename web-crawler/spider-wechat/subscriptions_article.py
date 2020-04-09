#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/12/012 14:04
# @Author : zengsm
# @File : subscriptions_article
# 参考资料  https://www.zhihu.com/question/31285583/answer/850969561

import json
import re
import time

import jsonpath
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Host": "mp.weixin.qq.com",
    "Referer": "https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit&action=edit&type=10&isMul=1&isNew=1&lang=zh_CN&token=1862390040",
    "Cookie": "自己获取信息时的cookie"
}
# from pymongo import MongoClient

url = 'https://mp.weixin.qq.com/s/Fxf5q8Z1vOzJwE-zmjmTgQ'  # （公众号不让添加主页链接，xxx表示profile_ext)


def getInfo():
    for i in range(80):
        # token  random 需要要自己的   begin：参数传入
        url = "https://mp.weixin.qq.com/cgi-bin/appmsg?token=1904193044&lang=zh_CN&f=json&ajax=1&random=0.9468236563826882&action=list_ex&begin={}&count=5&query=&fakeid=MzI4MzkzMTc3OA%3D%3D&type=9".format(
            str(i * 5))

        response = requests.get(url, headers=headers)

        jsonRes = response.json()

        titleList = jsonpath.jsonpath(jsonRes, "$..title")
        coverList = jsonpath.jsonpath(jsonRes, "$..cover")
        urlList = jsonpath.jsonpath(jsonRes, "$..link")

        # 遍历 构造可存储字符串
        for index in range(len(titleList)):
            title = titleList[index]
            cover = coverList[index]
            url = urlList[index]

            scvStr = "%s,%s, %s,\n" % (title, cover, url)
            with open("info.csv", "a+", encoding="gbk", newline='') as f:
                f.write(scvStr)


url_wxv = ""
response = requests.get(url_wxv, headers=headers)

# 我用的是正则，也可以使用xpath
jsonRes = response.text  # 匹配:wxv_1105179750743556096
dirRe = r"wxv_.{19}"
result = re.search(dirRe, jsonRes)

wxv = result.group(0)
print(wxv)


def getVideo(video_title, url_wxv):
    video_path = './videoFiles/' + video_title + ".mp4"

    # 页面可下载形式
    video_url_temp = "https://mp.weixin.qq.com/mp/videoplayer?action=get_mp_video_play_url&preview=0&__biz=MzI4MzkzMTc3OA==&mid=2247488495&idx=4&vid=" + wxv
    response = requests.get(video_url_temp, headers=headers)
    content = response.content.decode()
    content = json.loads(content)
    url_info = content.get("url_info")
    video_url2 = url_info[0].get("url")
    print(video_url2)

    # 请求要下载的url地址
    html = requests.get(video_url2)
    # content返回的是bytes型也就是二进制的数据。
    html = html.content
    with open(video_path, 'wb') as f:
        f.write(html)


# Mongo配置
# conn = MongoClient('127.0.0.1', 27017)
# db = conn.wx  #连接wx数据库，没有则自动创建
# mongo_wx = db.article  #使用article集合，没有则自动创建

def get_wx_article(biz, uin, key, index=0, count=10):
    """ __biz : 用户和公众号之间的唯一id，
        uin ：用户的私密id
        key ：请求的秘钥，一段时候只会就会失效。
        offset ：偏移量
        count ：每次请求的条数      """
    offset = (index + 1) * count
    params = {
        '__biz': biz,
        'uin': uin,
        'key': key,
        'offset': offset,
        'count': count,
        'action': 'getmsg',
        'f': 'json'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    }

    response = requests.get(url=url, params=params, headers=headers)
    resp_json = response.json()
    if resp_json.get('errmsg') == 'ok':
        resp_json = response.json()
        # 是否还有分页数据， 用于判断return的值
        can_msg_continue = resp_json['can_msg_continue']
        # 当前分页文章数
        msg_count = resp_json['msg_count']
        general_msg_list = json.loads(resp_json['general_msg_list'])
        list = general_msg_list.get('list')
        print(list, "**************")
        for i in list:
            app_msg_ext_info = i['app_msg_ext_info']
            # 标题
            title = app_msg_ext_info['title']
            # 文章地址
            content_url = app_msg_ext_info['content_url']
            # 封面图
            cover = app_msg_ext_info['cover']

            # 发布时间
            datetime = i['comm_msg_info']['datetime']
            datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(datetime))
            print('title', title, 'content_url', content_url, 'cover', cover, 'datetime', datetime)
            # mongo_wx.insert({
            #     'title': title,
            #     'content_url': content_url,
            #     'cover': cover,
            #     'datetime': datetime
            # })
        if can_msg_continue == 1:
            return True
        return False
    else:
        print('获取文章异常...')
        return False


if __name__ == '__main__':
    biz = 'Mzg4MTA2Nzg0NA=='
    uin = 'NDIyMTI5NDM1'
    key = '20a680e825f03f1e7f38f326772e54e7dc0fd02ffba17e92730ba3f0a0329c5ed310b0bd55' \
          'b3c0b1f122e5896c6261df2eaea4036ab5a5d32dbdbcb0a638f5f3605cf1821decf486bb6eb4d92d36c620'
    index = 0
    while 1:
        print(f'开始抓取公众号第{index + 1} 页文章.')
        flag = get_wx_article(biz, uin, key, index=index)
        # 防止和谐，暂停8秒
        time.sleep(8)
        index += 1
        if not flag:
            print('公众号文章已全部抓取完毕，退出程序.')
            break
        print(f'..........准备抓取公众号第{index + 1} 页文章.')
