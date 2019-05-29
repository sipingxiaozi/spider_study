# -*- coding:utf-8 -*-

from baseclass.readconfig import ReadConfig
import pymysql

class HandleMysql(object):

    def __init__(self):
        self.readconfig = ReadConfig()

    def conn_mysql(self):
        host = self.readconfig.get_value('Mysql', 'host')
        user = self.readconfig.get_value('Mysql', 'user')
        passwd = self.readconfig.get_value('Mysql', 'passwd')
        db = self.readconfig.get_value('Mysql', 'db')
        port = self.readconfig.get_value('Mysql', 'port')
        self.__conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db, port=port)
        self.__cur = self.__conn.cursor()

    def execute_sql(self, sql, data):
        self.conn_mysql()
        try:
            self.__cur.execute(sql, data)
            self.__conn.commit()
        except:
            self.__conn.rollback()

    def search(self, sql):
        self.conn_mysql()
        self.__cur.execute(sql)
        return self.__cur.fetchall()

    def close(self):
        self.__cur.close()
        self.__conn.close()

