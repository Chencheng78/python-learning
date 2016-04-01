'''
Define a function isPrime that takes one integer argument and returns true
or false depending on if the integer is a prime.
Per Wikipedia, a prime number (or a prime) is a natural number greater
than 1 that has no positive divisors other than 1 and itself.
'''

def is_prime(num):
	num = abs(num)
	if num <= 1:
		return False
	else:
		for i in range(2,num):
			if num % i == 0:
				return False
		return True

