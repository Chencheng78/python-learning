import telnetlib

ip = '192.168.2.1'
tn = telnetlib.Telnet(ip, timeout=5)

tn.read_until('K3C', timeout=5)
tn.write('iwconfig\n')
tn.write('exit\n')
#print tn.read_all()
