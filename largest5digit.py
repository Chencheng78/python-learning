'''
Complete the solution so that it returns the largest five digit number
found within the number given.. The number will be passed in as a string
of only digits. It should return a five digit integer. The number passed
may be as large as 1000 digits.
'''
def solution(digits):
	numbers = list(map(int,[digits[i:i+5] for i in range(len(digits)-4)]))
	#return int(''.join(sorted(list(digits),reverse=True))[0:5])
	return max(numbers)
number = "731671765313306249192251196744265747423"
print(solution(number))