def longestjump(seq):
	l = 0
	for i in range(1,len(seq)):
		if seq[i]>=i and seq[i]>=l:
			l = i
	if len(seq) -1 == l: return []
	else:
		return seq[l:]

def jump(nums):
	seq = list(reversed(nums))

	count = 0
	while seq !=[]:
		count+=1
		seq = longestjump(seq)
	return count
print(jump([2,3,1,1,4]))
print(jump([2,1,1,1,1,1,4]))