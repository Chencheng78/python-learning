#Approach #1 Brute Force
def maxarea(height):
	m = 0
	for i in range(len(height)):
		for j in range(len(height)):
			sq = abs(i-j) * min (height[i],height[j])
			if sq > m: m = sq

	return m
	# if len(height)<=1: return 0
	# else:
	# 	l = max(height)
	# 	c = 0
	# 	for i in range(l):
	#
	# 	return m

print(maxarea([1,1]))
print(maxarea([1,2,3,4,5]))