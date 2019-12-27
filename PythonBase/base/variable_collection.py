# -*-coding:utf-8-*-
import datetime
import time


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
    set_collection = set()
    set_collection1 = {'a', 'b'}
    dict_collection = {}
    dict_collection1 = dict()
    list_collection = []
    list_collection1 = list()
    print(type(set_collection))  # <class 'set'>
    print(type(set_collection1))  # <class 'set'>
    print(type(dict_collection))  # <class 'dict'>
    print(type(dict_collection1))  # <class 'dict'>
    print(type(list_collection))  # <class 'list'>
    print(type(list_collection1))  # <class 'list'>


if __name__ == '__main__':
    bytes_convert_str('test')
