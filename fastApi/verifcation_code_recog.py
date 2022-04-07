#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/7
# @Author : zengsm
# @File : verifcation_code_recognitionslefocr @Description:
import base64
import logging
import urllib.request

from ddddocr import DdddOcr


def verifcationCodeByUrl(picUrl:str):
    ocr = DdddOcr()
    urlopen = urllib.request.urlopen(picUrl)
    img = urlopen.read()
    res = ocr.classification(img)
    print(res)
    return res
def verifcationCodeByB64(picBase64:str):
    ocr = DdddOcr()
    imgdata = base64.b64decode(picBase64)
    res = ocr.classification(imgdata)
    print(res)
    return res

if __name__ == '__main__':
    with open("E:\\8296.png","rb") as f:#转为二进制格式
        base64_data = base64.b64encode(f.read()) #使用base64进行加密
        print(base64_data)
        code = verifcationCodeByB64(base64_data)
        print(code)
        # file=open('1.txt','wt')#写成文本格式
        # file.write(base64_data)
        # file.close()
