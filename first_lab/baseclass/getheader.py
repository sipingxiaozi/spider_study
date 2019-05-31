# -*- coding:utf-8 -*-

from first_lab.baseclass.readconfig import ReadConfig
import time
import hashlib
from fake_useragent import UserAgent

class GetHeader(object):

    def __init__(self, path=None, cookies=None):
        self.readconfig = ReadConfig(path)
        self.__cookies = cookies
        self.__header = {}

    def cal_header(self):
        auth = self.xdaili_proxy_auth()

        accept_lan = self.readconfig.get_value('Request-Header', 'accept_lan')
        accept_info = self.readconfig.get_value('Request-Header', 'accept_info')
        connection = self.readconfig.get_value('Request-Header', 'connection')
        accept_code = self.readconfig.get_value('Request-Header', 'accept_code')
        cache_control = self.readconfig.get_value('Request-Header', 'Cache-control')
        if_none_match = self.readconfig.get_value('Request-Header', 'If-None-Match')
        if_modified_since = self.readconfig.get_value('Request-Header', 'If-Modified-Since')
        referer = self.readconfig.get_value('Request-Header', 'Referer')


        ua = UserAgent(verify_ssl=False)
        # user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
        cookie = self.__cookies

        if(cookie):
            self.__header = {'User-Agent': ua.random, 'Accept-Language': accept_lan,
                              'Accept-Encoding': accept_code, 'Connection': connection,
                              'Accept': accept_info, 'Proxy-Authorization': auth,
                              'Cookie': cookie, 'Referer': referer,
                             'Cache-contro': cache_control, 'If-None-Match': if_none_match,
                             'If-Modified-Since': if_modified_since}
        else:
            self.__header = {'User-Agent': ua.random, 'Accept-Language': accept_lan,
                              'Accept-Encoding': accept_code, 'Connection': connection,
                              'Accept': accept_info, 'Proxy-Authorization': auth,
                             'Referer': referer,
                             'Cache-contro': cache_control, 'If-None-Match': if_none_match,
                             'If-Modified-Since': if_modified_since}
        return self.__header

# use xdaili service
    def xdaili_proxy_auth(self):
        timestamp = str(int(time.time()))
        orderno = self.readconfig.get_value('Request-Header', 'orderno')
        secret = self.readconfig.get_value('Request-Header', 'secret')
        string = "orderno=" + orderno + "," + "secret=" + secret + "," + "timestamp=" + timestamp
        md5_string = hashlib.md5(string.encode()).hexdigest()
        sign = md5_string.upper()
        auth = "sign=" + sign + "&" + "orderno=" + orderno + "&" + "timestamp=" + timestamp
        # print(auth)
        return auth

    def proxy(self):
        ip_port = self.readconfig.get_value('Request-Header', 'ip_port')
        proxies = {"http": "http://" + ip_port, "https": "https://" + ip_port}
        return proxies


    def get_header(self):
        self.__header = self.cal_header()
        return self.__header