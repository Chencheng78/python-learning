def pascals_triangle(n):
	x=[[1]]
	for i in range(n-1):
		print(x)
		print([0]+ x[-1])
		print(list(zip([0]+x[-1],x[-1]+[0])))
		x.append([sum(i) for i in zip([0]+x[-1],x[-1]+[0])])
	return x

print(pascals_triangle(6))