def find_message(text):
	text = ' '.join(text)
	list1 = text.strip().split(' ')
	list2 = []
	for i in list1:
		if i.isupper() == True:
			list2.append(i)
	text2 = ''.join(list2)
	return text2

	

print(find_message("hello world!"))
print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))
