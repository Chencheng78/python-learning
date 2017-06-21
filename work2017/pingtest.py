# -*- coding:utf-8 -*-
import threading
import subprocess
import os
import re
from time import sleep
from K3C_wifiset import K3C
from K3C_wifiset import netsh

cmd = netsh('WLAN', '5FLAB', '5FLAB_5G')
test = K3C()
print cmd.disconnect()
sleep(3)
connect = cmd.connect_24g()
success = re.search(u'(已成功.+)', connect)
# print success
try:
    print success.group(1)
except: pass
sleep(5)
print cmd.show_wlan_status()
status = cmd.check_wlan_connection()
print status

test.wifi_set(1, 1)
sleep(30)
status = cmd.check_wlan_connection()
print status
# status = cmd.show_wlan_status()
# connection = re.search(u'(状态.+: )(.+)\\r', status)
# print status
# print connection.group(1)
# print connection.group(2)
# print '=============='
# a = connection.group(2)
# print a
# if a == u'\u5df2\u8fde\u63a5':
#     print 'connected'
#
# a = subprocess.Popen('ping 192.168.2.1 -n 1', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# line=a.stdout.read()
# print line.decode('gbk')
# loss = re.search(u'(\()(.+)( 丢失\))', line.decode('gbk'))
# print loss.group(2)
# if loss.group != '100%':
# 	print 'fail'
# else:
# 	print 'pass'
# # for i in line:
# # 	i = i.decode('utf8')
# # 	print 'Line : ' + i
