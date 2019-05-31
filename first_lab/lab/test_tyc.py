# -*- coding:utf-8 -*-

from first_lab.tyc_lab.tyc_chawler import TycCrawler
import threadpool
import time

if __name__ == '__main__':

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time()))))
    print("========start========")


    test = TycCrawler(url='https://www.tianyancha.com', thread_num=1)
    lists = test.load_data('/Users/sipingboy/GitHub/spider_study/data/company_name')

    num = 1
    for i in lists:
        if (num > 0 and '公司' in i):
            test.row_handler(i)
            num -= 1

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time()))))
    print("========over========")
