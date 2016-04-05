
s = 0
n = 0

def checkio(num):
	global s
	global n
	if n < len(num):
		s += num[n]
		n += 1
		return checkio(num)
	else:
		s1 = s
		s = 0
		n = 0
		return s1




print(checkio(num))


