'''
You are given a non-empty list of integers (X). 
For this task, you should return a list consisting of only the non-unique elements in this list. 
To do so you will need to remove all unique elements (elements which are contained in a given list only once). 
When solving this task, do not change the order of the list. 
Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3]. 
'''
a = [1,2,3,1,3]
b = [1,3,5]
c = [5,5,5,5,5]
d = [10,9,10,10,9,8]

'''wrong code when using remove in a Iterate loop
def checkio(list1):
	for each_i in list1:
		if list1.count(each_i) == 1 :
			list1.remove(each_i)
		print(list1)
	return(list1)
'''	
def checkio(list1):
	result = []
	for each_i in list1:
		if list1.count(each_i) != 1 :
			result.append(each_i)
		
	return(result)


print(checkio(a))
print(checkio(b))
print(checkio(c))
print(checkio(d))