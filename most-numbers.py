def checkio(*args):
	list1 = []
	for i in args:
		list1.append(*args)
		#print(i)
	if list1 != []:
		return (max(list1) - min(list1))
	else: 
		return 'Empty'

checkio(1,2,3,4)
	#
	#return (max(numbers) - min(numbers))
	#return list1
	