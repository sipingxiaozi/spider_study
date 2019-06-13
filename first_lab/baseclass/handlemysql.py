# -*- coding:utf-8 -*-

from first_lab.baseclass.readconfig import ReadConfig
import pymysqlpool

class HandleMysql(object):

    def __init__(self, size):
        self.readconfig = ReadConfig()
        host = self.readconfig.get_value('Mysql', 'host')
        user = self.readconfig.get_value('Mysql', 'user')
        passwd = self.readconfig.get_value('Mysql', 'passwd')
        db = self.readconfig.get_value('Mysql', 'db')
        port = int(self.readconfig.get_value('Mysql', 'port'))
        autocommit = bool(self.readconfig.get_value('Mysql', 'autocommit'))
        config = {'host': host, 'user': user, 'password': passwd, 'database': db, 'autocommit': autocommit}
        # self.__conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db, port=port)

        self.pool = pymysqlpool.ConnectionPool(size=size, name='pool1', **config)
        # self.__conn = None
        # self.__cur = None

    def conn_mysql(self, timeout, retry_num):
        con = self.pool.get_connection(timeout, retry_num)
        return con

    def execute_sql(self, sql, data):
        con = self.conn_mysql(timeout=30, retry_num=5)
        try:
            cur = con.cursor()
            cur.execute(sql, data)
        except:
            pass
        finally:
            con.close()



    def search(self, table_name):
        con = self.conn_mysql(timeout=30, retry_num=5)
        try:
            cur = con.cursor()
            sql = "select * from " + table_name
            cur.execute(sql)
            res = cur.fetchall()
            return res
        except:
            pass
        finally:
            con.close()

    def search_single_col(self, table_name, col_name):

        con = self.conn_mysql(timeout=30, retry_num=5)
        try:
            cur = con.cursor()
            sql = "select distinct " + col_name + " from " + table_name
            cur.execute(sql)
            res = cur.fetchall()
            return res
        except:
            pass
        finally:
            con.close()

    # def close(self):
    #     self.__cur.close()
    #     self.__conn.close()

