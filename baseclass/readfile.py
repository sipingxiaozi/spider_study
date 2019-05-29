# -*- coding:utf-8 -*-

class ReadFile(object):
    def __init__(self, path="123"):
        self.path = path
        # if(path):
        #     self.__fp = open(path, 'r')
        #
        # else:
        #     print("File Not Found, Please check path")
        #     print(path)

    def readlines(self):
        print("read")

    def rowhandle(self):
        print("row handle")

    def close(self):
        if(self.__fp):
            self.__fp.close()
