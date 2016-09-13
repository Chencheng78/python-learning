#插入排序和选择排序
def ins_sort_rec(seq,i):
	if i ==0: return
	ins_sort_rec(seq,i-1)
	j=i
	while j > 0 and seq[j-1] > seq[j]:
		seq[j-1],seq[j] = seq[j],seq[j-1]
		j -= 1
	return seq

def ins_sort(seq):
	for i in range(1,len(seq)):
		j = i
		while j > 0 and seq[j-1] > seq[j]:
			seq[j-1],seq[j] = seq[j],seq[j-1]
			j -= 1
	return seq
a = [2,6,5,1,3,4,8,7]


print((ins_sort(a)))
print(ins_sort_rec(a,len(a)-1))
