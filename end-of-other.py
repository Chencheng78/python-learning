def checkio(words):
	words = list(words)
	for i in words:
		for j in range(0,len(words)):
			if (i.find(words[j]) != -1 and (len(i)-len(words[j]) == i.find(words[j])) and i != words[j]):
				return True
	return False

print(checkio({"hello", "lo", "he"}))
print(checkio({"hello", "la", "hellow", "cow"}))
print(checkio({"walk", "duckwalk"}))
print(checkio({"one"}))
print(checkio({"helicopter", "li", "he"}))