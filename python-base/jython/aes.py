#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/9/29 11:10
# @Author : zengsm
# @File : aes.py

import subprocess
import chardet
import sys


class AES(object):
	def __init__(self, data, key):
		self.data = data
		self.key = key

	def decrypt(self):
		command = "java -jar aes.jar"
		arg0 = self.data
		arg1 = self.key
		cmd = [command, arg0, arg1]
		new_cmd = " ".join(cmd)
		stdout, stderr = subprocess.Popen(new_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
		encoding = chardet.detect(stdout)["encoding"]
		result = stdout.decode(encoding)
		return result


if __name__ == '__main__':
	data = sys.argv[1]
	key = sys.argv[2]
	AES = AES(data, key)
	print(AES.decrypt())
