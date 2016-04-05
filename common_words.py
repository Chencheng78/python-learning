def checkio(s1,s2):
	common=[]
	list_s1,list_s2 = s1.split(','),s2.split(',')
	for i in list_s1:
		if list_s2.count(i) != 0:
			common.append(i)
	return ','.join(sorted(common))
