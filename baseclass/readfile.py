# -*- coding:utf-8 -*-

import os

class ReadFile(object):
    def __init__(self, filepath):
        self.filepath = filepath
        self.fp = None

    def read_lines(self):
        res = []
        if(os.path.exists(self.filepath)):
            try:
                self.fp = open(self.filepath, 'r', encoding='utf-8')
                res = self.fp.readlines()
                self.fp.close()
                return res

            except Exception:
                print("Opening DataFile Failed!")
                pass
        else:
            print("FileNotFound!")
            return res