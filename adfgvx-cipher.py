'''
encode('I am going.', 'dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g','cipher') == 'FXGAFVXXAXDDDXGA'
decode('FXGAFVXXAXDDDXGA', 'dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g','cipher') == 'iamgoing'

'''
from itertools import product
import string
def encode(message, secret_alphabet, keyword):
	ADFGVX = list(map(lambda x : ''.join(x),product('ADFGVX',repeat = 2)))
	secret = list(i for i in secret_alphabet)
	secret_dict = dict(zip(secret,ADFGVX))
	msg = list(i for i in message.lower().replace(' ',''))
	for i in msg:
		if i in string.punctuation:
			msg.remove(i)
	encrypted = ''.join(map(lambda x : secret_dict[x],msg))
	encoded = {}
	keyword = ''.join(sorted(set(keyword),key = keyword.index))
	for i in range(len(keyword)):
		j = i
		code = ''
		while j < len(encrypted):
			code += encrypted[j]
			j += len(keyword)
		encoded[keyword[i]] = code
		formed = list(map(list,sorted(encoded.items())))
		output = ''
		for i in range(len(formed)):
			output += formed[i][1]
	return output

def decode(message, secret_alphabet, keyword):
	ADFGVX = list(map(lambda x : ''.join(x),product('ADFGVX',repeat = 2)))
	secret = list(i for i in secret_alphabet)
	secret_dict = dict(zip(ADFGVX,secret))
	key = sorted(set(list(i for i in keyword)))
	keyword = ''.join(sorted(set(keyword),key = keyword.index))
	m = len(message) % len(keyword)
	n = len(message) // len(keyword)
	decoded = {}
	msg = list(i for i in message)
	for i in range(len(keyword)):
		if keyword.index(key[i]) >= m:
			code = ''
			for j in range(n):
				if len(msg) > 1:
					code += msg.pop(0)
				else:
					code += msg[0]
			decoded[key[i]] = code
		else:
			code = ''
			for j in range(n+1):
				if len(msg) > 1:
					code += msg.pop(0)
				else:
					code += msg[0]
			decoded[key[i]] = code
	#formed = sorted(decoded.items(),key=keyword.index)
	encrypted = []
	for i in keyword:
		encrypted.append(list(decoded[i]))
	code = ''
	try:
		for i in range(n+1):
			for j in encrypted:
				code += j[i]
	except: pass
	code = [code[i:i+2] for i in range(0,len(code),2)]
	output = ''
	for i in code:
		output += secret_dict[i]
	return output


print(encode('I am going.', 'dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g','cipher'))
print(decode('FXGAFVXXAXDDDXGA', 'dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g','cipher'))