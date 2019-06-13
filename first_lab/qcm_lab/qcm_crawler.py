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
timeout = 5
retry_times = 4


cookie0 = r'qznewsite.uid=vk0dj4gp30n2vt1p0axyflo1; ASP.NET_SessionId=vxrdgthhwonmkiabn0uijaou; Hm_lvt_55ad112b0079dd9ab00429af7113d5e3=1560329830; Hm_lpvt_55ad112b0079dd9ab00429af7113d5e3=1560329830; qz.newsite=95B64578D870CD0E09B949A879E62380FF1CEB0558906DE4E48DBC0C600406037FAD356FFB5E208563401FDC83D7457598689074FFC87B06FA175F509160910128AB170CDF4A01BDF9E0F6D9F8F0AD2A563EE7AE49BCBD0468560E21512209023319843567A4F386D9129474581BE126C03BBB88CCDE6957E2C31FF7DF604157C7F333E79E422ABBC2B1625F23DE18762938A7B18B2F1A564051555A1263E6CB66FFB1E11FCD7621D617712471EEE9A45418E8CBF6567376183CBC2FC02A3A816564810C'
cookie1 = r'qznewsite.uid=vk0dj4gp30n2vt1p0axyflo1; ASP.NET_SessionId=vxrdgthhwonmkiabn0uijaou; Hm_lvt_55ad112b0079dd9ab00429af7113d5e3=1560329830; Hm_lpvt_55ad112b0079dd9ab00429af7113d5e3=1560330107; qz.newsite=9ABB274F7EF32A8F95A0E3F7CBB30E9DC9FDC7D73FC235072FC66D119A73165CF64E64318723113CD60F88C874D9AD4343CC6A53F1A6A716BCD4383354D793CC7EBC5AB533FE021C74BF7C81989974C92992FC0C11614CB6F6EBC2A4611F71B0835A8B392D0B06B67F17A494F9B734027DDF82395853720F611BEB75D7E1CCAD55F5E2199E536F1D4E5A2499079BA21E974394101AAF6A0C124248903580403E96AE55B001B122A87325EF4F377EBC9C0240AEACF9A2D38E6B3784DB12D72DD06B2767D2'
cookie2 = r'qznewsite.uid=vk0dj4gp30n2vt1p0axyflo1; ASP.NET_SessionId=vxrdgthhwonmkiabn0uijaou; Hm_lvt_55ad112b0079dd9ab00429af7113d5e3=1560329830; Hm_lpvt_55ad112b0079dd9ab00429af7113d5e3=1560330150; qz.newsite=1D187CC37C8F493EB914281C2DA545AEFEF8904191261E0172E86601F5BEDEE0752191B3DA641E9C4D567AD246CF8CAEB74E9C605BDCB56FAF02802251D222F9A1CA1D4725D2A8485E44A2C71916D69FF8A146129DD78E447ABB6D36C6B7E2F9E3245BD2A0916A2CE4C55874A24332A0193179FD75AEDC85640E25A78D1ABEE81B88DAD9561517EDADA7946746EEB09190D32D60826AF9ED812FE21978E9E119E2AD46E096308143B4B861AEF2AEEC006B6A0B1E0951164AF85E06167FA4237D31916D60'
cookie3 = r'qznewsite.uid=vk0dj4gp30n2vt1p0axyflo1; ASP.NET_SessionId=vxrdgthhwonmkiabn0uijaou; Hm_lvt_55ad112b0079dd9ab00429af7113d5e3=1560329830; Hm_lpvt_55ad112b0079dd9ab00429af7113d5e3=1560330235; qz.newsite=F9C75B7741EDA0572FCB34840950E0056AC32FA2F82921E499838A70C770BF88E74FF0A1A8DC1C36681DE5ACDABF177ECB35AFFC418F528DAA30AF7AC8D52CD61D03005350CB20F690CF04E9F86F12E060FC871EA1EB48DBC62CABE9D52D98A16533927D55E00E7EC4A815DBACDC235B375CB109373795E32D886F1F31228DD10D092D3AD93983C7648393878BA7927B9211DF6233ADEC2BA3AFD71205469A3305D671D851143F65779FCAB23B4149D2019570E94E0EF26633C86611A869942F1AAEE56E'
cookie4 = r'qznewsite.uid=vk0dj4gp30n2vt1p0axyflo1; ASP.NET_SessionId=vxrdgthhwonmkiabn0uijaou; Hm_lvt_55ad112b0079dd9ab00429af7113d5e3=1560329830; Hm_lpvt_55ad112b0079dd9ab00429af7113d5e3=1560330544; qz.newsite=D6E6E9975C2C79999ED4201A9701140ABB04676600F964BA3E3F8885283C3D2AF33FAEE529C1E5BF32E3E949B2BF8077058F3F0C60FE801327FD191F2F3FDA834E7BFF91E11EAA0A12CCF473EFF3DE1580FD63A7727F33053DA061B3F6DA7284BC7FD1CECBC6055B595ED25AE766CECE21573C8CD227D7C1D23DBC99F219CA1C5D15219AF3A9A2F3D0C3AA57C5BEF0CA30208D8796D78295ACDB07997D8A78C97CD6BDCC5C1870E90E8CFD083E2DF5F1B5355B7BFE8A87AAF1A156D3DE6F4E91234C9600'


cookie_pool = [cookie0, cookie1, cookie2, cookie3, cookie4]

class QcmCrawler(Crawler):

    def load_data(self, filepath):
        read_fp = ReadFile(filepath)
        read_lists = read_fp.read_lines()
        return read_lists

    def row_handler(self, data):
        line = self.pre_clean_data(data)
        insert_sql = 'insert ignore into cp_info(name, credit_code, tax_number, register_number,' \
                     'org_no, oper_name, econ_kind, status, regist_capi, start_date, belong_org,' \
                     'teem_start_end, belong_area, check_date, address, scope, ' \
                     'industry_label, prospective_label, expo_label, other_name)' \
                     ' values (%s, %s, %s, %s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s)'

        insert_suc_sql = 'insert ignore into name(name) values(%s)'
        insert_err_sql = 'insert ignore into err_name(name) values(%s)'
        if (line != ''):
            proxy = GetHeader().proxy()
            href_pre = self.get_url()
            url_crawl = href_pre + '/search/all/'
            company_map = self.crawl(url_crawl, line, proxy)
            if len(company_map) > 0:
                value = list()

                for k in company_map.keys():
                    # print(k + "  :  " + str(company_map[k]))
                    value.append(company_map[k])
                value.append(line)
                data = (value[4], value[0], value[1], value[2], value[3], value[5], value[6],
                        value[7], float(value[8]), value[9], value[10], value[11], value[12],
                        value[13], value[14], value[15], value[16], value[17], value[18], value[19])
                self.save(insert_sql, data)
                self.save(insert_suc_sql, value[19])
                # time.sleep(5)
            else:
                print("The Error Company:  " + line)
                self.save(insert_err_sql, line)

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
               # print(url)
                self.cnt += 1
                header = GetHeader(cookies=random.choice(cookie_pool)).get_header()
                # print(header)
                time.sleep(random.randint(5, 8))
                res = session.get(url, headers=header, proxies=proxies,  timeout=timeout,
                                  verify=False, allow_redirects=False)
                # cookie = res.cookies.get_dict()
                # print(str(cookie))
                print(str(self.cnt))

                status_code = res.status_code
                # print("status_code:  " + str(status_code))
                if(status_code == 200):
                    # if(res.text.find('-') == -1):
                       # print(res.text)
                    retry_flag = False
                    try:
                        bs_obj = BeautifulSoup(res.text, 'html.parser')
                    except AttributeError as e:
                        print(e)
                        pass
                    return bs_obj
                    # else:
                    #     # print(res.text)
                    #     retry_times -= 1
                    #     pass
                else:
                    # retry_times -= 1
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
                page = bs_obj.find('ul', {'id': 'listsec'})
                # print(page)
                if isinstance(page, bs4.element.Tag):
                    # print("hello,page")
                    retry_flag = False
                    page = page.select('a')
                    # print(page)
                    cnt = 0
                    href = ''
                    str_a = ''
                    cp_name = ''
                    get_flag = True
                    for i in page:
                        if(get_flag):
                            cnt += 1
                            if(get_flag and cnt % 3 == 1):
                                str_a = i
                                # print(str_a)
                            if(get_flag and cnt % 3 == 2):
                                cp_name = i.get_text().strip('\n').strip(' ')
                            # if cp_name == data:
                                get_flag = False
                                pattern = 'href.*\.html'
                                href_tmp = re.findall(pattern, str(str_a))
                                href_start = str(href_tmp[0]).find('\"') + 1
                                href_pre = self.get_url()
                                href_last = str(href_tmp[0])[href_start::]
                                href = href_pre + href_last
                                # print(href)

                    if href == '':
                        print("Can't find the company")
                else:
                   # print(bs_obj)
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
            cnt = 1
            try:
                bs_obj = self.request(url, proxies, timeout, retry_times)
                info_lists = bs_obj.find('ul', {'class': 'art-basic'})
                if isinstance(info_lists, bs4.element.Tag):
                    retry_flag = False
                    info_lists = info_lists.select('li')
                    for i in info_lists:
                        # print(str(cnt))
                        cnt += 1
                        info = i.get_text()
                        # print(info)
                        key = info.split('：')[0].replace('\n', '').replace(' ', '')
                        value = info[len(key)+1::].replace('\n', '').replace(' ', '')
                        # print(key)
                        # print(value)
                        (key, value) = self.clean(key, value)
                        company_map[key] = value

                more_labels_lists = bs_obj.find('ul', {'class': 'art-basic art-basic-swot'})
                if isinstance(more_labels_lists, bs4.element.Tag):
                    retry_flag = False
                    info_lists = more_labels_lists.select('li')
                    for i in info_lists:
                        # print(str(cnt))
                        # cnt += 1
                        info = i.get_text()
                        key = info.split('：')[0].replace('\n', '').replace(' ', '')
                        value = info[len(key)+2::].replace('\n', '').replace(' ', '')
                        # print(key)
                        # print(value)
                        (key, value) = self.clean(key, value)
                        company_map[key] = value

                else:
                    retry_times -= 1
            except AttributeError as e:
                print(e)
                retry_times -= 1
        return company_map


    def clean(self, key, value):
        # if(key == "企业地址" or key == "住所"):
        #     value_tmp = value.find('查看地图')
        #     value = value[:value_tmp:]
        if(key == "注册资本" or (key == "实缴资本")):
            # print(str(value))
            if str(value) == '-' or str(value) == '--':
                value = 0
            else:
                if '(' in value:
                    tmp = value
                    value_tmp = value.find('(')
                    value = value[:value_tmp:].replace(',', '')
                    # print(value)
                    if ('万' in tmp):
                        value = float(value) * 10000
                        # rmb = value.find('万')
                        # value = int(int(value[:rmb:])*10000)
                    if ('亿' in tmp):
                        value = float(value) * 10000000
                        # rmb = str(value).find('亿')
                        # value = int(int(value[:rmb:]) * 10000000)
                else:
                    value_tmp = value.find('元')
                    value = value[:value_tmp:]
                    if ('万' in value):
                        rmb = value.find('万')
                        value = float(value[:rmb:].replace(',', '').replace('（', ''))*10000
                    if ('亿' in str(value)):
                        rmb = str(value).find('亿')
                        value = float(value[:rmb:].replace(',', '')) * 10000000
        if(key == "成立日期" or key == "核准日期"):
            value = str(value).replace('-', '')
        # if(key == '参保人数'):
        #     if (value == "-"):
        #         value = 0
        #     else:
        #         value = int(value)
        # if(key == "人员规模"):
        #     if (value != '-'):
        #         tmp = value.find('人')
        #         value = value[:tmp:]
        #     else:
        #         value = 0
        # if(key == "经营状态"):
        #     if (value == "存续"): value = 1
        #     if (value == "在业"): value = 2
        #     if (value == "吊销"): value = 3
        #     if (value == "注销"): value = 4
        #     if (value == "迁入"): value = 5
        #     if (value == "迁出"): value = 6
        #     if (value == "停业"): value = 7
        #     if (value == "清算"): value = 8
        return (key, value)


    def save(self, sql, data):
        self.pool.execute_sql(sql, data)
