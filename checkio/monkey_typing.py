'''
def count_words(strings,words):
	s_lower = strings.lower()
	list1 = list(words)
	count = 0
	for i in list1:
		m = re.search(i,s_lower)
		if m != None:
			count+=1

	return count
'''
import re

def count_words(strings,words):
	s_lower = strings.lower()
	
	count = 0
	for i in words:
		if i in s_lower:
			count+=1

	return count

print(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}))
print(count_words("Bananas, give me bananas!!!", {"banana", "bananas"}))
print(count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",{"sum", "hamlet", "infinity", "anything"}))