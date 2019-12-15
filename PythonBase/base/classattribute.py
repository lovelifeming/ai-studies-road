# -*-coding:utf-8-*-


class People(object):
    """  造函数，不明确定义参数个数
        单星号（*）：*agrs，将所有参数以元组(tuple)的形式导入
        双星号（**）：**kwargs,双星号（**）将参数以字典的形式导入:
    """
    age = None
    name = None
    male = None

    def __init__(self, *arg):
        self.age = arg

    def setattribute(self, **kwargs):
        age = kwargs.pop('age', 0)
        name = kwargs.pop('name', 'sam')
        male = kwargs.pop('male', 1)


if __name__ == '__main__':
    People()
