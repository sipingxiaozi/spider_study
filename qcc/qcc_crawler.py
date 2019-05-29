# -*- coding:utf-8 -*-

from baseclass.crawler import Crawler
from baseclass.readfile import ReadFile
import threading


class QccCrawler(Crawler):

    def load_data(self):
        self.__read = ReadFile()
        print("hello")

    def crawl(self):
        print("crawl start, yeah")

    def parse(self):
        print("parse success")

    def save(self):
        print("hold on")

    def close(self):
        self.__read.close()
        self.__db.close()