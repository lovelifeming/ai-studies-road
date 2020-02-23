# -*-coding:utf-8-*-


def bytes_convert_str(value: str):
	# 字符串转字节
	print('定义字节：' + str(b'this is bytes'))
	str_bytes = bytes(value, encoding='utf-8')
	print('bytes()方式字符转字节：' + str(str_bytes))
	print('str.encode()方式字符转字节：' + str(str.encode(value, encoding='utf-8')))
	print('s.encode()方式字符转字节：' + str(value.encode('utf-8')))
	# 字节转字符串
	print('bytes.decode()方式字节转字符：' + bytes.decode(str_bytes, encoding='utf-8'))
	print('s.decode()方式字节转字符：' + str_bytes.decode('utf-8'))
	bytes_str = str(str_bytes, encoding='utf-8')
	print('str()方式字节转字符：' + bytes_str)


def init_collection():
	""" 集合对象声明  """
	# set集合：不重复无序列集合
	set_collection = set()
	set_collection1 = {'a', 'b', 'a'}
	# 字典：有序列 key-value键值对，后面覆盖前面重复元素
	dict_collection = dict()
	dict_collection1 = {1: 'a', 2: 'b', 3: 'a', 3: 'c'}
	# 数字：有序列集合，后面覆盖前面重复元素
	list_collection = list()
	list_collection1 = ['a', 'b', 'c', 1, 'a']
	# 元组：有序列不同类型集合，后面覆盖前面重复元素
	tuple_collection = tuple()
	tuple_collection1 = (1, 2, 3, 'example', 2)
	print(type(set_collection))  # <class 'set'>
	print(type(set_collection1))  # <class 'set'>
	print(type(dict_collection))  # <class 'dict'>
	print(type(dict_collection1))  # <class 'dict'>
	print(type(list_collection))  # <class 'list'>
	print(type(list_collection1))  # <class 'list'>
	print(type(tuple_collection))  # <class 'tuple'>
	print(type(tuple_collection1))  # <class 'tuple'>


if __name__ == '__main__':
	bytes_convert_str('test')
	init_collection()
