# -*- coding:utf-8 -*-

import configparser
import os

class ReadConfig(object):

    def __init__(self, path=None):
        self.cf = configparser.ConfigParser()

        if(path):
            filepath = path
        else:
            root_dir = os.path.dirname(os.path.abspath('.'))
            filepath = root_dir + "/config/config.ini"
            # print(filepath)
        try:
            self.cf.read(filepath)
        except FileNotFoundError:
            print("File Not Found")
            pass


    def get_sections(self):
        return self.cf.sections()

    def get_options(self, group):
        return self.cf.options(group)

    def get_items(self, group):
        return self.cf.items(group)

    def get_value(self, group, param):
        value = self.cf.get(group, param)
        return value