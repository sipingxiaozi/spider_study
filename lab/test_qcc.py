# -*- coding:utf-8 -*-

from qcc_lab.qcc_crawler import QccCrawler

import threadpool
import time

if __name__ == '__main__':

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time()))))
    print("========start========")

    thread_num = 100
    test = QccCrawler(url='https://www.qichacha.com', thread_num=thread_num)
    lists = test.load_data('/Users/sipingboy/GitHub/spider_study/data/company_name')

    # pool = threadpool.ThreadPool(thread_num)
    # requests = threadpool.makeRequests(test.test_row_handler, lists)
    # [pool.putRequest(req) for req in requests]
    # pool.wait()

    num = 1
    for i in lists:
        if (num > 0 and '公司' in i):
            num -= 1
            test.row_handler(i)

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time()))))
    print("========over========")


    # test = ReadConfig()
    # print(test.get_sections())
    # print(test.get_items('Request-Header'))


    # test = GetHeader(cookies=cookie)
    # print(test.get_header())


