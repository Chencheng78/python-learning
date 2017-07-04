import telnetlib
import time



# tmp2 = tn.read_until('~ #', timeout=5)
# time.sleep(1)
# print tmp2
# print '~~~~~~~~~~~~~~~~~~~~'
#
# tn.write('iwconfig wlan1\n')
# time.sleep(10)
# tmp = tn.read_eager()
# print tmp
# print '~~~~~~~~~~~~~~~~~~~~'
# tn.write('exit\n')
# print tn.read_all()

ip = '192.168.2.1'
tn = telnetlib.Telnet(ip, timeout=5)

while 1:
    enter = raw_input('K3C#')
    if enter == 'exit':
        tn.close()
        break
    else:
        tn.read_until('~ #', timeout=5)
        tn.write(enter + '\n')
        time.sleep(2)
        #receive = tn.read_until('~ #')
        receive = tn.read_very_eager()
        print receive
