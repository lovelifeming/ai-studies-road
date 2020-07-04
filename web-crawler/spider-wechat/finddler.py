#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/30 13:42
# @Author : zengsm
# @File : finddler
#       https://cloud.tencent.com/developer/article/1592955
import requests
import re
import html
import json
import demjson

class WxCrawler(object):

    # 复制出来的 Headers，注意这个 x-wechat-key，有时间限制，会过期。当返回的内容出现 验证 的情况，就需要换 x-wechat-key 了
    headers = """Connection: keep-alive
        x-wechat-uin: MTY4MTI3NDIxNg%3D%3D
        x-wechat-key: 5ab2dd82e79bc5343ac5fb7fd20d72509db0ee1772b1043c894b24d441af288ae942feb4cfb4d234f00a4a5ab88c5b625d415b83df4b536d99befc096448d80cfd5a7fcd33380341aa592d070b1399a1
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (Linux; Android 10; GM1900 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 XWEB/992 MMWEBSDK/191102 Mobile Safari/537.36 MMWEBID/7220 MicroMessenger/7.0.9.1560(0x27000933) Process/toolsmp NetType/WIFI Language/zh_CN ABI/arm64
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/wxpic,image/apng,*/*;q=0.8
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,en-US;q=0.9
        Cookie: wxuin=1681274216; devicetype=android-29; version=27000933; lang=zh_CN; pass_ticket=JvAJfzySl6uLWYdYwzyQ+4OqrqiZ2zfaI4F2OCVR7omYOmTjYNKalCFbr75X+T6K; rewardsn=; wxtokenkey=777; wap_sid2=COjq2KEGElxBTmotQWtVY2Iwb3BZRkIzd0Y0SnpaUG1HNTQ0SDA4UGJOZi1kaFdFbkl1MHUyYkRKX2xiWFU5VVhDNXBkQlY0U0pRXzlCZW9qZ29oYW9DWmZYOTdmQTBFQUFBfjD+hInvBTgNQJVO
        X-Requested-With: com.tencent.mm"""

    url = "https://mp.weixin.qq .com/mp/profile_ext?action=home&__biz=MjEwNDI4NTA2MQ==&scene=123&devicetype=android-29&version=27000933&lang=zh_CN&nettype=WIFI&a8scene=7&session_us=wxid_2574365742721&pass_ticket=JvAJfzySl6uLWYdYwzyQ%2B4OqrqiZ2zfaI4F2OCVR7omYOmTjYNKalCFbr75X%2BT6K&wx_header=1"


    # 将 Headers 转换为 字典
    def header_to_dict(self):
        headers = self.headers.split("\n")
        headers_dict = dict()
        for h in headers:
            k,v = h.split(":")
            headers_dict[k.strip()] = v.strip()
        return headers_dict;


    def run(self):
        headers = self.header_to_dict()
        response = requests.get(self.url, headers=headers, verify=False)

        print(response.text)

def article_list(self, context):
    rex = "msgList = '({.*?})'"
    pattern = re.compile(pattern=rex, flags=re.S)
    match = pattern.search(context)
    if match:
        data = match.group(1)
        data = html.unescape(data)
        data = json.loads(data)
        articles = data.get("list")
        return articles

##########      解析单个文章
# 获取单个文章的URL
content_url_array = []

def content_url(self, articles):
    content_url = []
    for a in articles:
        a = str(a).replace("\/", "/")
        a = demjson.decode(a)
        content_url_array.append(a['app_msg_ext_info']["content_url"])
        # 取更多的
        for multi in a['app_msg_ext_info']["multi_app_msg_item_list"]:
            self.content_url_array.append(multi['content_url'])
    return content_url
# 解析单个文章
def parse_article(self, headers, content_url):
    for i in content_url:
        content_response = requests.get(i, headers=headers, verify=False)
        with open("wx.html", "wb") as f:
            f.write(content_response.content)
        html = open("wx.html", encoding="utf-8").read()
        soup_body = BeautifulSoup(html, "html.parser")
        context = soup_body.find('div', id = 'js_content').text.strip()
        print(context)
def page(self, headers):
    response = requests.get(self.page_url, headers=headers, verify=False)
    result = response.json()
    if result.get("ret") == 0:
        msg_list = result.get("general_msg_list")
        msg_list = demjson.decode(msg_list)
        self.content_url(msg_list["list"])
        #递归
        self.page(headers)
    else:
        print("无法获取内容")

#############

if __name__ == "__main__":

    wx = WxCrawler()
    wx.run()