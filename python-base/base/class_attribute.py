# -*-coding:utf-8-*-
from copy import deepcopy

""" 
当使用 import 语句导入模块后，Python 会按照以下顺序查找指定的模块文件：
    在当前目录，即当前执行的程序文件所在目录下查找；
    到 PYTHONPATH（环境变量）下的每个目录中查找；
    到 Python 默认的安装目录下查找。
解决 'ModuleNotFoundError' 的方法有 3 种，分别是：
    1.向 sys.path 中临时添加模块文件存储位置的完整路径；
    2.将模块放在 sys.path 变量中已包含的模块加载路径中；
    3.设置 path 系统环境变量。
    
from 是从文件里面导入模块或包，import 是导入对象
 import class,class1,class2
 import class as cla
 import class.function as fun
 form module import class[,class1][,class2]
 form module import *
 
相对导入：在顶层的 __init__.py 文件中导入
 from . import class                #导入同级对象
 from .submodule import class       #导入同级目录里对象
 from ..submodule import class      #导入上级目录对象
 from ...submodule import class     #导入上上级目录对象
 
可选导入（Optional imports）
    代码为例：
    try:
        # For Python 3
        from http.client import responses
    except ImportError:  # For Python 2.5-2.7
        try:
            from httplib import responses  # NOQA
        except ImportError:  # For Python 2.4
            from BaseHTTPServer import BaseHTTPRequestHandler as _BHRH
            responses = dict([(k, v[0]) for k, v in _BHRH.responses.items()])
循环导入:如果创建两个模块，二者相互导入对方，那么就会出现循环导入。建议重构代码结构。
覆盖导入：当创建的模块与标准库中的模块同名时，如果你导入这个模块，就会出现覆盖导入。建议命名时避免与标准库名相同。

"""


class Human(object):
    """ Python 原生仅支持抽象类。抽象类：包含抽象函数，可以有函数实现和属性。抽象类只能被继承，不能被实例化 """
    birthday = None

    def set_name(self, name):
        NotImplementedError

    def set_birthday(self, date):
        self.birthday = date

    def death_date(self, date):
        pass


class People(Human):
    """  造函数，不明确定义参数个数
        单星号（*）：*agrs，将所有参数以元组(tuple)的形式导入，是Arguments简写
        双星号（**）：**kwargs,双星号（**）将参数以字典的形式导入，是 keyWordArguments简写
        self 是类内部成员变量，作用范围是类内部
        Python 不支持重载，只有重写。方法名相同时：后面的方法名会覆盖前面相同的方法名。
    """
    name = None
    age = None
    gender = None

    # 默认的构造函数
    def __init__(self, *arg):
        Human.__init__(self)  # 调用父类构造函数
        # super(People,self).__init__()     # 多继承时调用所有父类构造函数
        self.name = arg[0]
        self.age = arg[1]
        self.gender = arg[2]

    def set_name(self, name):
        self.name = name

    def set_attribute(self, **kwargs):
        # 成员方法
        self.name = kwargs.pop('name', 'sam')
        self.age = kwargs.pop('age', 0)
        self.gender = kwargs.pop('gender', 1)
        self.birthday = kwargs.pop('birthday', '1990-01-01')

    def venture_company(self, **kwargs):
        try:
            company_name = kwargs.pop('companyName')
            legal_person = kwargs.pop('legalPerson')
            company_name = kwargs.pop('ventureCapital')
        except Exception as e:
            raise Exception('venture capital fail ' + str(e))
        finally:
            print('this company output:', kwargs.items())

    @classmethod
    def have_lunch(self, sth):
        # 类方法，必须传 self
        print(str(sth) + " for lunch today")

    @staticmethod
    def go_to_sleep(name):
        print(str(name) + ",you should go to bed!")

    def __str__(self):
        print("This is the custom method!")
        return "name={},age={},gender={},birthday={}".format(self.name, self.age, self.gender, self.birthday)

    # 析构函数
    # def __del__(self):
    #     print("del Human...")


if __name__ == '__main__':
    people = People('test', 18, 'male')
    people.have_lunch('steak')
    People.go_to_sleep('Jason')
    p = deepcopy(people)
    print('people.__dict__:' + str(people.__dict__))
    people.set_attribute(name='jenny', age=20, gender='female')
    print('people.__dict__:' + str(people.__dict__))
    print("People 继承自 Human：" + issubclass(People, Human).__str__())
    print("深拷贝对象 p：" + p.__dict__.__str__())
    print('people.__str__():' + people.__str__())
