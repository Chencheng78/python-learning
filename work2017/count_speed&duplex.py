import re
import sys

fp = open(sys.argv[1], 'r')
total = 0
speed_100 = 0
speed_1000 = 0

for i in fp.readlines():
	fe = re.search(r'Link is Up - (100)/Full', i)
	ge = re.search(r'Link is Up - (1000)/Full', i)
	if fe and fe.group(1) == '100':
		speed_100 += 1
		total += 1
	elif ge and ge.group(1) == '1000':
		speed_1000 += 1
		total += 1
	else: pass
print 'total: %s; 100: %s; 1000: %s' % (total, speed_100, speed_1000)
fp.close()
