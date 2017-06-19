def checkio(array):
	l = len(array)
	if l ==0 :
		return 0
	else:
		even = []
		for i in range(0,l):
			if i % 2 ==0:
				even.append(array[i])
		return sum(even) * array[l-1]

print(checkio([0, 1, 2, 3, 4, 5]))
print(checkio([1, 3, 5]))
print(checkio([5]))
print(checkio([]))