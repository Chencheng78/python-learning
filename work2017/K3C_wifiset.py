# -*- coding:utf-8 -*-

import requests
import json
import logging
from time import sleep
import time
import xlwt
import sys
import os
import threading
import re
import subprocess

class K3C(object):

    def __init__(self, band24=1, band5=1):
        self.band24 = str(band24)
        self.band5 = str(band5)
        self.base_url = 'http://p.to/cgi-bin/'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/'
                                 '53.0', 'Content-Type': 'application/json'}
        self.login = {"method": "set", "module": {"security": {"login": {"username": "admin", "password": "YWRtaW4%3D"}}},
                 "_deviceType": "pc"}
        self._wifi_settings = {"method": "set",
                               "module": {
                                 "wireless":
                                 {"smart_connect": {"enable": "0"},
                                  "wifi_2g_config": {"enable": "0",
                                                     "ssid": "5FLAB",
                                                     "password": "11111111",
                                                     "hidden": "0",
                                                     "mode": "0",
                                                     "channel": "0",
                                                     "band_width": "1",
                                                     "ap_isolate": "0",
                                                     "mu_mimo": "1",
                                                     "beamforming": "1"},
                                  "wifi_5g_config": {"enable": "0",
                                                     "ssid": "5FLAB_5G",
                                                     "password": "11111111",
                                                     "hidden": "0",
                                                     "mode": "0",
                                                     "channel": "0",
                                                     "band_width": "3",
                                                     "ap_isolate": "0"}}},
                               "_deviceType": "pc"}

    def get_stok(self):
        get_token = requests.post(self.base_url, data=json.dumps(self.login), headers=self.headers)
        stok = json.loads(get_token.content)['module']['security']['login']['stok']
        return stok

    def wifi_set(self):
        send_data = self.base_url + 'stok=' + self.get_stok() + '/data'
        logging.info(send_data)
        self._wifi_settings['module']['wireless']['wifi_2g_config']['enable'] = self.band24
        self._wifi_settings['module']['wireless']['wifi_5g_config']['enable'] = self.band5
        r = requests.post(send_data, headers=self.headers, data=json.dumps(self._wifi_settings))
        # logging.info(r.content)
        return r.content

    def __repr__(self):
        return self.wifi_set()


def check_wlan_status():
    a = subprocess.Popen('netsh wlan show interfaces', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    line = a.stdout.read()
    print line.decode('gbk')
    connection = re.search(u'(已连接)', line.decode('gbk'))
    ssid_name = re.search(r'5FLAB', line.decode('gbk'))

    if not connection:
        print 'not connected!'

    else:
        print connection.group(), ssid_name.group()

if __name__ == '__main__':
    test = K3C(1, 1)
    test.wifi_set()
    sleep(120)
    check_wlan_status()





''' 
base_url = 'http://p.to/cgi-bin/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/'
                         '53.0', 'Content-Type': 'application/json'}
login = {"method": "set", "module": {"security": {"login": {"username": "admin", "password": "YWRtaW4%3D"}}},
         "_deviceType": "pc"}
# WiFi default settings
wifi_settings = {"method": "set",
                 "module": {
                            "wireless":
                                    {"smart_connect": {"enable": "0"},
                                     "wifi_2g_config": {"enable": "0",
                                                        "ssid": "5FLAB",
                                                        "password": "11111111",
                                                        "hidden": "0",
                                                        "mode": "0",
                                                        "channel": "0",
                                                        "band_width": "1",
                                                        "ap_isolate": "0",
                                                        "mu_mimo": "1",
                                                        "beamforming": "1"},
                                     "wifi_5g_config": {"enable": "0",
                                                        "ssid": "5FLAB_5G",
                                                        "password": "11111111",
                                                        "hidden": "0",
                                                        "mode": "0",
                                                        "channel": "0",
                                                        "band_width": "3",
                                                        "ap_isolate": "0"}}},
                 "_deviceType": "pc"}

get_token = requests.post(base_url, data=json.dumps(login), headers=headers)
stok = json.loads(get_token.content)['module']['security']['login']['stok']
send_data = base_url + 'stok='+stok + '/data'
print stok, send_data
r = requests.post(send_data, headers=headers, data=json.dumps(wifi_settings))
print r.content

# reboot_r = requests.post(reboot_url, headers=headers)
'''

