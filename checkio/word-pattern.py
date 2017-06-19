def check_command(num,pattern):
	num_bin = bin(num)[2:]
	pattern_bin = ''
	for i in pattern:
		if i.isdigit() == True:
			pattern_bin += '0'
		else:
			pattern_bin += '1'
	print(pattern_bin)
	num_bin = '0'*abs(len(pattern_bin) - len(num_bin)) + num_bin
	print(num_bin)
	if num_bin == pattern_bin:
		return True
	else:
		return False

print(check_command(42, "12a0b3e4"))
print(check_command(101, "ab23b4zz"))
