# -*- coding:utf-8 -*-

from baseclass.readconfig import ReadConfig
import time
import hashlib
from fake_useragent import UserAgent

class GetHeader(object):

    def __init__(self, path=None, cookies=None):
        self.readconfig = ReadConfig(path)
        self.__cookies = cookies

    def cal_header(self):
        # ip_port = self.readconfig.get_value('Request-Header', 'ip_port')
        # proxies = {"http": "http://" + ip_port, "https": "https://" + ip_port}
        auth = self.xdaili_proxy_auth()

        accept_lan = self.readconfig.get_value('Request-Header', 'accept_lan')
        accept_info = self.readconfig.get_value('Request-Header', 'accept_info')
        connection = self.readconfig.get_value('Request-Header', 'connection')
        accept_code = self.readconfig.get_value('Request-Header', 'accept_code')

        ua = UserAgent()
        cookie = self.__cookies
        self.__header = {}

        if(cookie):
            self.__header = {'User-Agent': ua.chrome, 'Accept-Language': accept_lan,
                              'Accept-Encoding': accept_code, 'Connection': connection,
                              'Accept': accept_info, 'Proxy-Authorization': auth,
                              'Cookie': cookie}
        else:
            self.__header = {'User-Agent': ua.chrome, 'Accept-Language': accept_lan,
                              'Accept-Encoding': accept_code, 'Connection': connection,
                              'Accept': accept_info, 'Proxy-Authorization': auth}
        return self.__header


# use xundaili service
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


    def get_header(self):
        self.__header = self.cal_header()
        return self.__header