def count_inversion(sequence):
	seq = list(sequence)
	count = 0
	while seq != sorted(seq):
		for i in range(0,len(seq)-1):
			a,b = seq[i],seq[i+1]
			if a > b :
				seq[i],seq[i+1] = b,a
				count +=1
	return count

print(count_inversion((1, 2, 5, 3, 4, 7, 6)))
print(count_inversion((5, 3, 2, 1, 0)))
