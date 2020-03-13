#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/1/001 10:54
# @Author : zengsm
# @File : wechat
import os
import time
import xml

import itchat
from itchat.content import *

""" TEXT = 'Text' MAP = 'Map' CARD = 'Card' NOTE = 'Note' SHARING = 'Sharing' PICTURE = 'Picture'
RECORDING = VOICE = 'Recording' ATTACHMENT = 'Attachment' VIDEO = 'Video' FRIENDS = 'Friends'
SYSTEM = 'System'   INCOME_MSG = [TEXT, MAP, CARD, NOTE, SHARING, PICTURE,
RECORDING, VOICE, ATTACHMENT, VIDEO, FRIENDS, SYSTEM]"""

itchat.login()  # 自动登录 itchat.auto_login(hotReload=True)
friends = itchat.get_friends()  # 好友列表   昵称、备注名、地址、个性签名、性别等
print(friends)

# 这是保存撤回消息的文件目录(如：图片、语音等)，这里已经写死了，大家可以自行修改
temp = 'C:/Users/Administrator/Desktop/CrawlerDemo' + '/' + '撤回的消息'
if not os.path.exists(temp):
    os.mkdir(temp)
dict = {}  # 定义一个字典
global dict  # 声明全局变量


# 这是一个装饰器，给下面的函数添加新功能
# 能够捕获好友发送的消息，并传递给函数参数msg
@itchat.msg_register([TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO, NOTE])
def resever_info(msg):  # 监听系统消息
    print(msg)
    info = msg['Text']  # 取出文本消息
    info_type = msg['Type']  # 取出消息类型
    name = msg['FileName']  # 取出语音(图片)文件名
    msgId = msg['MsgId']  # 取出消息标识
    ticks = msg['CreateTime']  # 获取信息发送的时间

    # 取出消息发送者标识并从好友列表中检索
    fromUser = itchat.search_friends(userName=msg['FromUserName'])['NickName']
    ticks = msg['CreateTime']  # 获取信息发送的时间
    time_local = time.localtime(ticks)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)  # 格式化日期
    # 将消息标识和消息内容添加到字典
    # 每一条消息的唯一标识作为键，消息的具体信息作为值，也是一个字典
    dict[msgId] = {"info": info, "info_type": info_type, "name": name, "fromUser": fromUser, "dt": dt}
    print("发送人:" + fromUser + '\n消息类型:' + info_type + '\n发送时间:' + dt + '\n消息内容:' + info)
    if info_type == 'Recording':
        info(temp + '/' + name)
    elif info_type == 'Picture':
        info(temp + '/' + name)  # 保存图片


@itchat.msg_register(NOTE)  # 监听系统提示
def note_info(msg):
    # 监听到好友撤回了一条消息
    if '撤回了一条消息' in msg['Text']:
        # 获取系统消息中的Content结点值
        content = msg['Content']
        # Content值为xml，解析xml
        doc = xml.dom.minidom.parseString(content)
        # 取出msgid标签的值
        result = doc.getElementsByTagName("msgid")
        # 该msgId就是撤回的消息标识，通过它可以在字典中找到撤回的消息信息
        msgId = result[0].childNodes[0].nodeValue
        # 从字典中取出对应消息标识的消息类型
        msg_type = dict[msgId]['info_type']
        if msg_type == 'Recording':  # 撤回的消息为语音
            recording_info = dict[msgId]['info']  # 取出消息标识对应的消息内容
            info_name = dict[msgId]['name']  # 取出消息文件名
            fromUser = dict[msgId]['fromUser']  # 取出发送者
            dt = dict[msgId]['dt']  # 取出发送时间
            recording_info(temp + '/' + info_name)  # 保存语音
            # 拼接提示消息
            send_msg = '【发送人:】' + fromUser + '\n' + '发送时间:' + dt + '\n' + '撤回了一条语音'
            itchat.send(send_msg, 'filehelper')  # 将提示消息发送给文件助手
            # 发送保存的语音
            itchat.send_file(temp + '/' + info_name, 'filehelper')
            del dict[msgId]  # 删除字典中对应的消息
            print("保存语音")
        elif msg_type == 'Text':
            text_info = dict[msgId]['info']  # 取出消息标识对应的消息内容
            fromUser = dict[msgId]['fromUser']  # 取出发送者
            dt = dict[msgId]['dt']  # 取出发送时间
            # 拼接提示消息
            send_msg = '【发送人:】' + fromUser + '\n' + '发送时间:' + dt + '\n' + '撤回内容:' + text_info
            # 将提示消息发送给文件助手
            itchat.send(send_msg, 'filehelper')
            del dict[msgId]  # 删除字典中对应的消息
            print("保存文本")
        elif msg_type == 'Picture':
            picture_info = dict[msgId]['info']  # 取出消息标识对应的消息内容
            fromUser = dict[msgId]['fromUser']  # 取出发送者
            dt = dict[msgId]['dt']  # 取出发送时间
            info_name = dict[msgId]['name']  # 取出文件名
            picture_info(temp + '/' + info_name)  # 保存图片
            # 拼接提示消息
            send_msg = '【发送人:】' + fromUser + '\n' + '发送时间:' + dt + '\n' + '撤回了一张图片'
            itchat.send(send_msg, 'filehelper')  # 将图片发送给文件助手
            # 发送保存的语音
            itchat.send_file(temp + '/' + info_name, 'filehelper')
            del dict[msgId]  # 删除字典中对应的消息
            print("保存图片")


itchat.run()  # 保持运行
