'''
1. dropping any duplicate letters and digits in KEY
and then the remaining spaces are filled with the rest
of the letters and digits of the alphabet in order.

'''
import string
keyletters = "abcdefghijklmnopqrstuvwxyz0123456789"

def encode(text, key):
	key = ''.join(sorted(set(key),key = key.index))
	keytable = [list(key + ''.join([i for i in list(keyletters) if i not in key]))[i:i+6] for i in range(0,36,6)]
	print(keytable)

	text = [i for i in text.lower().replace(' ','') if i not in string.punctuation]
	print(text)
	for i in range(0,len(text),2):
		try:
			if text[i] == text[i+1] and text[i] == 'x':
				text.insert(i + 1,'z')
			elif text[i] == text[i+1]:
				text.insert(i + 1, 'x')
		except:pass
	if len(text) % 2 != 0 and text[-1] == 'z':
		text.append('x')
	elif len(text) % 2 != 0:
		text.append('z')
	text = [''.join(text[i:i+2]) for i in range(0,len(text),2)]
	print(text)

	output = ''
	for i in text:
		f_samerow = 0
		f_samecol = 0
		for j in keytable:
			if i[0] in j and i[1] in j:
				output += (j*2)[j.index(i[0])+1] + (j*2)[j.index(i[1])+1]
				f_samerow = 1

		for j in list(map(list,zip(*keytable))):
			if i[0] in j and i[1] in j:
				output += (j*2)[j.index(i[0]) + 1] + (j*2)[j.index(i[1])+1]
				f_samecol = 1
		if f_samerow == 0 and f_samecol == 0:
			for j in keytable:
				if i[0] in j:
					p1 = j.index(i[0])
					l1 = j
				elif i[1] in j:
					p2 = j.index(i[1])
					l2 = j
			output += l1[p2] + l2[p1]
	return output

def decode(secret, key):
	key = ''.join(sorted(set(key),key = key.index))
	keytable = [list(key + ''.join([i for i in list(keyletters) if i not in key]))[i:i+6] for i in range(0,36,6)]
	#print(keytable)

	secret =[secret[i:i+2] for i in range(0,len(secret),2)]

	output = ''
	for i in secret:
		f_samerow = 0
		f_samecol = 0
		for j in keytable:
			if i[0] in j and i[1] in j:
				output += (j*2)[j.index(i[0])+5] + (j*2)[j.index(i[1])+5]
				f_samerow = 1

		for j in list(map(list,zip(*keytable))):
			if i[0] in j and i[1] in j:
				output += (j*2)[j.index(i[0]) + 5] + (j*2)[j.index(i[1])+5]
				f_samecol = 1
		if f_samerow == 0 and f_samecol == 0:
			for j in keytable:
				if i[0] in j:
					p1 = j.index(i[0])
					l1 = j
				elif i[1] in j:
					p2 = j.index(i[1])
					l2 = j
			output += l1[p2] + l2[p1]
	return output

print(encode("How are you?", "hello"))
#print(decode("do2y7mt22kry94y2y2", "checkio101"))