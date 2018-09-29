# -*-coding:utf-8-*-

import importlib
import sys

importlib.reload(sys)

# 获取默认编码
print(sys.getdefaultencoding())


def Code(value):
	u = value
	print(u)
	repr(u)  # u'\u6c49'
	print(u)
	s = u.encode('UTF-8')
	print(s)
	repr(s)  # '\xe6\xb1\x89'
	print(u)
	u2 = s.decode('UTF-8')
	print
	repr(u2)  # u'\u6c49'
	print(u)


Code("test")
