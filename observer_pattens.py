#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: zhengxianjun
@contact: 1596492090@qq.com
@datetime:2020/6/29 下午4:46
@software: PyCharm 
"""

"""
观察者模式
简单来说就是发布与订阅
观察者和被观察者
"""

import abc

class Subject(abc.ABC):
    """
    主题 被观察者
    """

    def __init__(self):
        # 观察者列表
        self.observer_list = []

    @abc.abstractmethod
    def register_observer(self,observer):
        """
        注册观察者
        :return:
        """
        pass

    @abc.abstractmethod
    def remove_observer(self,observer):
        """
        remove observer
        :return:
        """
        pass

    @abc.abstractmethod
    def notify_observer(self):
        """
        通知观察者
        :return:
        """
        pass


class Observer(abc.ABC):

    @abc.abstractmethod
    def update(self,config):
        """
        被通知执行的方法
        :return:
        """


class ConfigSubject(Subject):

    def __init__(self):
        super().__init__()

    def set_config(self,config):
        self.config = config

    def register_observer(self,observer):
        self.observer_list.append(observer)

    def remove_observer(self,observer):
        self.observer_list.remove(observer)

    def notify_observer(self):
        for o in self.observer_list:
            o.update(self.config)


class AppA(Observer):

    def update(self, config):
        print('AppA.config.',config)


class AppB(Observer):

    def update(self, config):
        print('AppB.config.', config)


class AppC(Observer):

    def update(self, config):
        print('AppC.config.', config)


if __name__ == '__main__':

    a = AppA()
    b = AppB()
    c = AppC()

    s = ConfigSubject()
    s.register_observer(a)
    s.register_observer(b)
    s.register_observer(c)
    # 模拟修改配置文件 通知各个应用
    s.set_config('/home/dev')
    s.notify_observer()
# AppA.config. /home/dev
# AppB.config. /home/dev
# AppC.config. /home/dev
    s.set_config('/home/jun')
    s.notify_observer()
# AppA.config. /home/jun
# AppB.config. /home/jun
# AppC.config. /home/jun
    s.remove_observer(b)
    s.notify_observer()
# AppA.config. /home/jun
# AppC.config. /home/jun


