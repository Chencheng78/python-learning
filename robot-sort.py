def swapsort(sequence):
	seq = list(sequence)
	count = []
	while seq != sorted(seq):
		for i in range(0,len(seq)-1):
			a,b = seq[i],seq[i+1]
			if a > b :
				seq[i],seq[i+1] = b,a
				count.append(str(i) + str(i+1))
	return ','.join(count)

print(swapsort((6, 4, 2)))
print(swapsort((1,2,3,4,5)))
print(swapsort((1, 2, 3, 5, 3)))