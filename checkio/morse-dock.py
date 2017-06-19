def checkio(time):
	#time = time.replace(':','')
	binary = []
	for i in time.split(':'):
		if len(i) == 1:
			binary.extend(['0',bin(int(i))[2:]])
		else:
			binary.extend([bin(int(i[0]))[2:],bin(int(i[1]))[2:]])

	if len(binary[0]) != 2:
		binary.insert(0,'0'*(2-len(binary[0])) + binary.pop(0))
	if len(binary[1]) != 4:
		binary.insert(1,'0'*(4-len(binary[1])) + binary.pop(1))
	if len(binary[2]) != 3:
		binary.insert(2,'0'*(3-len(binary[2])) + binary.pop(2))
	if len(binary[3]) != 4:
		binary.insert(3,'0'*(4-len(binary[3])) + binary.pop(3))
	if len(binary[4]) != 3:
		binary.insert(4,'0'*(3-len(binary[4])) + binary.pop(4))
	if len(binary[5]) != 4:
		binary.insert(5,'0'*(4-len(binary[5])) + binary.pop(5))

	binary = ': '.join([binary[0]+' '+ binary[1]+' ',binary[2]+' '+binary[3]+' ',binary[4]+' '+binary[5]+' '])
	return  binary.replace('0','.').replace('1','-')
print(checkio("1:7:9"))
