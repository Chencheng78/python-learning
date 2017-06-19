def checkio(words):
    list1 = []
    word = words.split(' ')
    count = 0
    for i in word:
    	if i.isalpha() == True:
    		count += 1
    	else:
    		count = 0
    if count >= 3:
    	return True
    else:
    	return False