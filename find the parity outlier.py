def find_outlier(integers):
	parity = [i % 2 for i in integers]
	if parity.count(1) == 1:
		return integers[parity.index(1)]
	else:
		return integers[parity.index(0)]

print((find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])))
print((find_outlier([160, 3, 1719, 19, 11, 13, -21])))