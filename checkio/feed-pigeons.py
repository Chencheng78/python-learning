def checkio(portions):
	time = 1
	while portions > 0:
		food = time * (time+1) / 2
		portions -= food
		time +=1
	print(food)
	print(portions)
	time = time -1
	print(time)
	if abs(portions) > time:
		print('r1')
		return time * (time-1) / 2
	elif portions == 0:
		print('r2')
		return time * (time+1) / 2
	else:
		print('r3')
		return time * (time+1) / 2 +portions



print(checkio(27))
