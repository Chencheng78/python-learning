def checkio(matrix):
	tranpose = list(map(list, zip(*matrix)))
	for i in range(len(matrix)):
		for j in range(len(matrix)):
			tranpose[i][j] = -1 * tranpose[i][j]
	if tranpose == matrix:
		return True
	else:
		return False

print(checkio([
    [ 0,  1,  2],
    [-1,  0,  1],
    [-2, -1,  0]]))