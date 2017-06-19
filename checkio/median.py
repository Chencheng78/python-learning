'''
 A median is a numerical value separating the upper half of a sorted array of numbers from the lower half.
 In a list where there are an odd number of entities, the median is the number found in the middle of the array. 
 If the array contains an even number of entities, then there is no single middle value, instead the median becomes the average of the two numbers found in the middle. 
 For this mission, you are given a non-empty array of natural numbers (X). 
 With it, you must separate the upper half of the numbers from the lower half and find the median.

Input: An array as a list of integers.

Output: The median as a float or an integer. 
'''

a = [1,2,3,4,5]
b = [3,1,2,5,3]
c = [1,300,2,200,1]
d = [3,6,20,99,10,15]

def checkio(data):
	l = len(data)
	sort = sorted(data)
	print(sort)
	if l % 2 == 0:
		result = ((sort[int(l / 2)] +  sort[int(l / 2 - 1)]) / 2)
	else:
		result = sort[int(l / 2 - 0.5)]
	return(result)

print(checkio(a))
print(checkio(b))
print(checkio(c))
print(checkio(d))
