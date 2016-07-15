# def gcd(*args):
# 	divisor = []
# 	for i in args:
# 		divisor_x = []
# 		for j in range(1,i+1):
# 			if i % j == 0:
# 				divisor_x.append(j)
# 		if divisor ==[]:
# 			divisor = divisor_x
# 		else:
# 			divisor = set(divisor) & set(divisor_x)
# 	return list(set(divisor))[-1]

def gcd(*args):
	m = sorted(list(args))[0]
	l = []
	for i in range(1,m+1):
		if m % i == 0:
				l.append(i)
	print(l)

	for i in args:
		divisor =[]
		for j in l:
			if i % j == 0:
				divisor.append(j)
		print(divisor)
		l = set(l) & set(divisor)
		print(l)

	return sorted(list(l))[-1]

print(gcd(
32,
256,
2048,
16384,
131072,
1048576,
8388608,
67108864,
536870912,
4294967296))
