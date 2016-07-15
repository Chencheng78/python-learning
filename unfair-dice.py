from itertools import product
def winning_die(dice):
	sides = len(dice)
	my_dice = product(range(1,sum(dice) // sides + 2),repeat=sides)
	#print(list(my_dice))
	win = []
	for i in my_dice:
		if sum(dice) == sum(list(i)):
			big = 0
			small = 0
			compare = product(dice,i)
			for j in compare:
				if j[0] < j[1]:
					big +=1
				elif j[0] > j[1]:
					small += 1
			if big > small:
				win.append(list(i))
	if win ==[]:
		return []
	else:
		return win
print(winning_die([2,3,4]))
# print(winning_die([1, 2, 3, 4, 5, 6]))
print(winning_die([3, 3, 3, 3, 6, 6]))
# print(winning_die([2, 3, 4, 5, 6, 7]))
print(winning_die([2,2,5,5,5,5]))
