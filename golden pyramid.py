def count_gold(pyramid):
	floors = len(pyramid)
	gold = [max(pyramid(floors))]
	find_max(pyramid[floors])
	# for i in range(0,floors):
	# 	sum1 = 0
	# 	sum2 = 0
	# 	sum1 += pyramid[i][i]
	# 	sum2 += pyramid[i][1]
	pass

def find_max(t):
	list1 = []
	for i in range(0,len(t)):
		if t[i] == max(t):
			list1.append(i)
	return list1
