#-*- coding: utf-8 -*-

# 测试类型：RX/TX/TX_RX
test_type = 'TX'
#  网络类型：WAN/LAN
network_type = 'LAN'
# endpoint1的IP地址(注：网卡故障设置)
# e1_ip = ['192.168.2.110',
#         '192.168.2.120',
#         '192.168.2.130',
#         '192.168.2.140',
#         '192.168.2.150']
e1_ip = ['192.168.2.216']
# endpoint2的IP地址
e2_ip = '192.168.2.215'
# 超时时间（单位：s）
timeout = 5
# 最大超时时间（单位：s）
max_wait = 30
# 脚本运行时间（单位：s）
run_time = 10
# 网卡数量
num_cards = 1
# pair数量(注：num_pairs须是2*num_cards的整数倍)
num_pairs = 3
# 脚本文件名称
script_file = './Scripts/Throughput.scr'
# 结果文件名称
res_file = './Results/perf_test08012.tst'
# 发送文件类型
sendDataTypeName = 'send_datatype'
