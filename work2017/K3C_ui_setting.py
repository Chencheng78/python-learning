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
import base64


class K3C(object):

    def __init__(self, username, password):

        self.base_url = 'http://p.to/cgi-bin/'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/'
                                 '53.0', 'Content-Type': 'application/json'}
        # === get stok / Password (base64 encryption): admin  === #
        self.username = username
        self.password = base64.b64encode(password)
        # self.login = {"method": "set", "module": {"security": {"login": {"username": "admin", "password": "YWRtaW4%3D"}}}, "_deviceType": "pc"}
        self.login = {"method": "set", "module": {"security": {"login": {"username": self.username, "password": self.password}}}, "_deviceType": "pc"}
        # === get device list === #
        self.client_list = {"method": "get", "module": {"device_manage": {"client_list": "null"}}, "_deviceType": "pc"}
        # === Set/get wifi settings === #
        self.wifi_settings = {"method": "set",
                               "module": {
                                 "wireless":
                                 {"smart_connect": {"enable": "0"},
                                  "wifi_2g_config": {"enable": "1",
                                                     "ssid": "5FLAB",
                                                     "password": "11111111",
                                                     "hidden": "0",
                                                     "mode": "0",
                                                     "channel": "0",
                                                     "band_width": "1",
                                                     "ap_isolate": "0",
                                                     "mu_mimo": "1",
                                                     "beamforming": "1"},
                                  "wifi_5g_config": {"enable": "1",
                                                     "ssid": "5FLAB_5G",
                                                     "password": "11111111",
                                                     "hidden": "0",
                                                     "mode": "0",
                                                     "channel": "0",
                                                     "band_width": "3",
                                                     "ap_isolate": "0"}}},
                               "_deviceType": "pc"}
        # === get router status === #
        self.router_status = {"method": "get", "module": {"device": {"info": "null"},
                                                          "network": {"wan_status": "null", "lan": "null"},
                                                          "wireless": {"wifi_2g_status": "null", "wifi_5g_status": "null"},
                                                          "usb": {"device": "null"}}, "_deviceType": "pc"}
        # === internet settings === #
        self.pppoe_json = {"method": "set", "module": {"network": {
            "wan": {"protocol": "pppoe", "clone_mode": "0", "mac": "", "source_mac": "74%3A7D%3A24%3A53%3AC6%3A3A"},
            "pppoe": {"username": "admin", "password": "admin", "server": "", "mtu": "1480", "dns_mode": "0",
                      "dns_pri": "", "dns_sec": ""}}}, "_deviceType": "pc"}
        self.dhcp_json = {"method":"set","module":{"network":{"wan":{"protocol":"dhcp","clone_mode":"0","mac":"","source_mac":"74%3A7D%3A24%3A53%3AC6%3A3A"},"dhcp":{"mtu":"1500","dns_mode":"0","dns_pri":"","dns_sec":""}}},"_deviceType":"pc"}

        # === firmware upgrade === #
        # self.firmware

    def get_stok(self):
        get_token = requests.post(self.base_url, data=json.dumps(self.login), headers=self.headers)
        stok = json.loads(get_token.content)['module']['security']['login']['stok']
        return stok

    # ==========WIFISET=========== #
    def wifi_switch(self, band24=1, band5=1):

        send_data = self.base_url + 'stok=' + self.get_stok() + '/data'
        self.wifi_settings['module']['wireless']['wifi_2g_config']['enable'] = str(band24)
        self.wifi_settings['module']['wireless']['wifi_5g_config']['enable'] = str(band5)
        r = requests.post(send_data, headers=self.headers, data=json.dumps(self.wifi_settings))
        return r.content

    # MODE: 0=BGN, 1=BG ONLY, 2=N ONLY | CHANNEL: 0=AUTO; 1~13 | BANDWIDTH 0=20 1=20/40 2=40
    def wifi_ssid_set24(self, ssid, password, hidden=0, mode=0, channel=0, bandwidth=1, ap_isolate=0):
        self.wifi_settings['module']['wireless']['wifi_2g_config']['ssid'] = str(ssid)
        self.wifi_settings['module']['wireless']['wifi_2g_config']['password'] = password
        self.wifi_settings['module']['wireless']['wifi_2g_config']['hidden'] = str(hidden)
        self.wifi_settings['module']['wireless']['wifi_2g_config']['mode'] = str(mode)
        self.wifi_settings['module']['wireless']['wifi_2g_config']['channel'] = str(channel)
        self.wifi_settings['module']['wireless']['wifi_2g_config']['band_width'] = str(bandwidth)
        self.wifi_settings['module']['wireless']['wifi_2g_config']['ap_isolate'] = str(ap_isolate)
        send_data = self.base_url + 'stok=' + self.get_stok() + '/data'
        r = requests.post(send_data, headers=self.headers, data=json.dumps(self.wifi_settings))
        return r.content

    # MODE: 0=A/N/AC,1=N/AC ONLY | CHANNEL: 0=AUTO, 36~48;149~165 | BANDWIDTH: 0=20,1=40,2=80,3=20/40/80
    def wifi_ssid_set5(self, ssid, password, hidden=0, mode=0, channel=0, bandwidth=3, ap_isolate=0):
        self.wifi_settings['module']['wireless']['wifi_5g_config']['ssid'] = str(ssid)
        self.wifi_settings['module']['wireless']['wifi_5g_config']['password'] = password
        self.wifi_settings['module']['wireless']['wifi_5g_config']['hidden'] = str(hidden)
        self.wifi_settings['module']['wireless']['wifi_5g_config']['mode'] = str(mode)
        self.wifi_settings['module']['wireless']['wifi_5g_config']['channel'] = str(channel)
        self.wifi_settings['module']['wireless']['wifi_5g_config']['band_width'] = str(bandwidth)
        self.wifi_settings['module']['wireless']['wifi_5g_config']['ap_isolate'] = str(ap_isolate)
        send_data = self.base_url + 'stok=' + self.get_stok() + '/data'
        r = requests.post(send_data, headers=self.headers, data=json.dumps(self.wifi_settings))
        return r.content

    def get_ssid(self):
        return [self.wifi_settings['module']['wireless']['wifi_2g_config']['ssid'],
                self.wifi_settings['module']['wireless']['wifi_5g_config']['ssid']]

    # ==========DEVICE MANAGE=========== #
    def online_status(self, mac_addr):
        send_data = self.base_url + 'stok=' + self.get_stok() + '/data'
        r = requests.post(send_data, headers=self.headers, data=json.dumps(self.client_list))
        client_lists = json.loads(r.content)['module']['device_manage']['client_list']
        for i in client_lists:
            mac_addr = mac_addr.replace(':', '%3a')
            if i['mac'] == mac_addr:
                return [i['ip'], i['online_status']]
        return 0

    # =========ADVANCED========= #
    def get_router_status(self):
        send_data = self.base_url + 'stok=' + self.get_stok() + '/data'
        r = requests.post(send_data, headers=self.headers, data=json.dumps(self.router_status))
        status = json.loads(r.content)
        return status

    def set_internet_pppoe(self):
        mac_addr = self.get_router_status()['module']['device']['info']['mac']
        self.pppoe_json['module']['network']['wan']['source_mac'] = mac_addr
        send_data = self.base_url + 'stok=' + self.get_stok() + '/data'
        r = requests.post(send_data, headers=self.headers, data=json.dumps(self.pppoe_json))
        return r.content

    def set_internet_dhcp(self):
        mac_addr = self.get_router_status()['module']['device']['info']['mac']
        self.dhcp_json['module']['network']['wan']['source_mac'] = mac_addr
        send_data = self.base_url + 'stok=' + self.get_stok() + '/data'
        r = requests.post(send_data, headers=self.headers, data=json.dumps(self.dhcp_json))
        return r.content

    def upgrade(self, files):
        firmware_dir = {'files': open(files, 'rb')}
        send_data = self.base_url + 'stok=' + self.get_stok() + '/system/upgrade'
        r = requests.post(send_data, files=firmware_dir)
        return r.status_code

    def reboot(self):
        send_data = self.base_url + 'stok=' + self.get_stok() + '/system/reboot'
        r = requests.post(send_data, headers=self.headers, data=json.dumps(self.router_status))
        return r.status_code

    def reset(self):
        send_data = self.base_url + 'stok=' + self.get_stok() + '/system/reset'
        r = requests.post(send_data, headers=self.headers, data=json.dumps(self.router_status))
        return r.status_code

    def register(self):
        reg = {"method": "set", "module": {"security": {"register": {"username":self.login, "password": self.password}}}, "_deviceType":"pc"}
        timezone = {"method": "set", "module": {"time_zone": {"config": {"region": "00800"}}}, "_deviceType": "pc"}
        network = {"method": "set", "module": {"network": {"wan": {"protocol": "dhcp"}, "dhcp": {}}}, "_deviceType": "pc"}
        wifi = {"method": "set", "module": {"welcome": {"config": {"guide": "0"}},
                                     "wireless": {"smart_connect": {"enable": "0"},
                                                  "wifi_2g_config": {"ssid": "%40PHICOMM_3A", "password": ""},
                                                  "wifi_5g_config": {"ssid": "%40PHICOMM_3A_5G", "password": ""}}},
         "_deviceType": "pc"}
        r1 = requests.get('http://p.to/cgi-bin/pc/setLgPwd.htm', headers=self.headers)
        time.sleep(0.5)
        r2 = requests.post(self.base_url, headers=self.headers, data=json.dumps(reg))
        time.sleep(0.5)

        stok = json.loads(r2.content)['module']['security']['register']['stok']
        send_data = self.base_url + 'stok=' + stok + '/data'
        r3 = requests.post(send_data, headers=self.headers, data=json.dumps(timezone))
        time.sleep(0.5)
        print r3.content
        r4 = requests.post(send_data, headers=self.headers, data=json.dumps(network))
        time.sleep(0.5)
        print r4.content
        r5 = requests.post(send_data, headers=self.headers, data=json.dumps(wifi))

        return r5.content

    def __repr__(self):
        return self.wifi_settings


class netsh(object):

    def __init__(self, interface, ssid24, ssid5):
        self.ssid24 = ssid24
        self.ssid5 = ssid5
        self.interface = interface

    @staticmethod
    def disconnect():
        cmd_disconnect = subprocess.check_output('netsh wlan disconnect').decode('gbk')
        return cmd_disconnect

    @staticmethod
    def show_wlan_status():
        a = subprocess.Popen('netsh wlan show interfaces', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        line = a.stdout.read()
        # print line.decode('gbk')
        return line.decode('gbk')

    def connect_24g(self):
        profile = 'netsh wlan add profile filename="%s-%s.xml" interface="%s"' \
                  % (self.interface, self.ssid24, self.interface)
        # print profile
        try:
            add_profile = subprocess.check_output(profile).decode('gbk')
            check_profile = re.search(u'(已将配置文件)', add_profile)
            if not check_profile:
                raise ValueError('Please check the profile name and put the profile under current working directory.')
        except Exception as e:
            logging.warning(e)
        sleep(2)
        cmd_24 = 'netsh wlan connect name="%s" interface="%s"' % (self.ssid24, self.interface)
        # adding retry loops to increase the robustness.
        try:
            retry = 0
            while retry < 3:
                connect24 = subprocess.check_output(cmd_24).decode('gbk')
                sleep(1)
                retry += 1
            return connect24
        except Exception as e:
            logging.warning(e)

    def connect_5g(self):
        profile = 'netsh wlan add profile filename="%s-%s.xml" interface="%s"' \
                  % (self.interface, self.ssid5, self.interface)
        print profile
        try:
            print 'try'
            add_profile = subprocess.check_output(profile).decode('gbk')
            check_profile = re.search(u'(已将配置文件)', add_profile)
            print add_profile
            if not check_profile:
                raise ValueError('Please check the profile name and put the profile under current working directory.')
        except Exception as e:
            print e
        sleep(2)
        cmd_5 = 'netsh wlan connect name="%s" interface="%s"' % (self.ssid5, self.interface)
        try:
            retry = 0
            while retry < 3:
                connect5 = subprocess.check_output(cmd_5).decode('gbk')
                sleep(1)
                retry += 1
            return connect5
        except Exception as e:
            logging.warning(e)

    def check_wlan_connection(self):
        status = netsh.show_wlan_status()
        connection = re.search(u'(状态.+: )(.+)\\r', status)
        ssid_name = re.search(r'(SSID.+: )(.*)\r', status)
        c = connection.group(2)
        # print c
        if c == u'\u5df2\u8fde\u63a5':
            # print c
            # print '2' + ssid_name.group(2)
            # print self.ssid24
            if ssid_name.group(2) == self.ssid24:
                print '2.4G connected.'
            elif ssid_name.group(2) == self.ssid5:
                print '5G connected.'
            else:
                print '%s is not correct SSID under the test' % ssid_name.group(2)
                return 0
            return ssid_name.group(2)
        else:
            print 'not connected!'
            return 0


def run(count, band, wifiset, command, mac):
    current_day = time.strftime('%Y_%m_%d', time.localtime())
    current_time = time.strftime('%H_%M_%S', time.localtime())

    # logging.basicConfig(filename='wifiset.log', filemode='w', level=logging.DEBUG)
    logging.basicConfig(level=logging.INFO, filename='wifiset.log', filemode='w',
                        format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%d %b %Y %H:%M:%S')
    try:
        os.mkdir(r'k:/Reboot/wifi_stability_%s' % current_day)

    except:pass
    logging.info('creating test execl file...')
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('wifi_interface_switching', cell_overwrite_ok=True)
    sheet.write(0, 0, 'COUNT')
    sheet.write(0, 1, 'RESULTS')
    sheet.write(0, 2, 'COMMENTS')

    # step 1: initialize ENV.
    logging.info('DUT and client initializing...')
    wifiset.wifi_switch()
    command.disconnect()
    sleep(60)

    # run test loop
    for i in range(1, count+1):
        ret = 1

        # step 2: connect 2.4G wifi (retry 3 times)
        if band == '24':
            logging.info('No.%i: connecting to 2.4G network...' % i)
            command.connect_24g()
            sleep(8)
        # step 3-1: check the connection status from PC, set the fail flag if not connected.
            s1 = command.check_wlan_connection()
            logging.info('NO.%i: connected to SSID: %s' % (i, s1))
            if s1 != wifiset.get_ssid()[0]:
                # print 'failed step3'
                logging.warning('Failed to connect to correct SSID: %s' % wifiset.get_ssid()[0])
                ret = 0
        elif band == '5':
            logging.info('No.%i: connecting to 5G network...' % i)
            command.connect_5g()
            sleep(8)
            # step 3-1: check the connection status from PC, set the fail flag if not connected.
            s1 = command.check_wlan_connection()
            logging.info('NO.%i: connected to SSID: %s' % (i, s1))
            if s1 != wifiset.get_ssid()[0]:
                # print 'failed step3'
                logging.warning('Failed to connect to correct SSID: %s' % wifiset.get_ssid()[1])
                ret = 0
        else:
            raise ValueError('The band parameter should be either "2.4" or "5".')
        # step 3-2:  check the online statue on WEBUI and ping gateway/baidu.com.
        dev_status = test.online_status(mac)
        if not dev_status:
            ret = 0
            logging.warning('MAC:  %s is not listed on device list.' % mac)
        elif dev_status[1] == '1':
            cmd1 = 'ping 192.168.2.1 -n 1 -S ' + dev_status[0]
            cmd2 = 'ping www.baidu.com -n 1 -S ' + dev_status[0]
            a = subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            line1 = a.stdout.read()
            loss1 = re.search(u'(\()(.+)( 丢失\))', line1.decode('gbk'))
            if loss1.group(2) != '0%':
                ret = 0
                logging.info(line1.decode('gbk'))
                logging.warning('cannot ping through 192.168.2.1')
            b = subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            line2 = b.stdout.read()
            loss2 = re.search(u'(\()(.+)( 丢失\))', line2.decode('gbk'))
            if loss2.group(2) != '0%':
                ret = 0
                logging.info(line2.decode('gbk'))
                logging.warning('cannot ping through internet')
        else:
            ret = 0
            logging.warning('device offline.')

        # step 4: shutdown 2.4G wifi interface.
        logging.info('shutting down wireless interface...')
        if band == '2.4':
            wifiset.wifi_switch(0, 1)
        else:
            wifiset.wifi_switch(1, 0)
        sleep(70)
        # step 5: check the wifi connection, if status is not 'not connected', mark the connected SSID.
        s2 = command.check_wlan_connection()
        logging.info('connection status: %s' % s2)
        if s2:
            ret = 0
            logging.warning('FAILED, Wrong connection status!')
            logging.info(command.show_wlan_status())
            sheet.write(i, 2, command.check_wlan_connection())
        # step 6 : set the results to excel.
        sheet.write(i, 0, i)
        if ret:
            sheet.write(i, 1, 'PASS')
        else:
            sheet.write(i, 1, 'FAIL')
        book.save(r'k:/Reboot/wifi_stability_%s/test_%s.csv' % (current_day, current_time))
        # step 7: teardown. restart wifi interface.
        wifiset.wifi_switch()
        sleep(60)
        command.disconnect()

    logging.info('DONE!')

if __name__ == '__main__':
    test = K3C('admin', 'admin')
    #cmd = netsh('WLAN', '5FLAB', '5FLAB_5G')
    #run(1, '5', test, cmd, '50:9a:4c:47:1e:ad')
    #print test.online_status('50:9a:4c:47:1e:ad')
    #print test.wifi_set(0, 1)
    #cmd.connect_5g()
    #print test.reset()
    #sleep(300)
    #print test.wifi_ssid_set5('5FLAB_5G','11111111',hidden=0)

    #print test.get_router_status()
    #print test.get_router_status()['module']['device']['info']['mac']
    while 1:
        test.set_internet_dhcp()
        time.sleep(20)
        test.wifi_ssid_set5('Repo_issue5', '11111111', hidden=0, mode=1, channel=149, bandwidth=1)
        time.sleep(5)
        test.wifi_ssid_set24('Repo_issue24', '11111111', hidden=0, mode=2, channel=1, bandwidth=2)
        time.sleep(20)
        print test.get_router_status()
        time.sleep(1)
        test.set_internet_pppoe()
        time.sleep(40)
        test.wifi_ssid_set5('Repo_issue5', '11111111')
        time.sleep(5)
        test.wifi_ssid_set24('Repo_issue24', '11111111')
        time.sleep(20)
        print test.get_router_status()
        time.sleep(1)




