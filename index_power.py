def index_power(l,i):
	if i > len(l)-1 :
		return -1
	else:
		return pow(l[i],i)		
print(index_power([1, 2, 3, 4], 2))
print(index_power([1, 3, 10, 100], 3))
print(index_power([0, 1], 0))
print(index_power([1, 2], 3))
print(index_power([1, 2], 2))