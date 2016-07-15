'''
6 drones total
negative number means it doesn’t know about the original size of the pie
if remains is zero, return (0,1)
'''
from fractions import Fraction
def divide_pie(steps):
	total = sum(abs(i) for i in steps)
	print(total)
	remain = 1
	for i in steps:
		if i == total:
			return (0,1)
		else:
			if i > 0 :
				remain -= Fraction(i)/Fraction(total)
				#remain = Fraction(remain).limit_denominator()
			else:
				remain -= (Fraction(abs(i))/Fraction(total) * Fraction(remain))
				#remain = Fraction(remain).limit_denominator()
		#print(Fraction(remain))
	#print(Fraction(remain))
	return (remain.numerator,remain.denominator)

print(divide_pie([15,33,37,16,-1,22,-73,66,-59,10,-39,57]))
