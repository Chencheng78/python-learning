def checkio(num):
	for i in range(2,37):
		try:
			if int(num,i) % (i -1) == 0:
				return i
		except ValueError as e: pass
	return 0

print(checkio("18"))
print(checkio("1010101011"))
print(checkio("222"))
print(checkio("A23B"))
print(checkio("IDDQD"))