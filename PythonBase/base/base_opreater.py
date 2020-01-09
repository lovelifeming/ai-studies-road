# -*-coding:utf-8-*-
""" 演示Python基础操作
    Numbers（数字） String（字符串）List（列表）Tuple（元组）Dictionary（字典）
    int（有符号整型）long（长整型[也可以代表八进制和十六进制]）float（浮点型）complex（复数）
"""
# 自然语言使用双引号，机器标示使用单引号，因此 代码里 多数应该使用 单引号
# 正则表达式 使用原生的双引号 r"..."
# 文档字符串 (docstring) 使用三个双引号 """......"""
# 在二元运算符两边各空一格 [=,-,+=,==,>,in,is not, and]:
# 反斜杠\换行，二元运算符 '+' ' .'等应出现在行末；长字符串也可以用此法换行
# 禁止复合语句，即一行中包含多个语句

# 模块尽量使用小写命名，首字母保持小写，尽量不要用下划线
# 类名使用驼峰(CamelCase)命名风格，首字母大写，私有类可用一个下划线开头
# 函数名一律小写，如有多个单词，用下划线隔开，私有函数在函数前加一个下划线 _
# 变量名尽量小写, 如有多个单词，用下划线隔开
# 常量采用全大写，如有多个单词，使用下划线隔开
import hashlib
import math
import os
import random
import sys
import uuid


def file_example():
    print('文件编码：' + sys.getdefaultencoding())  # 获取默认编码
    return sys.argv


def number_example():
    # b、d、o、x 分别是二进制、十进制、八进制、十六进制
    int_1 = 126  # 整数 126
    print('整数：' + str(int_1))
    binary_1 = 0b1111110  # 二进制
    print('二进制：' + str(binary_1))
    octal_1 = 0o176  # 八进制
    print('八进制：' + str(octal_1))
    hexadecimal_1 = 0x7e
    print('十六进制：' + str(hexadecimal_1))
    x = 10
    y = 3
    z = 7
    print('x=' + str(x) + ' y=' + str(y) + ' z=' + str(z))
    # x+y,x-y 加 减，'+'号可重载为连接符号
    # x*y,x**y,x/y,x%y,x//y 相乘，求x的y次幂，相除，求余，整除，'*'号可重载为重复，'%'号可重载为格式化
    print('x+y=' + str(x + y) + ' x-y=' + str(x - y) + ' x*y=' + str(x * y) + ' x**y=' + str(x ** y) +
          ' x/y=' + str(x / y) + ' x%y=' + str(x % y) + ' x//y=' + str(x // y))
    # x+y=13 x-y=7 x*y=30 x**y=1000 x/y=3.3333333333333335 x%y=1 x//y=3
    print('abs(-x)=' + str(abs(-x)))  # 求x的绝对值 10
    print('divmod(x,y)=' + str(divmod(x, y)))  # 以二元组的形式返回x除以y所得的商和余数(两个整数) (3,1)
    print('pow(x,y)=' + str(pow(x, y)))  # 计算x的y次幂，与操作符**等同 1000
    print('pow(x,y,z)=' + str(pow(x, y, z)))  # (x**y)%z的另外一种写法 6
    print('round(x/y,2)=' + str(round(x / y, 2)))  # 求浮点数x的四舍五入后得到的相应整数    3.33

    print('整数转八进制：31=' + str(oct(31)))  # 整数转八进制数
    print('整数转十六进制：31=' + str(hex(31)))  # 整数转十六进制数
    print('字符串转整数，第二个参数指示进制：0110=' + str(int('0110')))  # 整数 110
    print('字符串八进制数转整数，第二个参数指示进制：0110=' + str(int('0110', 8)))  # 整数 72
    print('字符串十六进制数转整数，第二个参数指示进制：0x1d=' + str(int('0x1d', 16)))  # 整数29
    print('字符串格式表达式转换八进制、十六进制字符："%o %x %X ="' + str('%o %x %X' % (72, 29, 29)))
    # python里面没有 %O， "%o %x %X ="110 1d 1D

    print('小数转分子分母 float.as_integer_ratio(0.75)：0.75=' + str(float.as_integer_ratio(0.75)))  # 0.75=(3, 4)


def number_example_and_or_not():
    # 位逻辑操作运算符：& | ^ ~，布尔类型有 True/False,逻辑操作符：and，or，not
    x = 9
    y = 5
    z = -2
    print('整数形式：x=' + str(x) + ' y=' + str(y) + ' z=' + str(z))
    print('二进制数：x=' + str(bin(x)) + ' y=' + str(bin(y)) + ' z=' + str(bin(z)))  # x=0b1001 y=0b101 z=-0b10
    print('对整数x与y进行位逻辑 AND运算：x&y=' + str(x & y))  # 1
    print('对整数x与y进行位逻辑 OR 运算，对负数则假定使用2的补：x|y=' + str(x | y))  # 13
    print('对整数x与y进行位逻辑 XOR运算：x^y=' + str(x ^ y))  # 12
    print('将x左移y位，类似 x*(2**y),但不检查溢出：x<<y=' + str(x << y) + ' x*(2**y)=' + str(x * (2 ** y)))  # 288
    print('将x右移y位，类似 x//(2**y),但不检查溢出：x>>3=' + str(x >> 3) + ' x/(2**3)=' + str(x // (2 ** 3)))  # 1
    print('反转x的每一位：~x=' + str(~x))  # -10


def number_example_operational_character():
    # python中1表示真，0表示假，非0都为真
    # 算数运算符：+(加)，-(减)，*(乘)，/(除)，%(取模)，**(幂)，//(取整除)
    # 比较关系运算符：==(等于)，!=(不等于)，>(大于)，<(小于)，>=(大于等于)，<=(小于等于)
    # 赋值运算符：=(赋值)，+=(加等于)，-=(减等于)，*=(乘等于)，/=(除等于)，%=(取模等于)，**=(幂次方等于)，//=(取整等于)
    # 位运算符：&(按位与)，|(按位或)，^(按位异或)，~(按位取反)，<<(左移运算符)，>>(右移运算符)
    # 逻辑运算符：and( x and y 与，如果x为False，返回x的值False，否则返回y的计算值)，
    #           or( x or y 或，如果x为True，返回x的值True，否则返回y的计算值)，
    #           not( not x 非，如果x为True，返回False,否则返回True)
    x = 2
    y = 0
    #  x and y=0; x or y=2; not ( x and y )=True
    print('x and y=' + str(x and y) + '; x or y=' + str(x or y) + '; not ( x and y )=' + str(not (x and y)))
    # 成员运算符：in(如果在指定序列中找到值返回True，否则返回False)，not in(如果在指定序列中没有找到值返回True，否则返回False)
    # 身份运算符：is(is是判断两个标识符是不是引用自一个对象)，is not(is not是判断两个标识符是不是引用自不同对象)


def math_example():
    x = 3.14159265
    y = 2.71828459
    print('x=' + str(x) + ' y=' + str(y))
    print('向下取整数：math.floor(x)=' + str(math.floor(x)))  # 3
    print('向上取整数math.floor(x)=' + str(math.ceil(x)))  # 4


def condition_control_example(score=92):
    # for elif else; while; break continue; pass; else分支
    # 条件分支: if <>: else:    if <>: elif <>: else:
    if (score >= 80):
        print('得分为良：' + str(score))
    elif 60 < score < 80:
        print('得分为中：' + str(score))
    else:
        print('得分为差：' + str(score))
    # for 循环结构 固定次数循环 for 变量 in 集合：
    for i in range(1, 10, 2):
        print('for循环体内部：i=' + str(i))  # 1 3 5 7 9
    # while 循环语句   while 条件表达式：
    index = 1
    while index <= 5:
        i = index
        line = ''
        while i <= 5:
            line += str(index) + '*' + str(i) + '=' + str(index * i) + ' '
            i += 1
        print(line)
        index += 1
    else:
        print('while循环语句结束：index=' + str(index))
    # 条件控制 break 结束当前循环，终止循环， continue 结束当前这一次循环，继续执行循环条件
    # Python中的pass是空语句，为保证程序结构的完整性。pass不做任何事情，一般用作占位语句。
    # Python中为循环结构引入了 else 子句，在循环结束时做特定处理。如果while/for条件正常退出循环，那么else分支将被执行。
    #       如果以非正常方式(break/continue)退出循环，else分支不被执行。


def get_uuid(param='test'):
    """ uuid是128位的全局唯一标识符（univeral unique identifier），通常用32位的一个字符串的形式来表现。
    有时也称guid(global unique identifier)。python中自带了uuid模块来进行uuid的生成和管理工作。
    python中的uuid模块基于信息如MAC地址、时间戳、命名空间、随机数、伪随机数来uuid。具体方法有如下几个：　　
　　uuid.uuid1()　　基于MAC地址，时间戳，随机数来生成唯一的uuid，可以保证全球范围内的唯一性。
　　*uuid.uuid2()　　算法与uuid1相同，不同的是把时间戳的前4位置换为POSIX的UID。
    *不过需要注意的是python中没有基于DCE的算法，所以python的uuid模块中没有uuid2这个方法。
　　uuid.uuid3(namespace,name)　　通过计算一个命名空间和名字的md5散列值来给出一个uuid，所以可以保证命名空间中的不同
    名字具有不同的uuid，但是相同的名字就是相同的uuid了。namespace并不是一个自己手动指定的字符串或其他量，
    而是在uuid模块中本身给出的一些值。比如uuid.NAMESPACE_DNS，uuid.NAMESPACE_OID，uuid.NAMESPACE_OID这些值。
    这些值本身也是UUID对象，根据一定的规则计算得出。
　　uuid.uuid4()　　通过伪随机数得到uuid，是有一定概率重复的
　　uuid.uuid5(namespace,name)　　和uuid3基本相同，只不过采用的散列算法是sha1 """
    namespace = uuid.NAMESPACE_URL
    name = param
    id1 = uuid.uuid1()
    print("uuid1:" + id1.hex)
    id3 = uuid.uuid3(namespace, name)
    print("uuid3:" + id3.__str__())
    id4 = uuid.uuid4()
    print("uuid4:int=" + str(id4.int))
    id5 = uuid.uuid5(namespace, name)
    print("uuid5:time=" + str(id5.time))
    return id1


def get_str_md5(str):
    """ 计算字符串md5值 """
    md5 = hashlib.md5(str.encode('utf-8'))
    md5_digest = md5.hexdigest()
    return md5_digest


def get_file_md5(file_name):
    """ 计算文件md5值 """
    with open(file_name, 'rb') as fn:
        data = fn.read()
        md5 = hashlib.md5(data).hexdigest()
        return md5


def get_big_file_md5(file_name):
    """ 计算大文件的md5值 """
    m = hashlib.md5()
    with open(file_name, 'rb') as fn:
        while True:
            data = fn.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()


def get_md5_of_folder(dir):
    """ 计算文件夹下面所有文件md5值 """
    if not os.path.isdir(dir):
        return None
    md5_file = "{}_tmp.md5".format(str(random.randint(0, 1000)).zfill(6))
    with open(md5_file, 'w') as outfile:
        for root, subdirs, files in os.walk(dir):
            for file in files:
                file_full_path = os.path.join(root, file)
                md5 = get_file_md5(file_full_path)
                outfile.write(md5)
    md5 = get_file_md5(md5_file)
    os.remove(md5_file)
    return md5


if __name__ == '__main__':
    # get_uuid('admin')
    # 不带括号时，调用的是这个函数本身，是整个函数体，获取函数内存地址，不须等函数执行完成。
    print("不带括号：" + file_example.__str__())
    # 带括号时，调用的是函数执行的结果，须等函数执行完成的结果。函数默认返回 None
    print("带括号：" + str(file_example()))
    # 获取字符串、文件、大文件、文件夹 md5值
    print(get_str_md5('abc'))
    print(get_file_md5('D:\\test\\test.txt'))
    print(get_big_file_md5('D:\\test\\test.txt'))
    print(get_md5_of_folder('D:\\test'))

    # file_example()    #文件操作编码
    # number_example()  # 数字操作
    # number_example_and_or_not()  # 逻辑操作
    # number_example_operational_character()  操作符
    # math_example()        # math 库操作
    # condition_control_example(68)  # 条件分支，循环结构，
    # str_example('test')  # 字符串操作
