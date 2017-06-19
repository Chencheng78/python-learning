# def order_n(number,side,target,i):
# 	count = 0
# 	n_max = pow(side, number)
# 	order = number
# 	#if target - i not in  range(1, side+1):
# 		#return 0
# 	if target - i in range(1, side+1) and order != 2:
# 		target -= i
# 		order -= 1
# 		print('when 1st = %i,target = %i'%(i,target))
# 		print('remain level = %i'%order)
# 		return order_n(order,side,target,i)
# 	else:
# 		for a in range(1,side+1):
# 			if target - a in range(1, side+1):
# 				count +=1
# 		#return round((pow(1/side,number-2) * (count / n_max)), 4)
# 		print('the probability is %f'%(count / 36))
# 		return (count / 36)
#
# def probability(number,side,target):
# 	n_max = pow(side, number)
# 	n_min = number * 1
# 	if target < number: return 0
# 	p = []
# 	for i in range(1,side+1):
# 		p.append(pow(1/side,number-2) * order_n(number,side,target,i))
# 		#print(order_n(number,side,target,i))
# 	return round(sum(p),4)
# 	#return p
from itertools import product

def probability(dice_number, sides, target):
    rollAmount = sides**dice_number
    targetAmount = 0
    for i in map(sum, product(range(1,sides+1), repeat=dice_number)):
        if i == target:
            targetAmount += 1
    odds = targetAmount / rollAmount
    return odds


print(probability(2, 6, 3))
print(probability(2, 6, 4))
print(probability(2, 6, 7))
print(probability(2, 3, 5))
print(probability(2, 3, 7))
print(probability(3, 6, 7))
#print(probability(10, 10, 50))


