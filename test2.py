# solution without dynamic programming
def back_tracking(n_steps):
	if n_steps < 1: return 0
	elif n_steps == 1: return 1
	elif n_steps == 2: return 2
	else:  return back_tracking(n_steps-1) + back_tracking(n_steps-2)

# solution with dynamic programming
def dynamic_programming(n_steps, method_values = None):
	if n_steps < 1: return 0
	elif n_steps == 1: return 1
	elif n_steps == 2: return 2
	else:
		# case where method_value list has not been initialized
		if(method_values == None):
			method_values = [-1] * n_steps

		# case when this method call has not been made
		if(method_values[n_steps-1] == -1):
			method_values[n_steps-1] = dynamic_programming(n_steps-1, method_values)
		if(method_values[n_steps-2] == -1):
			method_values[n_steps-2] = dynamic_programming(n_steps-2, method_values)

		return method_values[n_steps-1] + method_values[n_steps-2]

print(dynamic_programming(8))