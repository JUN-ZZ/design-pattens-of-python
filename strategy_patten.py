#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: zhengxianjun
@contact: 1596492090@qq.com
@datetime:2020/8/17 下午3:03
@software: PyCharm 
"""

# 策略模式
# 定义一系列算法，封装每个算法，并使它们可以互换。
# 策略模式可以让算法独立于使用它的客户端。
#状态模式 是通过状态的改变，来进行状态改变，产生对应的动作

import abc


class Strategy(abc.ABC):

    @abc.abstractmethod
    def algorithm(self):
        pass


class Context:
    """
    上下文
    """
    def __init__(self,strategy):
        self.strategy = strategy

    def algorithm(self):
        self.strategy.algorithm()


class ConcreteStrategyA(Strategy):

    def algorithm(self):
        print('hhhhhhhhhhh')


class ConcreteStrategyB(Strategy):

    def algorithm(self):
        print('aiaiiaaiaiiai')


if __name__ == '__main__':

    strategyA = ConcreteStrategyA()
    strategyB = ConcreteStrategyB()
    cxt = Context(strategyA)
    cxt.algorithm()
    # 选取不同的策略，使用不同的算法
    cxt1 = Context(strategyB)
    cxt1.algorithm()






