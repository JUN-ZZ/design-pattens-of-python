#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: zhengxianjun
@contact: 1596492090@qq.com
@datetime:2020/6/30 上午9:31
@software: PyCharm 
"""
"""
责任链模式
handler  （出现successor 后继者链）

"""
import abc

class Handler(abc.ABC):

    def __init__(self,successor):
        self.successor = successor #后继者
    @abc.abstractmethod
    def handler(self):
        pass

class ConcreteHandlerA(Handler):

    def __init__(self,successor=None):
        super().__init__(successor)

    def handler(self):
        print('ConcreteHandlerA handler method')
        if self.successor:
            self.successor.handler()

class ConcreteHandlerB(Handler):

    def __init__(self,successor=None):
        super().__init__(successor)

    def handler(self):
        print('ConcreteHandlerB handler method')
        if self.successor:
            self.successor.handler()


class ConcreteHandlerC(Handler):

    def __init__(self, successor=None):
        super().__init__(successor)

    def handler(self):
        print('ConcreteHandlerC handler method')
        if self.successor:
            self.successor.handler()


if __name__ == '__main__':

    h1 = ConcreteHandlerA()
    h2 = ConcreteHandlerB()
    h3 = ConcreteHandlerC()
    h1.handler()
    print('...........')
    h3 = ConcreteHandlerC()
    h2 = ConcreteHandlerB(h3)
    h1 = ConcreteHandlerA(h2)
    h1.handler()

# ConcreteHandlerA handler method
# ...........
# ConcreteHandlerA handler method
# ConcreteHandlerB handler method
# ConcreteHandlerC handler method


