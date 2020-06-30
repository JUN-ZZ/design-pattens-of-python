#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: zhengxianjun
@contact: 1596492090@qq.com
@datetime:2020/6/24 下午5:07
@software: PyCharm 
"""
import abc


class Product(abc.ABC):
    """
    抽象类
    """

    @abc.abstractmethod
    def service(self):
        """
        提供的调用方法
        :return:
        """
        pass


class ConcreteProductA(Product):

    def service(self):
        print('concreteProductA method.')


class ConcreteProductB(Product):

    def service(self):
        print('ConcreteProductB method.')


class ConcreteProductC(Product):

    def service(self):
        print('ConcreteProductC method.')

# 2.工厂方法
# 1。抽象类 Product
# 2。抽象工厂类 Factory
# 通过具体的工厂创建具体的类
# 有多少个具体类就创建多少个工厂类，把创建的放在具体的


class Factory(abc.ABC):
    """
    抽象工厂类
    """
    @abc.abstractmethod
    def create_instance(self):
        """
        创建实例
        :return:
        """
        pass


class ConcreteProductAFactory(Factory):

    def create_instance(self):
        return ConcreteProductA()


class ConcreteProductBFactory(Factory):

    def create_instance(self):
        return ConcreteProductB()


class ConcreteProductCFactory(Factory):

    def create_instance(self):
        return ConcreteProductC()


if __name__ == '__main__':

    f1 = ConcreteProductAFactory()
    p1 = f1.create_instance()
    p1.service()

    f2 = ConcreteProductBFactory()
    p2 = f2.create_instance()
    p2.service()

    f3 = ConcreteProductCFactory()
    p3 = f3.create_instance()
    p3.service()

# concreteProductA method.
# ConcreteProductB method.
# ConcreteProductC method.


