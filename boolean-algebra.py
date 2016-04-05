OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
	if operation == 'conjunction':
		return (x and y)
	elif operation == 'disjunction': 
		return(x or y)	
	elif operation == 'implication':
		if x ==1:
			return y
		else:
			return 1
	elif operation == 'exclusive': 
		if x == y :
			return 0
		else:
			return 1
	else:
		if x == y :
			return 1
		else:
			return 0

