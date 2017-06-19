'''
its length is greater than or equal to 10 symbols
it has at least one digit
containing at least one uppercase letter 
and one lowercase letter in it
'''


import re

s1 = 'A1213pokl'
s2 = 'bAse730onE'
s3 = 'asasasasasasasaas'
s4 = 'QWERTYqwerty'
s5 = '123456123456'
s6 = 'QwErTy911poqqqq'


def checkio(data):
	if len(data) < 10:
		return(False)
	a = 0
	b = 0
	c = 0
	for i in data:
		if re.match('[0-9]',i) != None:
			a+=1
		if re.match('[a-z]',i) != None:
			b+=1
		if re.match('[A-Z]',i) != None:
			c+=1
	if (a and b and c) == 0:
		return(False)
	else:
		return(True)
		'''
	if re.match('^[0-9a-zA-Z]+$',data):
		return(True)
	else:
		return(False)
	return(False)
	'''
print(checkio(s1))
print(checkio(s2))
print(checkio(s3))
print(checkio(s4))
print(checkio(s5))
print(checkio(s6))