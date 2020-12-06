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
import platform
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
    # 逻辑运算符：and、or都是惰性求值，and 第一个是false就不会运行第二个表达式，or 第一个是true就不会运行第二个表达式。
    #           and( x and y 与，如果x为False，返回x的值False，否则返回y的计算值)，
    #           or( x or y 或，如果x为True，返回x的值True，否则返回y的计算值)，
    #           not( not x 非，如果x为True，返回False,否则返回True)
    # 成员运算符：in(如果在指定序列中找到值返回True，否则返回False)，not in(如果在指定序列中没有找到值返回True，否则返回False)
    # 身份运算符：is(is是判断两个标识符是不是引用自一个对象)，is not(is not是判断两个标识符是不是引用自不同对象)
    x = 2
    y = 0
    #  x and y=0; x or y=2; not ( x and y )=True
    print('x and y=' + str(x and y) + '; x or y=' + str(x or y) + '; not ( x and y )=' + str(not (x and y)))


def print_example():
    """ 打印输出示例 """
    print('this is an integer %4d' % 2)
    print('this is a float %f' % 2.71828)
    print('this is a float %.4d' % 2.71828459)
    print('this is an integer {:04d}'.format(2))
    print('this is a float {:8f}'.format(2.71828459))
    i = 0
    while i < 3:
        print(i, end=',')
        i += 1


def str_example(val: str = 'A good beginning is half done '):
    """
    方法	描述
    string.capitalize()	把字符串的第一个字符大写
    string.center(width)	返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
    string.count(str, beg=0, end=len(string))	返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
    string.decode(encoding='UTF-8', errors='strict')	以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除非 errors 指 定 的 是 'ignore' 或 者'replace'
    string.encode(encoding='UTF-8', errors='strict')	以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
    string.endswith(obj, beg=0, end=len(string))	检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
    string.expandtabs(tabsize=8)	把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8。
    string.find(str, beg=0, end=len(string))	检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
    string.format()	格式化字符串
    string.index(str, beg=0, end=len(string))	跟find()方法一样，只不过如果str不在 string中会报一个异常.
    string.isalnum()	如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
    string.isalpha()	如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
    string.isdecimal()	如果 string 只包含十进制数字则返回 True 否则返回 False.
    string.isdigit()	如果 string 只包含数字则返回 True 否则返回 False.
    string.islower()	如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
    string.isnumeric()	如果 string 中只包含数字字符，则返回 True，否则返回 False
    string.isspace()	如果 string 中只包含空格，则返回 True，否则返回 False.
    string.istitle()	如果 string 是标题化的(见 title())则返回 True，否则返回 False
    string.isupper()	如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
    string.join(seq)	以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
    string.ljust(width)	返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
    string.lower()	转换 string 中所有大写字符为小写.
    string.lstrip()	截掉 string 左边的空格
    string.maketrans(intab, outtab])	maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
    max(str)	返回字符串 str 中最大的字母。
    min(str)	返回字符串 str 中最小的字母。
    string.partition(str)	有点像 find()和 split()的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string.
    string.replace(str1, str2,  num=string.count(str1))	把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.
    string.rfind(str, beg=0,end=len(string) )	类似于 find()函数，不过是从右边开始查找.
    string.rindex( str, beg=0,end=len(string))	类似于 index()，不过是从右边开始.
    string.rjust(width)	返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
    string.rpartition(str)	类似于 partition()函数,不过是从右边开始查找
    string.rstrip()	删除 string 字符串末尾的空格.
    string.split(str="", num=string.count(str))	以 str 为分隔符切片 string，如果 num 有指定值，则仅分隔 num+ 个子字符串
    string.splitlines([keepends])	按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
    string.startswith(obj, beg=0,end=len(string))	检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.
    string.strip([obj])	在 string 上执行 lstrip()和 rstrip()
    string.swapcase()	翻转 string 中的大小写
    string.title()	返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
    string.translate(str, del="")	根据 str 给出的表(包含 256 个字符)转换 string 的字符,要过滤掉的字符放到 del 参数中
    string.upper()	转换 string 中的小写字母为大写
    string.zfill(width)	返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0
    """
    ans = val.isspace() if val else 'In order to be irreplaceable one must always be different '
    print(ans.lower())  # 字符转小写
    print(ans.upper())  # 字符转大写
    print(ans.startswith('start'))  # 判断以指定字符开头
    print(ans.endswith('end'))  # 判断以指定字符结尾
    print(ans.title())  # 返回字符串中所有单词首字母大写且其他字母小写的格式
    print(ans.capitalize())  # 返回首字母大写、其他字母全部小写的新字符串
    print(ans.swapcase())  # 做大小写转换(大写-->小写，小写-->大写)
    print(ans.isdecimal())  # 判断是否是数字
    print(ans.isdigit())  # 判断是否是数字
    print(ans.isnumeric())  # 判断是否是数字
    print(ans.isalpha())  # 判断是否是字母
    print(ans.isalnum())  # 判断是否是数字或字母
    print(ans.islower())  # 判断是否是小写
    print(ans.isupper())  # 判断是否是大写
    print(ans.istitle())  # 判断是否是首字母大写
    print(ans.isspace())  # 判断是否是空白(空格、制表符、换行符等)字符
    print(ans.isprintable())  # 判断是否是可打印字符(例如制表符、换行符就不是可打印字符，但空格是)
    print(ans.sidentifier())  # 判断是否满足标识符定义规则
    # str.center(width[, fillchar])  将字符串居中，左右两边使用fillchar进行填充，使得整个字符串的长度为width。
    # fillchar默认为空格。如果width小于字符串的长度，则无法填充直接返回字符串本身(不会创建新字符串对象)。
    print(ans.center(20, '*'))
    print(ans.count('a'))  # 统计子串出现的次数
    print(ans.find('a', 1, 10))  # 搜索子串，如果包含，则返回sub的索引位置，否则返回"-1"。
    print(ans.rfind('a', 1, 10))  # 搜索最右边子串的位置，如果包含，则返回sub的索引位置，否则返回"-1"。
    print(ans.index('a', 1, 10))  # 搜索子串，如果包含，则返回sub的索引位置，否则抛出ValueError错误。
    print(ans.rindex('a', 1, 10))  # 搜索子串，如果包含，则返回sub的索引位置，否则抛出ValueError错误。
    print(ans.replace('old', 'new'))  # 将字符串中的子串o替换为新字符串，如果给定count，则表示只替换前count个子串。
    print(ans.expandtabs(2))  # 将字符串中的\t替换为一定数量的空格。默认N=8。
    tb = ans.maketrans('abco', '12*0')  # 生成一个字符一 一映射的table
    print(tb)
    print(ans.translate(tb))  # 对字符串中的每个字符进行映射
    # 搜索字符串中的子串，并从子串处进行分割，最后返回一个包含3元素的元组：子串左边的部分是元组的第一个元素，
    # 子串自身是元组的二个元素，子串右边是元组的第三个元素。
    print(ans.partition('is'))
    print(ans.rpartition('is'))  # 从右边开始分割。类似 partition
    # split()根据sep对S进行分割，maxsplit用于指定分割次数，如果不指定maxsplit或者给定值为"-1"，则会从做向右搜索并且
    # 每遇到sep一次就分割直到搜索完字符串。如果不指定sep或者指定为None，则改变分割算法：以空格为分隔符，
    # 且将连续的空白压缩为一个空格。rsplit()和split()是一样的，只不过是从右边向左边搜索。
    print(ans.split(' ', 2))
    print(ans.rsplit(' ', 2))
    # splitlines()用来专门用来分割换行符，常见的是\n、\r、\r\n。虽然它有点像split('\n')或split('\r\n'),但它们有些区别。
    print(ans.splitlines(keepends=True))  # 如果指定keepends为True，则保留所有的换行符
    # str.join(iterable)将可迭代对象(iterable)中的字符串使用str连接起来。注意，iterable中必须全部是字符串类型，否则报错。
    # iterable对象可以是：字符串string、列表list、元组tuple、字典dict(键值拼接)、集合set。
    print('_'.join({'name': 'Jasom', 'age': '18'}))
    # ljust 获取固定长度，左对齐，右边用*或空格补齐：str.ljust(width,"*")(width)
    print(ans.ljust(50, ''))
    # rjust 获取固定长度，右对齐，左边用*或空格补齐：str.rjust(width,"*")(width)
    print(ans.rjust(50, 'abc'))
    # str.strip([chars])    str.lstrip([chars])     str.rstrip([chars])
    # 分别是移除左右两边、左边、右边的字符char。如果不指定chars或者指定为None，则默认移除两边空白(空格、制表符、换行符)。
    print(ans.strip())
    print(ans.lstrip(' '))
    print(ans.rstrip('abc'))
    print(dir(str))  # dir()查看类的方法和属性，特殊字符串变量__name__指向模块的名字，__file__指向该模块的导入文件名。
    print(help(str))  # help()查看函数或模块用途的详细说明
    print(help(str.format))  # help(object.method_name) 查看具体类中某方法的详细说明


def math_example():
    x = 3.14159265
    y = 2.71828459
    print('x=' + str(x) + ' y=' + str(y))
    print('向下取整数：math.floor(x)=' + str(math.floor(x)))  # 3
    print('向上取整数math.floor(x)=' + str(math.ceil(x)))  # 4


def condition_control_example(score=92):
    """ for elif else; while; break continue; pass; else分支
        条件分支: if <>: else:    if <>: elif <>: else:
        条件控制 break 结束当前循环，终止循环， continue 结束当前这一次循环，继续执行循环条件
        Python中的pass是空语句，为保证程序结构的完整性。pass不做任何事情，一般用作占位语句。
        Python中为循环结构引入了 else 子句，在循环结束时做特定处理。如果while/for条件正常退出循环，那么else分支将被执行。
        如果以非正常方式(break/continue)退出循环，else分支不被执行。 """
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
    # print(get_file_md5('D:\\test\\test.txt'))
    # print(get_big_file_md5('D:\\test\\test.txt'))
    # print(get_md5_of_folder('D:\\test'))
    print_example()
    # file_example()    #文件操作编码
    # number_example()  # 数字操作
    # number_example_and_or_not()  # 逻辑操作
    # number_example_operational_character()  操作符
    # math_example()        # math 库操作
    # condition_control_example(68)  # 条件分支，循环结构，
    str_example('test')  # 字符串操作
    print('python 解释器版本：', platform.python_version())
    print('python 解释器版本：', sys.version)
    print('*********** run end ***********')
