def check_pangram(sentence):
	sentence.lower()
	count = 0
	for i in range(97,123):
		if sentence.find(chr(i)) != -1:
			count +=1
	if count == 26:
		return True
	else:
		return False

print(check_pangram("The quick brown fox jumps over the lazy dog."))
print(check_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

