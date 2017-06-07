import threading
import subprocess
import os
import re

a = subprocess.Popen('ping 192.168.2.1 -n 1', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
line=a.stdout.read()
print line.decode('gbk')
loss = re.search(u'(\()(.+)( 丢失\))', line.decode('gbk'))
print loss.group(2)
if loss.group != '100%':
	print 'fail'
else:
	print 'pass'
# for i in line:
# 	i = i.decode('utf8')
# 	print 'Line : ' + i
