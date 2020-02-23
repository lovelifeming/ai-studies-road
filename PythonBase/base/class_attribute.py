# -*-coding:utf-8-*-
from copy import deepcopy


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
	"""
	name = None
	age = None
	gender = None

	def __init__(self, *arg):
		self.name = arg[0]
		self.age = arg[1]
		self.gender = arg[2]

	def set_name(self, name):
		self.name = name

	def set_attribute(self, **kwargs):
		self.name = kwargs.pop('name', 'sam')
		self.age = kwargs.pop('age', 0)
		self.gender = kwargs.pop('gender', 1)
		self.birthday = kwargs.pop('birthday', None)


if __name__ == '__main__':
	people = People('test', 18, 'male')
	p = deepcopy(people)
	print(people.__dict__)
	people.set_attribute(name='jenny', age=20, gender='female')
	print(people.__dict__)
	print("People 继承自 Human：" + issubclass(People, Human).__str__())
	print("深拷贝对象 p：" + p.__dict__.__str__())
