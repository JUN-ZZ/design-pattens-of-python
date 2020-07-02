#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: zhengxianjun
@contact: 1596492090@qq.com
@datetime:2020/7/2 下午2:51
@software: PyCharm 
"""

import pymssql
import pymysql
import abc


class Connect(abc.ABC):
    """
    连接工具类,连接数据库
    抽象类
    """
    def __init__(self, host=None, user=None, pwd=None, db=None, as_dict=False):
        """
           类的构造函数，初始化数据库连接ip或者域名，以及用户名，密码，要连接的数据库名称
           host=None,
           user=None
           pwd=None,
           db=None,
           as_dict=False 返回结果是否用字典的形式 默认是元组

           """
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.as_dict = as_dict

    @abc.abstractmethod
    def _get_connect(self):
        """
        得到数据库连接信息函数， 返回: conn.cursor()
        """
        pass

    @abc.abstractmethod
    def exec_query(self, sql):
        """
        执行查询语句,
        返回的是一个包含tuple的list，
        list的元素是记录行，tuple的元素是每行记录的字段
        """
        pass

    @abc.abstractmethod
    def exec_non_query(self, sql):
        """
        执行查询语句,
        无返回
        """
        pass

    @abc.abstractmethod
    def exec_query_params(self, sql, params):
        """
        带参数的，查询语句
        """
        pass

    @abc.abstractmethod
    def close_connect(self):
        """
           关闭连接
       """
        pass


class MSConnect(Connect):
    """
    连接工具类,连接数据库
    其他数据库换驱动
    """
    def __init__(self, host=None, user=None, pwd=None, db=None,as_dict=False):
        """
        类的构造函数，初始化数据库连接ip或者域名，以及用户名，密码，要连接的数据库名称
        host=None,
        user=None
        pwd=None,
        db=None,
        as_dict=False 返回结果是否用字典的形式 默认是元组

        """
        super().__init__(host=host, user=user, pwd=pwd, db=db,as_dict=as_dict)

    def _get_connect(self):
        """
        得到数据库连接信息函数， 返回: conn.cursor()
        """
        self.conn = pymssql.connect(host=self.host,
                                    user=self.user,
                                    password=self.pwd,
                                    database=self.db,
                                    as_dict=self.as_dict,
                                    login_timeout=60*2,
                                    charset='utf8')
        cur = self.conn.cursor()  #将数据库连接信息，赋值给cur。
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    def exec_query(self, sql):  #执行Sql语句函数，返回结果
        """
        执行查询语句,
        返回的是一个包含tuple的list，
        list的元素是记录行，tuple的元素是每行记录的字段
        """
        cursor = self._get_connect()   #获得数据库连接信息
        cursor.execute(sql)  #执行Sql语句
        result_list = cursor.fetchall()  #获得所有的查询结果
        #返回查询结果
        return result_list

    def exec_non_query(self, sql):
        """
        执行查询语句,
        无返回
        """
        cur = self._get_connect()
        cur.execute(sql)
        self.conn.commit()

    def exec_query_params(self, sql, params):
        """
        带参数的，查询语句
        """
        cursor = self._get_connect()
        cursor.execute(sql, params)
        result_list = cursor.fetchall()
        return result_list

    def close_connect(self):
        """
        关闭连接
        """
        self.conn.close()


class MySqlConnect(Connect):
    """
    连接工具类,连接数据库
    其他数据库换驱动
    """
    def __init__(self, host=None, user=None, pwd=None, db=None,as_dict=False):
        """
        类的构造函数，初始化数据库连接ip或者域名，以及用户名，密码，要连接的数据库名称
        host=None,
        user=None
        pwd=None,
        db=None,
        as_dict=False 返回结果是否用字典的形式 默认是元组

        """
        super().__init__(host=host, user=user, pwd=pwd, db=db,as_dict=as_dict)

    def _get_connect(self):
        """
        得到数据库连接信息函数， 返回: conn.cursor()
        """
        self.conn = pymysql.connect(host=self.host,
                                    user=self.user,
                                    password=self.pwd,
                                    database=self.db,
                                    read_timeout=60*2,
                                    charset='utf8')
        if self.as_dict:
            cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        else:
            cur = self.conn.cursor()  #将数据库连接信息，赋值给cur。
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    def exec_query(self, sql):  #执行Sql语句函数，返回结果
        """
        执行查询语句,
        返回的是一个包含tuple的list，
        list的元素是记录行，tuple的元素是每行记录的字段
        """
        cursor = self._get_connect()   #获得数据库连接信息
        cursor.execute(sql)  #执行Sql语句
        result_list = cursor.fetchall()  #获得所有的查询结果
        #返回查询结果
        return result_list

    def exec_non_query(self, sql):
        """
        执行查询语句,
        返回的是一个包含tuple的list，
        list的元素是记录行，tuple的元素是每行记录的字段
        """
        cur = self._get_connect()
        cur.execute(sql)
        self.conn.commit()

    def exec_query_params(self, sql, params):
        """
        带参数的，查询语句
        """
        cursor = self._get_connect()
        cursor.execute(sql, params)
        result_list = cursor.fetchall()
        return result_list

    def close_connect(self):
        """
        关闭连接
        """
        self.conn.close()


class ConnectFactory():
    """
    工厂模式 创建数据库连接实例
    """
    @staticmethod
    def create_mysql_connect(host=None, user=None, pwd=None, db=None,as_dict=False):
        return MySqlConnect(host=host, user=user, pwd=pwd, db=db,as_dict=as_dict)

    @staticmethod
    def create_ms_connect(host=None, user=None, pwd=None, db=None,as_dict=False):
        return MSConnect(host=host, user=user, pwd=pwd, db=db,as_dict=as_dict)


if __name__ == '__main__':
    # SQLSERVER db info ,
    #  加班写
    c = ConnectFactory.create_mysql_connect()










