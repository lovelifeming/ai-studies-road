# -*-coding:utf-8-*-
import json


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


def json_example():
    user = {"name": "zsm", "age": "20", "address": "China", "export": "The CHINA"}
    arr = ['a', 'b', 'c', 'd']
    user_str = json.dumps(user)
    arr_str = json.dumps(arr)
    print("user转换为json：" + user_str)
    print(type(user_str))
    print("array转换为json：" + arr_str)
    print(type(arr_str))
    user1 = json.loads(user_str)
    arr1 = json.loads(arr_str)
    print("json反转：" + str(user1))
    print(type(user1))
    print("json反转：" + str(arr1))
    print(type(arr1))


def str_format(name, age):
    """str.format（），替换字段用大括号标记，可以用索引来以任何顺序引用变量,
    如果插入变量名称，则会获得额外的能够传递对象的权限，然后在大括号之间引用参数和方法，也可以使用**来用字典来完成。
    f'{}' F'{}' 是字符串格式的一种简写"""
    print("Hello, {}. You are {}.".format(name, age))
    print("Hello, {1}. You are {0}-{0}.".format(age, name))
    person = {'name': name, 'age': age + 1}
    print("Hello, {name}. You are {age}.".format(name=person['name'], age=person['age']))
    print("Hello, {name}. You are {age}.".format(**person))
    print(f"Hello, {name}. You are {age}.")
    print(F"Hello, {name}. You are {age}.")


if __name__ == '__main__':
    # bytes_convert_str('test')
    # init_collection()
    # json_example()
    str_format('Jasom', 18)
