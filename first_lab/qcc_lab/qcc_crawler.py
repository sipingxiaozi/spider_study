# -*- coding:utf-8 -*-
# get some info of some company

from first_lab.baseclass.crawler import Crawler
from first_lab.baseclass.readfile import ReadFile
import requests
from bs4 import BeautifulSoup
import bs4
import re
import time
import random
from first_lab.baseclass.getheader import GetHeader
import http.cookiejar

special_key = ['SEW-传动设备(苏州)有限公司杭州分公司', '中外运-敦豪国际航空快件有限公司浙江分公司']
timeout = 3
retry_times = 2

cookie0 = r'zg_did=%7B%22did%22%3A%20%2216abaaded904f5-0d2283d62d5d1-366f7e03-13c680-16abaaded91832%22%7D; _uab_collina=155791012279488903991127; acw_tc=73e72d9515579101228961194e2a342daa5297cabc862aabdbdb976321; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1557973486,1558429174,1558512138,1558581160; QCCSESSID=adf5hjvegoudc0rjiqhq3b8cs5; CNZZDATA1254842228=1472431469-1557908174-https%253A%252F%252Fsp0.baidu.com%252F%7C1559540083; hasShow=1; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1559544983; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201559544433913%2C%22updated%22%3A%201559544998657%2C%22info%22%3A%201559195139568%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22ccf33f5e09a7ec8685cf81d40de1afdf%22%7D'
cookie1 = r'zg_did=%7B%22did%22%3A%20%2216abaaded904f5-0d2283d62d5d1-366f7e03-13c680-16abaaded91832%22%7D; _uab_collina=155791012279488903991127; acw_tc=73e72d9515579101228961194e2a342daa5297cabc862aabdbdb976321; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1557973486,1558429174,1558512138,1558581160; QCCSESSID=adf5hjvegoudc0rjiqhq3b8cs5; CNZZDATA1254842228=1472431469-1557908174-https%253A%252F%252Fsp0.baidu.com%252F%7C1559540083; hasShow=1; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1559544839; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201559544433913%2C%22updated%22%3A%201559544861552%2C%22info%22%3A%201559195139568%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22bbd581960791e96a67feb6966bde8484%22%7D'
cookie2 = r'zg_did=%7B%22did%22%3A%20%2216abaaded904f5-0d2283d62d5d1-366f7e03-13c680-16abaaded91832%22%7D; _uab_collina=155791012279488903991127; acw_tc=73e72d9515579101228961194e2a342daa5297cabc862aabdbdb976321; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1557973486,1558429174,1558512138,1558581160; QCCSESSID=adf5hjvegoudc0rjiqhq3b8cs5; CNZZDATA1254842228=1472431469-1557908174-https%253A%252F%252Fsp0.baidu.com%252F%7C1559540083; hasShow=1; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1559544783; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201559544433913%2C%22updated%22%3A%201559544793754%2C%22info%22%3A%201559195139568%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%2256141213b5defaa82a909a6f5f68db8a%22%7D'
cookie3 = r'zg_did=%7B%22did%22%3A%20%2216abaaded904f5-0d2283d62d5d1-366f7e03-13c680-16abaaded91832%22%7D; _uab_collina=155791012279488903991127; acw_tc=73e72d9515579101228961194e2a342daa5297cabc862aabdbdb976321; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1557973486,1558429174,1558512138,1558581160; QCCSESSID=adf5hjvegoudc0rjiqhq3b8cs5; CNZZDATA1254842228=1472431469-1557908174-https%253A%252F%252Fsp0.baidu.com%252F%7C1559540083; hasShow=1; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1559544742; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201559544433913%2C%22updated%22%3A%201559544754290%2C%22info%22%3A%201559195139568%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22f01db54b3dc9c3df654e6bf3c765bcad%22%7D'
cookie4 = r'zg_did=%7B%22did%22%3A%20%2216abaaded904f5-0d2283d62d5d1-366f7e03-13c680-16abaaded91832%22%7D; _uab_collina=155791012279488903991127; acw_tc=73e72d9515579101228961194e2a342daa5297cabc862aabdbdb976321; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1557973486,1558429174,1558512138,1558581160; QCCSESSID=adf5hjvegoudc0rjiqhq3b8cs5; CNZZDATA1254842228=1472431469-1557908174-https%253A%252F%252Fsp0.baidu.com%252F%7C1559540083; hasShow=1; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1559544693; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201559544433913%2C%22updated%22%3A%201559544714393%2C%22info%22%3A%201559195139568%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22d194ffe0e09194e5ea53a637554a44f7%22%7D'
cookie5 = r'zg_did=%7B%22did%22%3A%20%2216abaaded904f5-0d2283d62d5d1-366f7e03-13c680-16abaaded91832%22%7D; _uab_collina=155791012279488903991127; acw_tc=73e72d9515579101228961194e2a342daa5297cabc862aabdbdb976321; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1557973486,1558429174,1558512138,1558581160; QCCSESSID=adf5hjvegoudc0rjiqhq3b8cs5; CNZZDATA1254842228=1472431469-1557908174-https%253A%252F%252Fsp0.baidu.com%252F%7C1559540083; hasShow=1; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1559544566; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201559544433913%2C%22updated%22%3A%201559544580248%2C%22info%22%3A%201559195139568%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22164ee30874d60967587039b4063b708a%22%7D'
cookie6 = r'zg_did=%7B%22did%22%3A%20%2216abaaded904f5-0d2283d62d5d1-366f7e03-13c680-16abaaded91832%22%7D; _uab_collina=155791012279488903991127; acw_tc=73e72d9515579101228961194e2a342daa5297cabc862aabdbdb976321; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1557973486,1558429174,1558512138,1558581160; QCCSESSID=adf5hjvegoudc0rjiqhq3b8cs5; CNZZDATA1254842228=1472431469-1557908174-https%253A%252F%252Fsp0.baidu.com%252F%7C1559540083; hasShow=1; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1559544443; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201559544433913%2C%22updated%22%3A%201559544464641%2C%22info%22%3A%201559195139568%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22164ee30874d60967587039b4063b708a%22%7D'

cookie_pool = [cookie0, cookie1, cookie2, cookie3, cookie4, cookie5, cookie6]


class QccCrawler(Crawler):

    def load_data(self, filepath):
        read_fp = ReadFile(filepath)
        read_lists = read_fp.read_lines()
        return read_lists

    def row_handler(self, data):
        line = self.pre_clean_data(data)
        insert_sql = 'insert ignore into company_info(registered_capital, paidup_capital, operating_status,founded_date,' \
                     'uniform_social_credit_code, taxpayer_iden_number, registered_number,' \
                     'orginization_code, charater, industry, approved_date, registration, area,' \
                     'eng_name, his_name, insured_num, staff_size, business_term,register_address, business_scope, company_name)' \
                     ' values (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,' \
                     '%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s)'

        insert_suc_sql = 'insert ignore into name(name) values(%s)'

        if (line != ''):
            proxy = GetHeader().proxy()
            href_pre = self.get_url()
            url_crawl = href_pre + '/search?key='
            company_map = self.crawl(url_crawl, line, proxy)
            if len(company_map) > 0:
                value = list()
                for k in company_map.keys():
                    print(k + "  :  " + str(company_map[k]))
                    value.append(company_map[k])
                value.append(line)
                data = (int(value[0]), int(value[1]), int(value[2]), value[3], value[4], value[5],
                        value[6], value[7], value[8], value[9], value[10],
                        value[11], value[12], value[13], value[14], int(value[15]),
                        value[16], value[17], value[18], value[19], value[20])
                self.save(insert_sql, data)
                self.save(insert_suc_sql, value[20])
                time.sleep(5)

        else:
            pass


    def pre_clean_data(self, data):
        line = str(data.split('\t')[0]).strip('\r')
        if ('公司' in line):
            if(line in special_key):
                return line
            else:
                if('-' in line):
                    line = line.split('-')[0]
                if('——' in line):
                    line = line.split('——')[0]
                return line
        else:
            return ''

    def request(self, url, proxies, timeout, retry_times):
        # print("retry times: " + str(retry_times))
        retry_flag = True
        session = requests.session()
        status_code = 0
        while (retry_flag and retry_times > 0):
            try:
                print(url)
                self.cnt += 1
                header = GetHeader(cookies=random.choice(cookie_pool)).get_header()
                # print(header)
                time.sleep(random.randint(3, 5))
                res = session.get(url, headers=header, proxies=proxies,  timeout=timeout,
                                  verify=False, allow_redirects=False)
                # cookie = res.cookies.get_dict()
                # print(str(cookie))
                print(str(self.cnt))

                status_code = res.status_code
                # print("status_code:  " + str(status_code))
                if(status_code == 200):
                    if(res.text.find('index_verify') == -1):
                        # print(res.text)
                        retry_flag = False
                        try:
                            bs_obj = BeautifulSoup(res.text, 'html.parser')
                        except AttributeError as e:
                            print(e)
                            pass
                        return bs_obj
                    else:
                        print(res.text)
                        retry_times -= 1
                        pass
                else:
                    retry_times -= 1
                    if(status_code == 301 or status_code == 302):
                        loc = res.headers['Location']
                        url = self.get_url() + loc
                        # print(url)
                        retry_flag = False
                    else:
                        pass
            except Exception as e:
                print(e)
                retry_times -= 1

    def crawl(self, url1, url2, proxies):
        company_url = self.get_company_name(url1, url2, proxies, retry_times)
        if(company_url != ''):
            company_map = self.get_company_info(company_url, proxies, retry_times+1)
            return company_map
        else:
            return {}


    def get_company_name(self, url, data, proxies, retry_times):
        # time.sleep(random.randint(3, 5))
        crawl_url = url + data
        # print(crawl_url)
        retry_flag = True
        href = ''
        while(retry_flag and retry_times > 0):
            # print("get cp name Retry times: " + str(retry_times))

            try:
                bs_obj = self.request(crawl_url, proxies, timeout, retry_times)
                page = bs_obj.find('tbody', {'id': 'search-result'})
                if isinstance(page, bs4.element.Tag):
                    retry_flag = False
                    page = page.select('a')
                    href = ''
                    for i in page:
                        res_name = i.get_text()
                        if res_name == data:
                            pattern = 'href.*\.html'
                            href_tmp = re.findall(pattern, str(i))
                            href_start = str(href_tmp[0]).find('\"') + 1
                            href_pre = self.get_url()
                            href = href_pre + str(href_tmp[0])[href_start::]

                    if href == '':
                        print("Can't find the company")
                else:
                    print(bs_obj)
                    retry_times -= 1
            except AttributeError as e:
                print(e)
                retry_times -= 1
        return href

    def get_company_info(self, url, proxies, retry_times):
        # print(url)
        # time.sleep(random.randint(3, 10))
        retry_flag = True
        company_map = {}
        while(retry_flag and retry_times > 0):
            # print("get cp info Retry times: " + str(retry_times))

            try:
                bs_obj = self.request(url, proxies, timeout, retry_times)
                info_lists = bs_obj.find('table', {'class': 'ntable'})
                if isinstance(info_lists, bs4.element.Tag):
                    retry_flag = False
                    info_lists = info_lists.find_next_sibling().select('td')
                    num = 0
                    key = ""
                    for i in info_lists:
                        num += 1
                        if(num % 2 == 1):
                            key = i.get_text().replace('\n', '').replace(' ', '')
                        else:
                            value = i.get_text().replace('\n', '').replace(' ', '')
                            (key, value) = self.clean(key, value)
                            company_map[key] = value
                            key = ""
                else:
                    retry_times -= 1
            except AttributeError as e:
                print(e)
                retry_times -= 1
        return company_map


    def clean(self, key, value):
        if(key == "企业地址" or key == "住所"):
            value_tmp = value.find('查看地图')
            value = value[:value_tmp:]
        if(key == "注册资本" or (key == "实缴资本")):
            if(value == "-"):
                value = 0
            else:
                value_tmp = value.find('元')
                value = value[:value_tmp:]
                if ('万' in value):
                    rmb = value.find('万')
                    value = int(int(value[:rmb:])*10000)
                if ('亿' in str(value)):
                    rmb = str(value).find('亿')
                    value = int(int(value[:rmb:]) * 10000000)
        if(key == "成立日期" or key == "核准日期"):
            value = str(value).replace('-', '')
        if(key == '参保人数'):
            if (value == "-"):
                value = 0
            else:
                value = int(value)
        if(key == "人员规模"):
            if (value != '-'):
                tmp = value.find('人')
                value = value[:tmp:]
            else:
                value = 0
        if(key == "经营状态"):
            if (value == "存续"): value = 1
            if (value == "在业"): value = 2
            if (value == "吊销"): value = 3
            if (value == "注销"): value = 4
            if (value == "迁入"): value = 5
            if (value == "迁出"): value = 6
            if (value == "停业"): value = 7
            if (value == "清算"): value = 8
        return (key, value)


    def save(self, sql, data):
        self.pool.execute_sql(sql, data)
