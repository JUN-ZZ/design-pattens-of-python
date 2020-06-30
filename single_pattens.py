#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: zhengxianjun
@contact: 1596492090@qq.com
@datetime:2020/6/28 上午11:04
@software: PyCharm 
"""
# 单例模式

import threading


class Product():
    __instance_lock = threading.Lock() #加锁

    def __new__(cls, *args, **kwargs):
        with cls.__instance_lock as lock: #加锁
            if not hasattr(cls,'__single_instance__'):
                cls.__single_instance__ = super(Product, cls).__new__(cls)
        return cls.__single_instance__

    def service(self):
        print('Product method.,id:',id(self))


# if __name__ == '__main__':
#     p = Product()
#     p.service()
#
#     p1 = Product()
#     p1.service()

# Product method.,id: 139829767793360
# Product method.,id: 139829767793360

# python 装饰器 单例 不用加锁
# 创建类的时候 使用装饰器创建类对象
def singleton(cls):
    _instance = {}

    def _singleton(*args,**kargs):

        if _instance.get(cls):
            return _instance[cls]
        else:
            _instance[cls] = cls(*args,**kargs)
            return _instance[cls]

    return _singleton


@singleton
class ProductA():
    def service(self):
        print('Product method.,id:',id(self))


if __name__ == '__main__':
    p = ProductA()
    p.service()

    p1 = ProductA()
    p1.service()

# Product method.,id: 140559178208080
# Product method.,id: 140559178208080

