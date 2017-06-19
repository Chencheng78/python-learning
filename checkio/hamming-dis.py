def checkio(num1,num2):
	bin1 = bin(num1)[:1:-1]
	bin2 = bin(num2)[:1:-1]
	if len(bin1) > len(bin2):
		bin2 += '0'*(len(bin1) - len(bin2))
	else:
		bin1 += '0'*(len(bin2) - len(bin1))
	count = 0
	for i in range(len(bin1)):
		if bin1[i] != bin2[i]:
			count +=1

	return count