#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: zhengxianjun
@contact: 1596492090@qq.com
@datetime:2020/6/24 下午5:22
@software: PyCharm 
"""

# 抽象工厂模式与工厂方法模式最大的区别在于，工厂方法模式针对的是一个产品等级结构，
# 而抽象工厂模式则需要面对多个产品等级结构，
# 一个工厂等级结构可以负责多个不同产品等级结构中的产品对象的创建 。
# 当一个工厂等级结构可以创建出分属于不同产品等级结构的一个产品族中的所有对象时，
# 抽象工厂模式比工厂方法模式更为简单、有效率。

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


class ConcreteProductA1(Product):

    def service(self):
        print('ConcreteProductA1 method.')


class ConcreteProductA2(Product):

    def service(self):
        print('ConcreteProductA2 method.')


class ConcreteProductB(Product):

    def service(self):
        print('ConcreteProductB method.')


class Factory(abc.ABC):
    """
    抽象工厂类
    """
    @abc.abstractmethod
    def create_a1_instance(self):
        """
        创建实例A
        :return:
        """
        pass

    @abc.abstractmethod
    def create_a2_instance(self):
        """
        创建实例A
        :return:
        """
        pass

    @abc.abstractmethod
    def create_b_instance(self):
        """
        创建实例A
        :return:
        """
        pass


class ConcreteFactory(Factory):

    def create_a1_instance(self):
        return ConcreteProductA1()

    def create_a2_instance(self):
        return ConcreteProductA2()

    def create_b_instance(self):
        return ConcreteProductB()


if __name__ == '__main__':
    f = ConcreteFactory()

    pa1 = f.create_a1_instance()
    pa1.service()

    pa2 = f.create_a2_instance()
    pa2.service()

    p = f.create_b_instance()
    p.service()

# ConcreteProductA1 method.
# ConcreteProductA2 method.
# ConcreteProductB method.



