# -*-coding:utf-8-*-
import json

""" 
python内置函数
input() 函数接受一个标准输入数据，返回为 string 类型。在对待纯数字输入时具有自己的特性，它返回所输入的数字的类型（ int, float ）。
raw_input() 将所有输入作为字符串看待，返回字符串类型。接收任何类型的输入。
print() 方法用于打印输出，最常见的一个函数。

__import__() 函数用于动态加载类和函数 。如果一个模块经常变化就可以使用 __import__() 来动态载入。
reload() 用于重新载入之前载入的模块。
open() 函数用于打开一个文件，创建一个 file 对象，相关的方法才可以调用它进行读写。
file() 函数用于创建一个 file 对象，它有一个别名叫 open()，更形象一些，它们是内置函数。参数是以字符串的形式传递的。
execfile() 函数可以用来执行一个文件。
staticmethod 返回函数的静态方法。
all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。元素除了是 0、空、None、False 外都算 True。
any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。元素除了是 0、空、FALSE 外都算 TRUE。
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
iter() 函数用来生成迭代器。
next() 返回迭代器的下一个项目。next() 函数要和生成迭代器的iter() 函数一起使用。
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。如果各个迭代器
的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
range() 函数可创建一个整数列表，一般用在 for 循环中。range(start, stop[, step])
xrange() 函数用法与 range 完全相同，所不同的是生成的不是一个数组，而是一个生成器。

oct() 函数将一个整数转换成 8 进制字符串。
int() 函数用于将一个字符串或数字转换为整型。
long() 函数将数字或字符串转换为一个长整型。
float() 函数用于将整数和字符串转换成浮点数。
bool() 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False。bool 是 int 的子类。
complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，
则不需要指定第二个参数。complex([real[, imag]])
hex() 函数用于将10进制整数转换成16进制，以字符串形式表示。
hash() 用于获取取一个对象（字符串或者数值等）的哈希值。
ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符
（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的 Unicode 字符超出了Python 定义范围，
则会引发一个 TypeError 的异常。
bin() 返回一个整数 int 或者长整数 long int 的二进制表示。
chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
bytearray() 方法返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256。
abs() 函数返回数字的绝对值。
divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
round() 方法返回浮点数x的四舍五入值。
pow() 方法返回 x^y（x 的 y 次方） 的值。
min() 方法返回给定参数的最小值，参数可以为序列。
max() 方法返回给定参数的最大值，参数可以为序列。
sum() 方法对系列进行求和计算。
len() 方法返回对象（字符、列表、元组等）长度或项目个数。
sorted() 函数对所有可迭代的对象进行排序操作。
reverse() 函数用于反向列表中元素。
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。该接收两个参数，第一个为函数，
第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。
slice() 函数实现切片对象，主要用在切片操作函数里的参数传递。 slice(start, stop[, step])
basestring() 方法是 str 和 unicode 的超类（父类），也是抽象类，因此不能被调用和实例化，但可以被用来判断一个对象是否为 
str 或者 unicode 的实例，isinstance(obj, basestring) 等价于 isinstance(obj, (str, unicode))。
str() 函数将对象转化为适于人阅读的形式。
str.format() 通过 {} 和 : 来代替以前的 % 格式化字符串，参数个数可以受不限，位置可以不按顺序。
eval() 函数用来执行一个字符串表达式，并返回表达式的值。
isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。isinstance() 会认为子类是一种父类类型，考虑继承关系。
type() 函数如果你只有第一个参数则返回对象的类型，三个参数返回新的类型对象。type() 不会认为子类是一种父类类型，不考虑继承关系。
issubclass() 方法用于判断参数 class 是否是类型参数 classinfo 的子类。

dict() 函数用于创建一个字典。
map() 会根据提供的函数对指定序列做映射。第一个参数 function 以参数序列中的每一个元素调用function函数，返回包含每次function函数返回值的新列表。
set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
list() 方法用于将元组转换为列表。元组与列表区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中。
tuple() 元组 函数将列表转换为元组。
object() Object类是Python中所有类的基类，如果定义一个类时没有指定继承哪个类，则默认继承object类。object没有定义__dict__，
所以不能对object类实例对象尝试设置属性。

super() 函数是用于调用父类(超类)的一个方法。
super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序
（MRO）、重复调用（钻石继承）等种种问题。MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。

callable() 函数用于检查一个对象是否是可调用的。如果返回 True，object 仍然可能调用失败；但如果返回 False，调用
对象 object 绝对不会成功。对于函数、方法、lambda 函式、 类以及实现了 __call__ 方法的类实例, 它都返回 True。
setattr() 函数对应函数 getattr()，用于设置属性值，该属性不一定是存在的。setattr(object, name, value)。
getattr() 函数用于返回一个对象属性值。
hasattr() 函数用于判断对象是否包含对应的属性。
delattr 函数用于删除属性。delattr(x, 'foobar') 相等于 del x.foobar。
property() 函数的作用是在新式类中返回属性值。
vars() 函数返回对象object的属性和属性值的字典对象。

classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
globals() 函数会以字典类型返回当前位置的全部全局变量。
dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。如果参数包含
方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
id() 函数返回对象的唯一标识符，标识符是一个整数。CPython 中 id() 函数用于获取对象的内存地址。
memoryview() 函数返回给定参数的内存查看对象(memory view)。所谓内存查看对象，是指对支持缓冲区协议的数据进行包装，
在不需要复制对象基础上允许Python代码访问。
repr() 函数将对象转化为供解释器读取的形式。
compile() 函数将一个字符串编译为字节代码。

exec 执行储存在字符串或文件中的Python语句，相比于 eval，exec可以执行更复杂的 Python 代码。
help() 函数用于查看函数或模块用途的详细说明。
"""


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


def list_join(a: list = [1, 2, 3], b: list = [3, 4, 5]):
    """ list集合连接操作：
    两个list 的交集：list(set(a).intersection(set(b)))            a&b
    两个list 的并集：list(set(a).union(set(b)))                   a|b
    两个list 的差集：list(set(b).difference(set(a)))              b-a     在b中而不在a中
    两个list对称差集：list(set(b).symmetric_difference(set(a)))    a^b     在a或b中，不同时在a和b中
    """
    # 遍历集合 range
    for index in range(len(b)):
        print(b[index])
    # 遍历集合
    for value in b:
        print(value)
    # 遍历集合
    for index, value in enumerate(b):
        print(index, value)
    # 遍历集合，下标从 2开始
    for index, value in enumerate(b, 2):
        print(index, value)
    print('两个list 的交集：', list(set(a).intersection(set(b))))
    print('两个list 的并集：', list(set(a).union(set(b))))
    print('两个list 的差集：', list(set(b).difference(set(a))))
    print('两个list对称差集：', list(set(b).symmetric_difference(set(a))))


if __name__ == '__main__':
    # bytes_convert_str('test')
    # init_collection()
    # json_example()
    # str_format('Jasom', 18)
    list_join()
