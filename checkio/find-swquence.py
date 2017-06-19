def checkio(seq):
	seq_t = list(map(list,zip(*seq)))
#Horizontal
	for i in seq:
		for j in range(len(i)):
			try:
				if i[j] == i[j+1] == i[j+2] == i[j+3]:
					return True
			except IndexError:
				continue
#Vertical
	for i in seq_t:
		for j in range(len(i)):
			try:
				if i[j] == i[j+1] == i[j+2] == i[j+3]:
					return True
			except IndexError:
				continue		
#Diagonal
	for i in range(len(seq)):
		for j in range(len(seq[i])):
			try:
				if seq[i][j] == seq[i+1][j+1] == seq[i+2][j+2] ==seq[i+3][j+3]:
					return True				
			except IndexError:
				pass
			try:
				if (seq[i][j] == seq[i+1][j-1] == seq[i+2][j-2] == seq[i+3][j-3]) and j>=3:
					return True
			except IndexError:
				continue
	return False

print(checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]))