

def iq_test(numbers):
	evenness = [int(i) % 2 for i in numbers.split(' ')]
	if evenness.count(0) == 1:
		return evenness.index(0) + 1
	else:
		return evenness.index(1) + 1

print(iq_test("2 4 7 8 10"))
print(iq_test("1 2 1 1"))