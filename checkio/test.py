def div2(num,size=2):
	l = []
	for i in range(1,num //2 +1):
		l.append([i,num-i])
	if size != 2:
		size -=1
		for i in l:
			i[-1] = div2(i[-1],size)
	return l
#
# def flat(l):
# 	for i in l:
# 		if len(i)==1:

# l2.append(l[i][0])
# if type(l[i][1]) == list:
# 	flat(l[i][1])

print(div2(20))
print(div2(10,3))
print(div2(10,4))
