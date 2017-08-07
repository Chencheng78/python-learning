# -*- coding: utf-8 -*-
import sys
from COMMON.LogMod import *

import os
import re
import getopt
import time
import subprocess
import logging
import string
import csv
from ctypes import *
from CHRAPI import *
import Spec_CHR
from run_chr import MyCHRLibrary
sys.path.append("..")

# 模式索引
Mode_IndexMap = {
    '11B': 0,
    '11G': 1,
    '11A': 2,
    '11N': [3,4],
    '11AC': [5,6,7,8]
    }

# 带宽索引
BW_IndexMap = {
    '20M':0,
    '40M':1,
    '80M':2,
    '160M':3
    }

if __name__ == '__main__':
    lib = MyCHRLibrary()

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hv', ['help', 'version', 'net_check', 'err_check', 'e1_ip=', 'e2_ip=',
                                                         'test_type=', 'network_type=','max_wait=',
                                                         'run_time=', 'num_cards=', 'num_pairs=',
                                                         'script_file=','res_file='])
    except getopt.GetoptError, err:
        print str(err)
        lib.Usage()
        sys.exit(2)

    for o, a in opts:
        if o in ('-h', '--help'):
            lib.Usage()
            sys.exit(1)
        elif o in ('-v', '--version'):
            lib.Version()
            sys.exit(0)
        elif o in ('--e1_ip'):
            #print o, a
            Spec_CHR.e1_ip = a.split('/')
        elif o in ('--e2_ip'):
            #print o, a
            Spec_CHR.e2_ip = a
        elif o in ('--err_check'):
            #
            #print 'Check the error log'
            lib.SetConf_CHR_Mod('ErrCheck','info')
            lib.CheckError()
            sys.exit(0)
        elif o in ('--net_check'):
            #
            #print 'Check the network'
            lib.SetConf_CHR_Mod('NetCheck','info')
            lib.CheckNetwork(Spec_CHR.num_cards)
            sys.exit(0)
        elif o in ('--test_type'):
            #print o, a
            Spec_CHR.test_type = a
        elif o in ('--network_type'):
            #print o, a
            Spec_CHR.network_type = a
        elif o in ('--max_wait'):
            #print o, a
            Spec_CHR.max_wait = string.atoi(a)
        elif o in ('--run_time'):
            #print o, a
            Spec_CHR.run_time = string.atoi(a)
            Spec_CHR.max_wait = Spec_CHR.run_time + 30
        elif o in ('--num_cards'):
            #print o, a
            Spec_CHR.num_cards = string.atoi(a)
        elif o in ('--num_pairs'):
            #print o, a
            Spec_CHR.num_pairs = string.atoi(a)
        elif o in ('--script_file'):
            #print o, a
            Spec_CHR.script_file = str(a)
        elif o in ('--res_file'):
            #print o, a
            Spec_CHR.res_file = str(a)
        else:
            #print o, a
            lib.Usage()
            sys.exit(1)

    print 'Running...'
    #
    lib.SetConf_CHR_Mod(Spec_CHR.test_type,'info')
    #
    lib.ImportDll()
    print lib.Initialize()

    test = lib.CreateTestNew()
    #
    lib.SetPairsAttribute(test)
    #
    #dgopts = lib.GetDGOpts(test)
    #lib.SetDgoptsRecvTimeout(dgopts, 2000)
    #lib.SetDgoptsRetransTimeout(dgopts, 2000)
    #
    runopts = lib.GetRunOpts(test)
    #lib.SetConnectTimeout(runopts, 1)
    #timeout = lib.GetConnectTimeout(runopts)
    lib.SetTestEnd(runopts, CHR_TEST_END_AFTER_FIXED_DURATION)
    lib.SetTestDurationt(runopts, Spec_CHR.run_time)
    lib.SetSavingFile(test, Spec_CHR.res_file)
    lib.SaveTest(test)
    #

    lib.StartTest(test)
    lib.WaitForTest(test)
    #lib.GetPairCount(test)
    #lib.GetPairAddr_e1(pair)
    #lib.GetPairAddr_e2(pair)
    #lib.GetPairProtocol(pair)
    #lib.GetPairScript(pair)
    #lib.GetPairApplScript(pair)
    #lib.GetPairTimRecordCnt(pair)
    #
    thr_all = 0.0
    thr_e1 = 0.0
    thr_e2 = 0.0
    thr_e1_tx = 0.0
    pairs = lib.GetPairs()
    bytes_sent_e1_tx = []
    bytes_recv_e1_tx = []
    bytes_sent_e1_rx = []
    bytes_recv_e1_rx = []
    time_elapsed_max = 1.0
    for pair in pairs:
        #
        num = lib.GetPairTimRecordCnt(pair)
        handle = lib.GetPairTimRecord(pair, num-1)
        time_elapsed = lib.GetPairTimElapsed(handle)
        print pair
        print num
        print handle
        print time_elapsed
        if time_elapsed > time_elapsed_max:
            time_elapsed_max = time_elapsed
        #
        cur_ip = lib.GetPairAddr_e1(pair)
        comment = lib.GetPairComment(pair, CHR_MAX_PAIR_COMMENT)
        print cur_ip
        print comment
        pair_header_len = 14
        pair_no = string.atoi(str(comment[pair_header_len:]))
        card_header_len = 6
        card_no = string.atoi(str(comment[card_header_len]))
        #
        single_thr_no = Spec_CHR.num_pairs/Spec_CHR.num_cards/2
        #thr_avg = lib.GetPairRes_Avg(pair, CHR_RESULTS_THROUGHPUT)ss
        sent_tmp = lib.GetPairBytesSentE1(pair)
        recv_tmp = lib.GetPairBytesRecvE1(pair)
        if Spec_CHR.network_type == 'LAN':
            if cur_ip in Spec_CHR.e1_ip:
                #thr_e1 += string.atof(thr_avg)
                bytes_sent_e1_tx.append(sent_tmp)
                bytes_recv_e1_tx.append(recv_tmp)
            #
            else:
                #thr_e2 += string.atof(thr_avg)
                bytes_sent_e1_rx.append(sent_tmp)
                bytes_recv_e1_rx.append(recv_tmp)
        elif Spec_CHR.network_type == 'WAN':
            if cur_ip in Spec_CHR.e1_ip:
                #thr_e1 += string.atof(thr_avg)
                if Spec_CHR.test_type == 'TX':
                    bytes_sent_e1_tx.append(sent_tmp)
                    bytes_recv_e1_tx.append(recv_tmp)
                elif Spec_CHR.test_type == 'RX':
                    bytes_sent_e1_rx.append(sent_tmp)
                    bytes_recv_e1_rx.append(recv_tmp)
                else:
                    # TX
                    if ((pair_no-1)/single_thr_no)%2 == 0:
                        bytes_sent_e1_tx.append(sent_tmp)
                        bytes_recv_e1_tx.append(recv_tmp)
                    # RX
                    else:
                        bytes_sent_e1_rx.append(sent_tmp)
                        bytes_recv_e1_rx.append(recv_tmp)
            else:
                pass
    print(bytes_sent_e1_tx)
    print(bytes_recv_e1_tx)
    print(bytes_sent_e1_rx)
    print(bytes_recv_e1_rx)

    #
    for card in range(Spec_CHR.num_cards):
        #
        if cur_ip in Spec_CHR.e1_ip:
            #
            for pair_no in range(len(bytes_sent_e1_tx)):
                thr_e1 += (string.atof(str(bytes_sent_e1_tx[pair_no]))
                           + string.atof(str(bytes_recv_e1_tx[pair_no])))
            #
            thr_e1_tx = thr_e1*8/1000000/time_elapsed_max
            #
            for pair_no in range(len(bytes_sent_e1_rx)):
                thr_e1 += (string.atof(bytes_sent_e1_rx[pair_no])
                           + string.atof(bytes_recv_e1_rx[pair_no]))
            #
            thr_e1 = thr_e1*8/1000000/time_elapsed_max
        else:
            #
            for pair_no in range(len(bytes_sent_e1_tx)):
                thr_e2 += (string.atof(str(bytes_sent_e1_tx[pair_no]))
                           + string.atof(str(bytes_recv_e1_tx[pair_no])))
            #
            for pair_no in range(len(bytes_sent_e1_rx)):
                thr_e2 += (string.atof(bytes_sent_e1_rx[pair_no])
                           + string.atof(bytes_recv_e1_rx[pair_no]))
            #
            thr_e2 = thr_e2*8/1000000/time_elapsed_max
    #
    thr_all = thr_e1 + thr_e2
    str_ret = 'AVG_All = %.3f'%(thr_all)+'Mbps, ' + 'AVG_E1 = %.3f'%(thr_e1)+'Mbps, ' + 'AVG_E2 = %.3f'%(thr_e2)+'Mbps, '+ 'AVG_E1_TX = %.3f'%(thr_e1_tx)+'Mbps'

    # 写入tmp文件
    f = open('tmp.txt', 'w')
    f.write(str_ret)
    f.close()

    #thr_avg = lib.GetPairRes_Avg(pair, CHR_RESULTS_THROUGHPUT)
    #thr_min = lib.GetPairRes_Min(pair, CHR_RESULTS_THROUGHPUT)
    #thr_max = lib.GetPairRes_Max(pair, CHR_RESULTS_THROUGHPUT)
    #lib.GetPairRes_Avg(pair, CHR_RESULTS_RSSI_E1)
    lib.SetSavingFile(test, Spec_CHR.res_file)
    lib.SaveTest(test)
    for pair in pairs:
        lib.DelPair(pair)
    # 耗费时间
    lib.DelTest(test)
    #lib.ExitTest(-1)
    os.popen('taskkill /t /f /im python.exe')

