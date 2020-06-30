#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: zhengxianjun
@contact: 1596492090@qq.com
@datetime:2020/6/24 下午5:29
@software: PyCharm 
"""

"""
建造者模式
将复杂的对象的构建过成和表示分离 用同一个建造流程 可以有不同的表示
将建造分给指挥者来建造
"""

import abc

class Builder(abc.ABC):
    @abc.abstractmethod
    def build_part_a(self):
        pass

    @abc.abstractmethod
    def build_part_b(self):
        pass

class Product():

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def service(self):
        self.a.service()
        self.b.service()

class ConcreteProductPartA():
    def service(self):
        print('ConcreteProductPartA method.')

class ConcreteProductPartB():
    def service(self):
        print('ConcreteProductPartB method.')


class ConcreteBuilderA(Builder):
    """
    产品A的建造者
    """

    def build_part_a(self):
        return ConcreteProductPartA()

    def build_part_b(self):
        return ConcreteProductPartB()


class Director:

    def set_builder(self, builder):
        self.builder = builder

    def construct(self):
        # 建造顺序
        a = self.builder.build_part_a()
        b = self.builder.build_part_b()
        return Product(a,b)

if __name__ == '__main__':
    b = ConcreteBuilderA() #具体的建造者
    d = Director() #指挥者
    d.set_builder(b)
    p = d.construct() # 建造
    p.service() #完整的产品

# ConcreteProductPartA method.
# ConcreteProductPartB method.















