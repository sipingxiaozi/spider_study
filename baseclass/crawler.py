# -*- coding:utf-8 -*-

import abc
from baseclass.getheader import GetHeader
from baseclass.handlemysql import HandleMysql

class Crawler(metaclass=abc.ABCMeta):

    def __init__(self, url, cookie, thread_num=1):
        self.__url = url
        self.__header = GetHeader(cookies=cookie).get_header()
        self.__thread_num = thread_num
        self.__db = HandleMysql()

    def get_url(self):
        return self.__url

    def get_header(self):
        return self.__header

    @abc.abstractclassmethod
    def load_data(self):
        pass

    @abc.abstractclassmethod
    def crawl(self):
        pass

    @abc.abstractclassmethod
    def save(self):
        pass

    @abc.abstractclassmethod
    def close(self):
        pass
