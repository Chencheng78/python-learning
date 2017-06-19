'''
"Fizz Buzz" if the number is divisible by 3 and by 5;
"Fizz" if the number is divisible by 3;
"Buzz" if the number is divisible by 5;
return the number if neither.
'''

def checkio(num):
	if (num % 3 == 0 and num % 5 == 0):
		return('Fizz Buzz')
	elif num % 3 ==0:
		return('Fizz')
	elif num % 5 ==0:
		return('Buzz')
	else:
		return(str(num))


print(checkio(15))
print(checkio(6))
print(checkio(5))
print(checkio(7))
print(checkio(20))
