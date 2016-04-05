'''
num = []
val = []
for i in range(0,36):
	val.append(i)
	if i <= 9:
		num.append(str(i))
	else:
		num.append(chr(i+55))
num_dict = dict(zip(num,val))

#print(num_dict)
def checkio(number,radix):
	n = number[::-1]
	result = 0
	for i in range(0,len(n)):
		if num_dict[n[i]] >= radix:
			return -1
		else:
			result += num_dict[n[i]] *  (radix ** i)
	return result
'''
def checkio(number,radix):
	try:
		return int(number,radix)
	except ValueError:
		return -1
print(checkio("AF", 16))
print(checkio("101", 2))
print(checkio("101", 5))
print(checkio("Z", 36))
print(checkio("AB", 10))

#Don't forget the second args in int(). so this will be simple if use int(str,base = n)

# try:
# 	return int(number,radix)
# except ValueError:
# 	return -1