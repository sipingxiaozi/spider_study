# -*- coding:utf-8 -*-

from qcc_lab.qcc_crawler import QccCrawler

import threadpool
import time

if __name__ == '__main__':

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time()))))
    print("========start========")

    cookie = 'UM_distinctid=16abaadeac5495-00e4a1eab204c4-366f7e03-13c680-16abaadeac6bf3; zg_did=%7B%22did%22%3A%20%2216abaaded904f5-0d2283d62d5d1-366f7e03-13c680-16abaaded91832%22%7D; _uab_collina=155791012279488903991127; acw_tc=73e72d9515579101228961194e2a342daa5297cabc862aabdbdb976321; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1557973486,1558429174,1558512138,1558581160; QCCSESSID=adf5hjvegoudc0rjiqhq3b8cs5; hasShow=1; CNZZDATA1254842228=1472431469-1557908174-https%253A%252F%252Fsp0.baidu.com%252F%7C1559198327; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1559200713; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201559200609570%2C%22updated%22%3A%201559200730536%2C%22info%22%3A%201559195139568%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qichacha.com%22%2C%22cuid%22%3A%20%22bbd581960791e96a67feb6966bde8484%22%7D'
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


