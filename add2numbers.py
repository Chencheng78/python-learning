def addtwonumbers(l1,l2):
	s1=''
	s2=''
	while l1 != []:
		i=l1.pop()
		s1+=str(i)
	while l2 != []:
		i=l2.pop()
		s2+=str(i)
	res = int(s1)+int(s2)
	return list(reversed([int(i) for i in str(res)]))

print(addtwonumbers([2,4,3],[5,6,4]))