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


class MyCHRLibrary():

    ###################################################
    ### 初始化
    def __init__(self):
        self.scrip_path = os.path.abspath(os.path.dirname(__file__))
        self.logger = LogMod()
        self.pairs = []

    ###################################################
    ### 用法
    def Usage(self):
        print 'run_chr.py usage:'
        print '-h, --help: print help message.'
        print '-v, --version: print script version'
        print '--test_type: RX/TX/TX_RX'
        print '--net_check: check the network'
        print '--e1_ip: the ip list of endpoint1'
        print '--e2_ip: the ip of endpoint2'
        print '--max_wait: the max wait time, or force to stop'
        print '--run_time: thr run time of the script'
        print '--num_cards: the cards number of the endpoint1'
        print '--num_pairs: the pairs number'
        print '--script_file: the script filepath'
        print '--res_file: the result filename'

    ###################################################
    ### 版本
    def Version(self):
        print 'run_chr.py 1.0'

    #####################################################
    ### 网络检查
    def NetCheck(self, ip):
        try:
            p = subprocess.Popen("ping -n 4 -w 1 "+ ip,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 shell=True)
            out=p.stdout.read()
            #print out
            regex=re.compile('100%')
            if len(regex.findall(out)) == 0:
                #print ip + ': host up'
                return True
            else:
                print ip + ': host down'
                return False
        except:
            print 'NetCheck work error!'
            return False

    #####################################################
    ### 检查网络是否正常
    def CheckNetwork(self, num_cards):
        #print u'检查网络是否正常'
        #self.logger.LogDev('CHR', 'info', 'Check network whether OK...')
        for index in range(num_cards):
            for i in range(4):
                if self.NetCheck(Spec_CHR.e1_ip[index]) == True:
                    break
                else:
                    if i < 3:
                        time.sleep(10)
                        continue
                #
                print '[Error]: [IP: %s] 1.请确认网络连接是否正常; 2.请确认网络设置是否正确'%(Spec_CHR.e1_ip[index])
                self.logger.LogDev('CHR', 'INFO', '[Error]: [IP: %s] 1.请确认网络连接是否正常; 2.请确认网络设置是否正确'%(Spec_CHR.e1_ip[index]))
                return False
                # 退出测试
                #sys.exit(-1)
        #
        print 'Network is OK'
        return True

    #####################################################
    ### 设置chariot日志配置
    def SetConf_CHR_Mod(self, test_type, log_level):
        #print u'设置chariot日志配置'
        #self.logger.LogDev('CHR', 'info', 'Set chariot log configure...')

        test_type = str(test_type)
        log_level = str(log_level)
        if len(test_type) == 0:
            test_type = 'COMMON'
        if len(log_level) == 0:
            log_level = 'info'

        # 时间戳
        ISOTIMEFORMAT='%Y_%m_%d_%H_%M_%S'
        timestamp = time.strftime(ISOTIMEFORMAT, time.localtime())

        # 测试类型
        Spec_CHR.test_type = str(test_type)
        self.logger.SetLogConf(test_type, 'Test.log')
        # 日志级别
        self.level = log_level

    #####################################################
    ### 导入接口dll
    def ImportDll(self):
        #print u'导入接口dll'
        #self.logger.LogDev('CHR', 'info', 'Import dll interface...')
        self.dll = CDLL(self.scrip_path + '\\ChrApi.dll')

    #####################################################
    ### 转换错误信息
    def ConvertErrorInfo(self, handle, code, where):
        #print u'转换错误信息'
        #self.logger.LogDev('CHR', 'info', 'Import dll interface...')

        str_ret = None
        msg = create_string_buffer("\0", CHR_MAX_RETURN_MSG)
        msgLen = c_int(0)
        # Get the API message for this return code
        rc = self.dll.CHR_api_get_return_msg(code, msg, CHR_MAX_RETURN_MSG, byref(msgLen))
        if rc != CHR_OK:
            # Could not get the message: show why
            #print("%s failed"%where)
            #print("Unable to get message for return code %d, rc = %d"%(code,rc))
            self.logger.LogDev('CHR', 'INFO', "%s failed"%where)
            self.logger.LogDev('CHR', 'INFO', "Unable to get message for return code %d, rc = %d"%(code,rc))
        else:
            # Tell the user about the error
            #print("%s failed: rc = %d (%s)"%(where, code, msg))
            self.logger.LogDev('CHR', 'INFO', "%s failed: rc = %d (%s)"%(where, code, msg))

        errorInfo = create_string_buffer("\0", CHR_MAX_ERROR_INFO)
        errorLen = c_int(0)
        if (code == CHR_OPERATION_FAILED or code == CHR_OBJECT_INVALID) and handle != CHR_NULL_HANDLE:
            rc = self.dll.CHR_common_error_get_info(handle, CHR_DETAIL_LEVEL_ALL,
                                                    errorInfo, CHR_MAX_ERROR_INFO,
                                                    byref(errorLen))
            if rc == CHR_OK:
                #print("Extended error info:\n%s\n"%errorInfo)
                self.logger.LogDev('CHR', 'INFO', "Extended error info:\n%s\n"%errorInfo)

    #####################################################
    ### 初始化IxChariot API
    def Initialize(self):
        #print u'初始化IxChariot API'
        #self.logger.LogDev('CHR', 'info', 'Import dll interface...')

        errorInfo = create_string_buffer("\0", CHR_MAX_ERROR_INFO)
        errorLen = c_int(0)
        rc = self.dll.CHR_api_initialize(CHR_DETAIL_LEVEL_ALL, errorInfo,
                                         CHR_MAX_ERROR_INFO, byref(errorLen))
        if CHR_OK != rc:
            #print("Initialization failed: rc = %d\n"%rc)
            #print("Extended error info:\n%s\n"%errorInfo)
            self.logger.LogDev('CHR', 'INFO', "Initialization failed: rc = %d\n"%rc)
            self.logger.LogDev('CHR', 'INFO', "Extended error info:\n%s\n"%errorInfo)

        return rc

    #####################################################
    ### 设置保存文件名
    def SetSavingFile(self, test, testFile):
        #print u'设置保存文件名'
        #self.logger.LogDev('CHR', 'info', 'Set the test filename for saving...')

        rc = self.dll.CHR_test_set_filename(test, testFile, len(testFile))
        if rc != CHR_OK:
            self.ConvertErrorInfo(test, rc, "test_set_filename")

    #####################################################
    ### 创建测试
    def CreateTestNew(self):
        print u'创建测试'
        self.logger.LogDev('CHR', 'info', 'Create a test...')

        test = c_long(0)
        rc = self.dll.CHR_test_new(byref(test)); 
        if rc != CHR_OK:
            self.ConvertErrorInfo(CHR_NULL_HANDLE, rc, "test_new")
        else:
            #self.test = test.value
            return test.value

    #####################################################
    ### 创建Pair
    def CreatePairNew(self):
        print u'创建Pair'
        self.logger.LogDev('CHR', 'info', 'Create a pair...')

        pair = c_long(0)
        rc = self.dll.CHR_pair_new(byref(pair)); 
        if rc != CHR_OK:
            self.ConvertErrorInfo(CHR_NULL_HANDLE, rc, "pair_new")
        else:
            #self.pair = pair.value
            print '%s,%s,%s'% (pair, type(pair), pair.value)
            return pair.value

    #####################################################
    ### 设置Pair的endpoint地址
    def SetPairAddr(self, pair, addr_e1, addr_e2):
        print u'设置pair的e1地址'
        self.logger.LogDev('CHR', 'info', 'Set required pair attributes...')

        addr_e1 = str(addr_e1)
        addr_e2 = str(addr_e2)
        rc = self.dll.CHR_pair_set_e1_addr(pair, addr_e1, len(addr_e1))
        if rc != CHR_OK:
            self.ConvertErrorInfo(pair, rc, "pair_set_e1_addr")
        else:
            #print 'SetPairAddr(e1) OK'
            pass

        rc = self.dll.CHR_pair_set_e2_addr(pair, addr_e2, len(addr_e2))
        if rc != CHR_OK:
            self.ConvertErrorInfo(pair, rc, "pair_set_e2_addr")
        else:
            #print 'SetPairAddr(e2) OK'
            pass

    #####################################################
    ### 设置Pair的注释
    def SetPairComment(self, pair, comment):
        print u'设置Pair的注释'
        self.logger.LogDev('CHR', 'info', 'Set the required pair comment...')

        rc = self.dll.CHR_pair_set_comment(pair, comment, len(comment))
        if rc != CHR_OK:
            self.ConvertErrorInfo(pair, rc, "pair_set_comment")

    #####################################################
    ### 设置Pair的协议
    def SetPairProtocol(self, pair, protocol):
        print u'设置Pair的协议'
        self.logger.LogDev('CHR', 'info', 'Set the required pair protocol...')

        rc = self.dll.CHR_pair_set_protocol(pair, protocol)
        if rc != CHR_OK:
            self.ConvertErrorInfo(pair, rc, "pair_set_protocol")

    #####################################################
    ### 设置Pair的脚本
    def SetPairScript(self, pair, script):
        print u'设置Pair的脚本'
        self.logger.LogDev('CHR', 'info', 'Set the required pair script...')

        rc = self.dll.CHR_pair_use_script_filename(pair, script, len(script))
        if rc != CHR_OK:
            self.ConvertErrorInfo(pair, rc, "pair_use_script_filename")

    #####################################################
    ### 设置Pair的脚本嵌入Payload
    def SetPairScriptEmbeddedPayload(self, pair, send_data_type_name):
        print u'设置Pair的脚本嵌入Payload'
        self.logger.LogDev('CHR', 'info', 'Set the Script Embedded Payload...')

        embeddedPayload = 'This is a sample\0embedded payload'
        rc = self.dll.CHR_pair_set_script_embedded_payload(pair,
                                                           send_data_type_name,
                                                           len(send_data_type_name),
                                                           embeddedPayload,
                                                           33)
        if (rc != CHR_OK):
            self.ConvertErrorInfo(pair, rc, "pair_set_script_embedded_payload")

    #####################################################
    ### 设置连接超时时间（单位：min）
    def SetConnectTimeout(self, runopts, timeout):
        print u'设置连接超时时间'
        self.logger.LogDev('CHR', 'info', 'Set the connect timeout...')

        rc = self.dll.CHR_runopts_set_connect_timeout(runopts,timeout)
        if (rc != CHR_OK):
            self.ConvertErrorInfo(pair, rc, "runopts_set_connect_timeout")

    #####################################################
    ### 设置数据包接收超时时间（单位：ms）
    def SetDgoptsRecvTimeout(self, dgopts, timeout):
        print u'设置数据包接收超时时间'
        self.logger.LogDev('CHR', 'info', 'Set the datagram receive timeout...')

        rc = self.dll.CHR_dgopts_set_recv_timeout(dgopts,timeout)
        if rc != CHR_OK:
            self.ConvertErrorInfo(pair, rc, "dgopts_set_recv_timeout")

    #####################################################
    ### 设置数据包重传超时时间（单位：ms）
    def SetDgoptsRetransTimeout(self, dgopts, timeout):
        print u'设置数据包接收超时时间'
        self.logger.LogDev('CHR', 'info', 'Set the datagram receive timeout...')

        rc = self.dll.CHR_dgopts_set_retrans_timeout(dgopts,timeout)
        if rc != CHR_OK:
            self.ConvertErrorInfo(pair, rc, "dgopts_set_retrans_timeout")

    #####################################################
    ### 设置脚本运行时间（单位：s）
    def SetTestDurationt(self, runopts, duration):
        print u'设置脚本运行时间'

        rc = self.dll.CHR_runopts_set_test_duration(runopts,duration)
        if rc != CHR_OK:
            self.ConvertErrorInfo(pair, rc, "runopts_set_test_duration")

    #####################################################
    ### 设置脚本运结束方式
    def SetTestEnd(self, runopts, testend):
        print u'设置脚本运结束方式'

        rc = self.dll.CHR_runopts_set_test_end(runopts,testend)
        if (rc != CHR_OK):
            self.ConvertErrorInfo(pair, rc, "runopts_set_test_end")

    #####################################################
    ### 添加Pair到测试
    def AddPairToTest(self, test, pair):
        print u'添加Pair到测试'
        self.logger.LogDev('CHR', 'info', 'Add the pair to the test...')

        rc = self.dll.CHR_test_add_pair(test, pair)
        if rc != CHR_OK:
            self.ConvertErrorInfo(test, rc, "test_add_pair")

    #####################################################
    ### 设置Pairs属性
    def SetPairsAttribute(self, test):
        print u'设置Pairs属性'
        self.logger.LogDev('CHR', 'info', 'Add the pair attribute...')

        pair_index = 0
        #
        card_no = 0
        part = Spec_CHR.num_pairs/Spec_CHR.num_cards
        semi = part/2
        for index in range(Spec_CHR.num_cards):
            card_no += 1
            for i in range(part):
                # 创建pair
                pair = self.CreatePairNew()
                # 添加pair注释
                pair_index += 1
                comment = "[Card %d] Pair %d"%(card_no, pair_index)
                self.SetPairComment(pair, comment)
                # 设置endpoint地址
                if Spec_CHR.test_type == 'RX':
                    if Spec_CHR.network_type == 'WAN':
                        self.SetPairAddr(pair, Spec_CHR.e1_ip[index], Spec_CHR.e2_ip)
                    else:
                        self.SetPairAddr(pair, Spec_CHR.e2_ip, Spec_CHR.e1_ip[index])
                    # 设置脚本
                    self.SetPairScript(pair, Spec_CHR.script_file)
                elif Spec_CHR.test_type == 'TX':
                    self.SetPairAddr(pair, Spec_CHR.e1_ip[index], Spec_CHR.e2_ip)
                    # 设置脚本
                    self.SetPairScript(pair, Spec_CHR.script_file)
                else:
                    if i >= semi:
                        self.SetPairAddr(pair, Spec_CHR.e1_ip[index], Spec_CHR.e2_ip)
                        # 设置脚本
                        if Spec_CHR.network_type == 'WAN':
                            ll = Spec_CHR.script_file.split('_')
                            # 修改脚本名称
                            i = 0
                            for elem in ll:
                                i += 1
                                if 'Throughput' in elem:
                                    break
                            ll.insert(i, 'TX')
                            script_file = '_'.join(ll)
                            self.SetPairScript(pair, script_file)
                        else:
                            self.SetPairScript(pair, Spec_CHR.script_file)
                    else:
                        if Spec_CHR.network_type == 'WAN':
                            self.SetPairAddr(pair, Spec_CHR.e1_ip[index], Spec_CHR.e2_ip)
                            # 设置脚本
                            ll = Spec_CHR.script_file.split('_')
                            # 修改脚本名称
                            i = 0
                            for elem in ll:
                                i += 1
                                if 'Throughput' in elem:
                                    break
                            ll.insert(i, 'RX')
                            script_file = '_'.join(ll)
                            self.SetPairScript(pair, script_file)
                        else:
                            self.SetPairAddr(pair, Spec_CHR.e2_ip, Spec_CHR.e1_ip[index])
                            # 设置脚本
                            self.SetPairScript(pair, Spec_CHR.script_file)
                # 设置协议
                self.SetPairProtocol(pair, CHR_PROTOCOL_TCP)
                # 设置脚本
                #self.SetPairScript(pair, Spec_CHR.script_file)
                # 设置嵌入Payload
                #self.SetPairScriptEmbeddedPayload(pair, Spec_CHR.send_data_type_name)
                # pair添加到list中
                self.pairs.append(pair)
                # pair添加到test中
                self.AddPairToTest(test, pair)

    #####################################################
    ### 开始测试
    def StartTest(self, test):
        print u'开始测试'
        self.logger.LogDev('CHR', 'info', 'Run the test...')

        rc = self.dll.CHR_test_start(test)
        if rc != CHR_OK:
            self.ConvertErrorInfo(test, rc, "start_test")

    #####################################################
    ### 等待测试结束
    def WaitForTest(self, test):
        print u'等待测试结束...'
        self.logger.LogDev('CHR', 'info', 'Wait for the test to stop...')

        # 
        isStopped = CHR_FALSE
        timer = 0
        while (isStopped == CHR_FALSE) and (timer < Spec_CHR.max_wait):
            rc = self.dll.CHR_test_query_stop(test, Spec_CHR.timeout)
            if rc == CHR_OK:
                isStopped = CHR_TRUE
            elif rc == CHR_TIMED_OUT:
                timer += Spec_CHR.timeout
                #print("Waiting for test to stop... (%d)"%timer)
                self.logger.LogDev('CHR', 'INFO', "Waiting for test to stop... (%d)"%timer)
            else:
                self.ConvertErrorInfo(test, rc, "test_query_stop")

        #
        if (isStopped == CHR_FALSE):
            self.ConvertErrorInfo(test, CHR_TIMED_OUT, "test_query_stop")

    #####################################################
    ### 保存测试结果
    def SaveTest(self, test):
        print u'保存测试结果'
        self.logger.LogDev('CHR', 'info', 'Save the test...')

        rc = self.dll.CHR_test_save(test)
        if (rc != CHR_OK):
            self.ConvertErrorInfo(test, rc, "test_save")

    #####################################################
    ### 获取运行参数句柄
    def GetRunOpts(self, test):
        print u'获取运行参数句柄'
        self.logger.LogDev('CHR', 'info', 'Get the handle of run options...')

        runopts = c_long(0)
        rc = self.dll.CHR_test_get_runopts(test, byref(runopts))
        if (rc != CHR_OK):
            self.ConvertErrorInfo(test, rc, "test_get_runopts")
        #
        return runopts.value

    #####################################################
    ### 获取Datagram参数句柄
    def GetDGOpts(self, test):
        print u'获取Datagram参数句柄'
        self.logger.LogDev('CHR', 'info', 'Get the handle of datagram options...')

        dgopts = c_long(0)
        rc = self.dll.CHR_test_get_dgopts(test, byref(dgopts))
        if (rc != CHR_OK):
            self.ConvertErrorInfo(test, rc, "test_get_dgopts")
        #
        return dgopts.value

    #####################################################
    ### 获取连接超时时间
    def GetConnectTimeout(self, runopts):
        print u'获取连接超时时间'
        self.logger.LogDev('CHR', 'info', 'Get the handle of run options...')

        timeout = c_long(0)
        rc = self.dll.CHR_runopts_get_connect_timeout(runopts, byref(timeout))
        if (rc != CHR_OK):
            self.ConvertErrorInfo(test, rc, "runopts_get_connect_timeout")
        #
        return timeout.value

    #####################################################
    ### 获取连接超时时间
    def GetConnectTimeout(self, runopts):
        print u'获取连接超时时间'
        self.logger.LogDev('CHR', 'info', 'Get the handle of run options...')

        timeout = c_long(0)
        rc = self.dll.CHR_runopts_get_connect_timeout(runopts, byref(timeout))
        if (rc != CHR_OK):
            self.ConvertErrorInfo(test, rc, "runopts_get_connect_timeout")
        #
        return timeout.value

    #####################################################
    ### 获取测试Pair数量
    def GetPairCount(self, test):
        print u'获取测试Pair数量'
        self.logger.LogDev('CHR', 'info', 'Get the number of pairs...')

        pairCount = c_int(0)
        rc = self.dll.CHR_test_get_pair_count(test, byref(pairCount))
        if (rc != CHR_OK):
            self.ConvertErrorInfo(test, rc, "get_pair_count")
        #
        #print("Number of pairs = %d"%pairCount.value)
        self.logger.LogDev('CHR', 'INFO', "Number of pairs = %d"%pairCount.value)
        return pairCount.value

    #####################################################
    ### 获取endpoint1的地址
    def GetPairAddr_e1(self, pair):
        print u'获取endpoint1的地址'
        self.logger.LogDev('CHR', 'info', 'Get the address of endpoint1...')

        addr = create_string_buffer("\0", CHR_MAX_ADDR)
        addr_len = c_long(0)
        rc = self.dll.CHR_pair_get_e1_addr(pair, addr, CHR_MAX_ADDR, byref(addr_len))
        if (rc != CHR_OK):
            self.ConvertErrorInfo(pair, rc, "pair_get_e1_addr")
        #
        #print addr.value
        return addr.value

    #####################################################
    ### 获取endpoint2的地址
    def GetPairAddr_e2(self, pair):
        print u'获取endpoint2的地址'
        self.logger.LogDev('CHR', 'info', 'Get the address of endpoint2...')

        addr = create_string_buffer("\0", CHR_MAX_ADDR)
        addr_len = c_long(0)
        rc = self.dll.CHR_pair_get_e2_addr(pair, addr, CHR_MAX_ADDR, byref(addr_len))
        if (rc != CHR_OK):
            self.ConvertErrorInfo(pair, rc, "pair_get_e2_addr")
        #
        #print addr.value
        return addr.value

    #####################################################
    ### 获取Pair的协议
    def GetPairProtocol(self, pair):
        print u'获取Pair的协议'
        self.logger.LogDev('CHR', 'info', 'Get the required pair protocol...')

        protocol = c_int(0)
        rc = self.dll.CHR_pair_get_protocol(pair, byref(protocol))
        if (rc != CHR_OK):
            self.ConvertErrorInfo(pair, rc, "pair_get_protocol")
        #
        #print protocol.value
        return protocol.value

    #####################################################
    ### 获取Pair的脚本
    def GetPairScript(self, pair):
        print u'获取Pair的脚本'
        self.logger.LogDev('CHR', 'info', 'Get the required pair script filename...')

        scriptName = create_string_buffer("\0", CHR_MAX_FILENAME)
        scriptName_len = c_long(0)
        rc = self.dll.CHR_pair_get_script_filename(pair, scriptName, 
                                           CHR_MAX_FILENAME, byref(scriptName_len)) 
        if (rc != CHR_OK):
            self.ConvertErrorInfo(pair, rc, "pair_get_script_filename")
        #
        #print scriptName.value
        return scriptName.value

    #####################################################
    ### 获取Pair的应用程序脚本
    def GetPairApplScript(self, pair):
        print u'获取Pair的应用程序脚本'
        self.logger.LogDev('CHR', 'info', 'Get the required pair application script name...')

        applScriptName = create_string_buffer("\0", CHR_MAX_APPL_SCRIPT_NAME)
        applScriptName_len = c_long(0)
        rc = self.dll.CHR_pair_get_appl_script_name(pair, applScriptName, 
                                           CHR_MAX_APPL_SCRIPT_NAME, 
                                           byref(applScriptName_len))
        if (rc != CHR_OK):
            self.ConvertErrorInfo(pair, rc, "pair_get_appl_script_name") 
        #
        #print applScriptName.value
        return applScriptName.value

    #####################################################
    ### 获取Pair的注释
    def GetPairComment(self, pair, len_buf):
        print u'获取Pair的注释'
        self.logger.LogDev('CHR', 'info', 'Set the required pair comment...')

        buf = create_string_buffer("\0", CHR_MAX_PAIR_COMMENT)
        retLen = c_int(0)
        rc = self.dll.CHR_pair_get_comment(pair, buf, len_buf, byref(retLen))
        if rc != CHR_OK:
            self.ConvertErrorInfo(pair, rc, "pair_get_comment")
        #
        return buf.value

    #####################################################
    ### 获取Pair的时间记录序列
    def GetPairTimRecordCnt(self, pair):
        print u'获取Pair的时间记录序列'
        self.logger.LogDev('CHR', 'info', 'Get the required pair number of timing records...')

        timingRecCount = c_long(0)
        rc = self.dll.CHR_pair_get_timing_record_count(pair, byref(timingRecCount))
        if (rc != CHR_OK):
            self.ConvertErrorInfo(pair, rc, "pair_get_timing_record_count")
        #
        return timingRecCount.value

    #####################################################
    ### 获取Pair的时间记录
    def GetPairTimRecord(self, pair, num):
        print u'获取Pair的时间记录数'
        self.logger.LogDev('CHR', 'info', 'Get the required pair number of timing records...')

        timing_rec_handle = c_long(0)
        rc = self.dll.CHR_pair_get_timing_record(pair, num, byref(timing_rec_handle))
        if (rc != CHR_OK):
            self.ConvertErrorInfo(pair, rc, "pair_get_timing_record")
        #
        return timing_rec_handle.value

    #####################################################
    ### 获取Pair的elapsed时间
    def GetPairTimElapsed(self, handle):
        print u'获取Pair的时间记录数'
        self.logger.LogDev('CHR', 'info', 'Get the required pair number of timing records...')

        time_elapsed = c_double(0.0)
        rc = self.dll.CHR_timingrec_get_elapsed(handle, byref(time_elapsed))
        if (rc != CHR_OK):
            self.ConvertErrorInfo(pair, rc, "timingrec_get_elapsed")
        #
        return time_elapsed.value

    #####################################################
    ### 获取Pair的endpoit1接收的字节数
    def GetPairBytesRecvE1(self, pair):
        print u'获取Pair的endpoit1接收的字节数'
        self.logger.LogDev('CHR', 'info', 'Get the number of bytes received by Endpoint 1 from the test results...')

        recv_bytes = c_double(0.0)
        rc = self.dll.CHR_common_results_get_bytes_recv_e1(pair, byref(recv_bytes))
        if (rc != CHR_OK):
            self.ConvertErrorInfo(pair, rc, "common_results_get_bytes_recv_e1")
        #
        return recv_bytes.value

    #####################################################
    ### 获取Pair的endpoit1发送的字节数
    def GetPairBytesSentE1(self, pair):
        print u'获取Pair的endpoit1发送的字节数'
        self.logger.LogDev('CHR', 'info', 'Get the number of bytes sent by Endpoint 1 from the test results...')

        sent_bytes = c_double(0.0)
        rc = self.dll.CHR_common_results_get_bytes_sent_e1(pair, byref(sent_bytes))
        if (rc != CHR_OK):
            self.ConvertErrorInfo(pair, rc, "common_results_get_bytes_sent_e1")
        #
        return sent_bytes.value

    #####################################################
    ### 获取Pair的endpoit2接收的字节数
    def GetPairBytesRecvE2(self, pair):
        print u'获取Pair的endpoit2接收的字节数'
        self.logger.LogDev('CHR', 'info', 'Get the number of bytes received by Endpoint 2 from the test results...')

        recv_bytes = c_double(0.0)
        rc = self.dll.CHR_common_results_get_bytes_recv_e2(pair, byref(recv_bytes))
        if (rc != CHR_OK):
            self.ConvertErrorInfo(pair, rc, "common_results_get_bytes_recv_e2")
        #
        return recv_bytes.value

    #####################################################
    ### 获取Pair平均结果
    def GetPairRes_Avg(self, pair, res_type):
        print u'获取Pair平均结果'
        self.logger.LogDev('CHR', 'info', 'Get the average results...')

        res_avg = c_double(0.0)
        rc = self.dll.CHR_pair_results_get_average(pair, res_type, byref(res_avg))
        if (rc != CHR_OK):
            self.ConvertErrorInfo(pair, rc, "pair_results_get_average")

        #
        res_avg = '%.3f'%res_avg.value
        #print 'avg = ' + res_avg
        return res_avg

    #####################################################
    ### 获取Pair最小结果
    def GetPairRes_Min(self, pair, res_type):
        print u'获取Pair最小结果'
        self.logger.LogDev('CHR', 'info', 'Get the minimum results...')

        res_min = c_double(0.0)
        rc = self.dll.CHR_pair_results_get_minimum(pair, res_type, byref(res_min)) 
        if (rc != CHR_OK):
            self.ConvertErrorInfo(pair, rc, "pair_results_get_minimum")

        #
        res_min = '%.3f'%res_min.value
        #print 'min = ' + res_min
        return res_min

    #####################################################
    ### 获取Pair最大结果
    def GetPairRes_Max(self, pair, res_type):
        print u'获取Pair最小结果'
        self.logger.LogDev('CHR', 'info', 'Get the maximum results...')
        
        res_max = c_double(0.0)
        rc = self.dll.CHR_pair_results_get_maximum(pair, res_type, byref(res_max)) 
        if (rc != CHR_OK):
            self.ConvertErrorInfo(pair, rc, "pair_results_get_maximum"); 
        #
        res_max = '%.3f'%res_max.value
        #print 'max = ' + res_max
        return res_max 

    #####################################################
    ### 删除Pair
    def DelPair(self, pair):
        print u'删除Pair'
        self.logger.LogDev('CHR', 'info', 'Delete the special pair...')

        if pair != CHR_NULL_HANDLE:
            self.dll.CHR_pair_delete(pair)

    #####################################################
    ### 删除Test
    def DelTest(self, test):
        print u'删除Test'
        self.logger.LogDev('CHR', 'info', 'Delete the special test...')

        if test != CHR_NULL_HANDLE:
            self.dll.CHR_test_delete(test)

    #####################################################
    ### 退出Test
    def ExitTest(self, rc):
        print u'退出Test'
        self.logger.LogDev('CHR', 'info', 'Exit the test...')

        ###
        sys.exit(rc)

    #####################################################
    ### 重置Test
    def ResetTest(self, rc):
        print u'重置Test'
        self.logger.LogDev('CHR', 'info', 'Reset the test...')

        ###
        self.pairs = []

    #####################################################
    ### 获取Pairs
    def GetPairs(self):
        print u'获取Pairs'
        self.logger.LogDev('CHR', 'info', 'Get the pairs...')

        ###
        return self.pairs

    #####################################################
    ### 检查错误
    def CheckError(self):
        # 检查是否存在timeout测试
        print 'Check the error log'
        f = open('error.log', 'r')
        lines = f.readlines()
        for line in lines:
            if 'attempt timed out' in line:
                print 'The test timed out'
                break
        #
        f.close()

##################################################################
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
        if time_elapsed > time_elapsed_max:
            time_elapsed_max = time_elapsed
        #
        cur_ip = lib.GetPairAddr_e1(pair)
        comment = lib.GetPairComment(pair, CHR_MAX_PAIR_COMMENT)
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

