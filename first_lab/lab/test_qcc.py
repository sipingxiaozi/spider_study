# -*- coding:utf-8 -*-

from first_lab.qcc_lab.qcc_crawler import QccCrawler
from first_lab.baseclass.getheader import GetHeader

import threadpool
import time

if __name__ == '__main__':

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time()))))
    print("========start========")

    thread_num = 1
    test = QccCrawler(url='https://www.qichacha.com', thread_num=thread_num)
    list = test.load_data('/Users/sipingboy/GitHub/spider_study/data/company_name')

    # header = GetHeader()
    # print(header.get_header())

    lists = []
    num = 0
    for i in list:
        if(num <= 10 and '公司' in i):
            num += 1
            test.row_handler(i)


    # pool = threadpool.ThreadPool(thread_num)
    # requests = threadpool.makeRequests(test.row_handler, lists)
    # [pool.putRequest(req) for req in requests]
    # pool.wait()

    # num = 10
    # for i in lists:
    #     if (num > 0 and '公司' in i):
    #
    #         if(num < 3):
    #             test.row_handler(i)
    #         num -= 1

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time()))))
    print("========over========")


    # test = ReadConfig()
    # print(test.get_sections())
    # print(test.get_items('Request-Header'))


    # test = GetHeader(cookies=cookie)
    # print(test.get_header())


