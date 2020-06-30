#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: zhengxianjun
@contact: 1596492090@qq.com
@datetime:2020/6/24 下午4:43
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

    @staticmethod
    def new_instance(type=None):
        """
        静态创建 工厂方法
        :param type:
        :return:
        """
        p = None
        if type == 'A':
            p = ConcreteProductA()
        elif type == 'B':
            p = ConcreteProductB()
        elif type == 'C':
            p = ConcreteProductC()

        return p


class ConcreteProductA(Product):

    def service(self):
        print('concreteProductA method.')


class ConcreteProductB(Product):

    def service(self):
        print('ConcreteProductB method.')


class ConcreteProductC(Product):

    def service(self):
        print('ConcreteProductC method.')


# 创建型
# 1。简单工厂模式
# 把 所有的具体类 统一交给 工厂类类创建 使用静态方法

if __name__ == '__main__':

    p = Product.new_instance('A')
    p.service()

    p2 = Product.new_instance('B')
    p2.service()

# concreteProductA method.
# ConcreteProductB method.
















