# -*-coding:utf-8-*-
from copy import deepcopy

""" from 是从文件里面导入模块或包，import 是导入对象"""
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
        单星号（*）：*agrs，将所有参数以元组(tuple)的形式导入
        双星号（**）：**kwargs,双星号（**）将参数以字典的形式导入:
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
