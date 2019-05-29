# -*- coding:utf-8 -*-

from qcc.qcc_crawler import QccCrawler
from baseclass.readconfig import ReadConfig
from baseclass.getheader import GetHeader
from baseclass.readfile import ReadFile

if __name__ == '__main__':

    cookie = 'QCCSESSID=t2j46ie8veapto4gkvevcvi0c3; UM_distinctid=16abaadeac5495-00e4a1eab204c4-366f7e03-13c680-16abaadeac6bf3; zg_did=%7B%22did%22%3A%20%2216abaaded904f5-0d2283d62d5d1-366f7e03-13c680-16abaaded91832%22%7D; _uab_collina=155791012279488903991127; acw_tc=73e72d9515579101228961194e2a342daa5297cabc862aabdbdb976321; hasShow=1; CNZZDATA1254842228=1472431469-1557908174-https%253A%252F%252Fsp0.baidu.com%252F%7C1558575976; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1557973486,1558429174,1558512138,1558581160; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1558581164; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201558574360096%2C%22updated%22%3A%201558581808171%2C%22info%22%3A%201558520620759%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22bbd581960791e96a67feb6966bde8484%22%7D'

    test = QccCrawler(url='www.baidu.com', cookie=cookie)
    # print(test.get_header())
    test.load_data()

    # test = ReadConfig()
    # print(test.get_sections())
    # print(test.get_items('Request-Header'))


    # test = GetHeader(cookies=cookie)
    # print(test.get_header())


