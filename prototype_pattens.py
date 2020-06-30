#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: zhengxianjun
@contact: 1596492090@qq.com
@datetime:2020/6/28 上午11:04
@software: PyCharm 
"""

# 原型模式
# 利用原原对象创建新的对象

# import pandas as pd
#
#
# df = pd.DataFrame([(1,'hh'),(2,'8'),(1,'h'),(2,'h'),(1,'h'),(2,'h')],columns=['id','gene'])
# # df = pd.DataFrame([[1,'h']],columns=['id','gene'])
#
# print(df)
#
# dfg = df.groupby(['id', 'gene']).size().reset_index(name='counts')
# print(dfg)
# dfg.sort_values(by=['counts'],ascending=False,inplace=True)
# print(dfg)
# print(type(dfg))
# list0 = dfg['gene'].tolist()[:2]
# list1 = dfg['counts'].tolist()[:2]
#
# t = zip(list0,dfg['counts'].tolist()[:2])
# print([(d[0],d[1]) for d in t])
# # d = dict(t)
# # print(d)
# # print(dfg['gene'])
#
# #
# # df.drop_duplicates(inplace=True)
# # print(df)
# # d = df.loc[:,['id','gene']]
# # print(d)
# # # df.c

import abc
"""
原型模式 通过已经存在的类创建新的类对象 属性相同
"""

class Clone(abc.ABC):
    """
    原型克隆
    """
    @abc.abstractmethod
    def clone(self):
        pass


class ProductA(Clone):

    def __init__(self,a):
        self.a = a

    def clone(self):
        return ProductA(a=self.a)

    def __repr__(self):
        return str(self.a)


class ProductB(Clone):

    def __init__(self, a):
        self.a = a

    def clone(self):
        return ProductB(a=self.a)

    def __repr__(self):
        return str(self.a)


if __name__ == '__main__':
    a = ProductA(a=88)
    print(a)
    print(id(a))
    new_a = a.clone()
    print(new_a)
    print(id(new_a))

    b = ProductB(a=88)
    print(b)
    new_b = b.clone()
    print(new_b)

# 88
# 140518614617104
# 88
# 140518614617168
# 88
# 88

