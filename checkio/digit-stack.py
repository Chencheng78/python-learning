def digit_stack(command):
	s = 0
	stack = []
	for i in command:
		if i.split(' ')[0] == 'PUSH':
			stack.append(i.split(' ')[1])
		elif i.split(' ')[0] == 'POP':
			try:
				s += int(stack.pop())
			except: pass
		else:
			try:
				s += int(stack[-1])
			except: pass
	return s

print(digit_stack(["PUSH 3", "POP", "POP", "PUSH 4",
				   "PEEK", "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]))
