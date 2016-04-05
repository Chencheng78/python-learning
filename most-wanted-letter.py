import re

def checkio(text):
	text = text.lower()
	list1 = re.findall(r'[a-zA-Z]',text)
	set1 = set(list1)
	times = []
	for i in set1:
		times.append(list1.count(i))
	d = dict(zip(set1,times))
	d1 = sorted(d.items(),key = lambda x: (-x[1], x[0])) 
	
	return d1[0][0]

print(checkio("Hello Worldaaa!"))
