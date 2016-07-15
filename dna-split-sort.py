# import operator
def golf(dna,num):
	dna = [dna[i:i+num] for i in range(0,len(dna)-(len(dna) % num),num)]
	dna1 = list(map(list,dna))
	sequence = []
	for seq in dna1:
		count = 0
		while seq != sorted(seq):
			for i in range(0,len(seq)-1):
				a,b = seq[i],seq[i+1]
				if ord(a) > ord(b) :
					seq[i],seq[i+1] = b,a
					count +=1
		sequence.append(count)
	while sequence != sorted(sequence):
		for i in range(0,len(sequence)-1):
			a,b = sequence[i],sequence[i+1]
			c,d = dna[i],dna[i+1]
			if a > b:
				sequence[i],sequence[i+1] = b,a
				dna[i],dna[i+1] = d,c
	# d = dict(zip(dna,sequence))
	# print(d)
	# print(d.values())
	# print(sorted(d.values()))
	# a = sorted(d.items(),key=operator.itemgetter(1))
	return ''.join(dna)
print(golf("ACGGCATAACCCTCGA",3))