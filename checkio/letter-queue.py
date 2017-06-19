import re

def letter_queue(command):
	list1 = []
	l = len(command)
	for i in range(0,l):
		if re.search(r'PUSH',command[i]) != None:
			list1.append(list(command[i].split(' '))[1])
		elif re.search(r'POP',command[i]) != None and list1 != []:
			list1.pop(0)
	return ''.join(list1)

print(letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]))