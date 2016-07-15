def checkio(num):
	roman = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
	arabic = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
	mul = []
	for i in arabic:
		a = num // i
		mul.append(a)
		num -= a*i
	output = ''
	for i in range(len(mul)):
		output += mul[i] * roman[i]
	return output

print(checkio(6))
print(checkio(76))
print(checkio(13))
print(checkio(44))
print(checkio(3999))
