
def decode_amsco(msg,key):
	l = []
	left = len(msg) % (1.5 * len(str(key)))
	print(len(msg))
	a =1
	while sum(l) < len(msg):
		if a % 2 != 0:
			for i in range(1,len(str(key))+1):
				if i % 2 != 0:
					l.append(1)
				else:
					l.append(2)
			a +=1
		else:
			for i in range(1,len(str(key))+1):
				if i % 2 != 0:
					l.append(2)
				else:
					l.append(1)
			a +=1
	print(l)
	while sum(l) > len(msg):
		l.pop()
	print(sum(l))
	if sum(l) != len(msg):
		l.append(1)
	if len(l) % len(str(key)) != 0:
		l.extend([0] * (len(str(key)) - len(l) % len(str(key))) )
	print(l)

	encode_matrix = [l[i:i+len(str(key))] for i in range(0,len(l),len(str(key)))]
	encode_matrix_t = list(map(list,zip(*encode_matrix)))
	print(encode_matrix)
	print(encode_matrix_t)
	decode_matrix = []
	for i in range(len(str(key))):
		decode_matrix.append(encode_matrix_t[[i for i in str(key)].index(str(i+1))])
	message = []
	count = 0
	for i in decode_matrix:
		l1 = []
		for j in i:
			l1.append(msg[count:count+j])
			count = count+j
		message.append(l1)
	print(message)
	message1 = []
	for i in range(len(str(key))):
		message1.append(message[int(str(key)[i])-1])
	print(message1)
	message2 = list(map(list,zip(*message1)))
	print(message2)
	output = ''
	for i in message2:
		output += ''.join(i)
	return output

print(decode_amsco("oruoreemdstmioitlpslam", 4123))
