# -*- coding:utf-8 -*-

from K3C_ui_setting import *
from time import sleep

if __name__ == '__main__':
    for i in range(20):
        test = K3C('admin', 'admin')
        # print test.get_router_status()
        ret1 = test.reset()
        if ret1 == 200:
            print 'reset success! Waiting for reboot...'
        # reboot time setting : 200s
        items = list(range(0, 100))
        l = len(items)
        # show starting time and ending time
        print time.ctime()
        printProgressBar(0, l, prefix='Progress:', suffix='Complete', length=50)
        for j, item in enumerate(items):
            # Do stuff...
            sleep(2)
            # Update Progress Bar
            printProgressBar(j + 1, l, prefix='Progress:', suffix='Complete', length=50)
        print time.ctime()
        # Quick-Guide settings
        print 'Start to config Quick-Guide.'
        ssid_24 = u'K3C_TEST_24_%d' % i
        ssid_5 = u'K3C_TEST_5_%d' % i
        print ssid_24
        print ssid_5
        ret2 = test.register('PPPoE', '00800', ssid_24, ssid_5)
        if ret2:
            print 'Quick-Guide fail'
        else:
            print 'Quick-Guide finished'
        sleep(20)
        ret3 = test.get_router_status()
        # print ret3
        if ret3['module']['network']['wan_status']['protocol'] == 'pppoe' and\
           ret3['module']['wireless']['wifi_2g_status']['ssid'] == ssid_24 and\
           ret3['module']['wireless']['wifi_5g_status']['ssid'] == ssid_5:
            print 'No.%d success' % i
        else:
            print 'No.%d failed' % i

        # test.wifi_ssid_set24('Repo_issue24', '11111111', hidden=0, mode=2, channel=1, bandwidth=2)
        # test.wifi_ssid_set5('Repo_issue5', '11111111', hidden=0, mode=1, channel=149, bandwidth=1)
