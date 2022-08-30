#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/26
# @Author : zengsm
# @File : common @Description:

import base64

from Crypto.Cipher import AES


# 补足字符串长度为16的倍数
def add_to_16(s):
    while len(s) % 16 != 0:
        s += '\0'
    return str.encode(s)  # 返回bytes

key = '244F3C2C1AB08F70'.upper()
key = 'skyeyesensor?000'  # 密钥长度必须为16、24或32位，分别对应AES-128、AES-192和AES-256
text = 'jwwl@tz1-xxaqb'  # 待加密文本
if __name__ == '__main__':

    aes = AES.new(str.encode(key), AES.MODE_ECB)  # 初始化加密器，本例采用ECB加密模式
    encrypted_text = str(base64.encodebytes(aes.encrypt(add_to_16(text))), encoding='utf8').replace('\n', '')  # 加密
    decrypted_text = str(
        aes.decrypt(base64.decodebytes(bytes(encrypted_text, encoding='utf8'))).rstrip(b'\0').decode("utf8"))  # 解密

    print('加密值：', encrypted_text)
    print('解密值：', decrypted_text)
