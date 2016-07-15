def clockwise_90(matrix):
	matrix.reverse()
	return list(map(list,zip(*matrix)))

def recall_password(grille,password):
	cipher_matrix = []
	for i in grille:
		cipher_matrix.append([j for j in i])
	pwd_matrix = []
	for i in password:
		pwd_matrix.append([j for j in i])
	i = 0
	output = ''
	while i < 4:
		for a in range(4):
			for b in range(4):
				if cipher_matrix[a][b] == 'X':
					output += pwd_matrix[a][b]
		cipher_matrix = clockwise_90(cipher_matrix)
		i +=1
	#print(clockwise_90(cipher_matrix))

	return output

print(recall_password(
 	('X...',
     '..X.',
     'X..X',
     '....'),
    ('itdf',
     'gdce',
     'aton',
     'qrdi')))