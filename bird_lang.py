'''
rules:

- after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
- after each vowel letter the bird appends two of the same letter (a ⇒ aaa);
Vowels letters == "aeiouy".
'''
def translate(text):
	trans = ''
	for i in range(len(text)):
		try:
			if text[i-1] not in 'aeiouy' and text[i] in 'aeiouy' and text[i-1] != ' ':
				pass
			else:
				trans += text[i]
		except: pass
	for i in 'aeiouy':
		if i*3 in trans:
			trans = trans.replace(i*3,i)
	return trans

print(translate('hieeelalaooo'))
print(translate("hoooowe yyyooouuu duoooiiine"))
print(translate("aaa bo cy da eee fe"))
print(translate("sooooso aaaaaaaaa"))