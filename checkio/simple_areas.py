from math import sqrt
def simple_areas(*args):
	if len(args) == 1:
		a = args[0]
		print(a)
		return round(3.14*pow(a/2,2),2)
	elif len(args) ==2:
		a,b = args
		return round(a*b,2)
	elif len(args) == 3:
		a,b,c = args
		p = (a+b+c)/2
		print(p)
		return round(sqrt(p*(p-a)*(p-b)*(p-c)),2)
	else:
		return 0



print(simple_areas(1.5,2))