def checkio(list1):
	list2 = [list(list1[0]),list(list1[1]),list(list1[2])]
	neighbors =(
	((0,1),(0,2)),
	((0,-1),(0,-2)),
	((1,1),(2,2)),
	((-1,-1),(-2,-2)),
	((1,0),(2,0)),
	((-1,0),(-2,0)),
	((-1,1),(-2,2)),
	((1,-1),(2,-2)),
	((0,-1),(0,1)),
	((-1,0),(1,0)),
	((1,1),(-1,-1)),
	((-1,1),(1,-1))
		)

	dot = (
	(0,0),(0,1),(0,2),
	(1,0),(1,1),(1,2),
	(2,0),(2,1),(2,2),
		)

	for i in dot:
		for diff in neighbors:
 			n_row1 = i[0] + diff[0][0]
 			n_row2 = i[0] + diff[1][0]
 			n_col1 = i[1] + diff[0][1]
 			n_col2 = i[1] + diff[1][1]

 			if (3 > n_col1 >=0 and 3 > n_col2 >= 0 and 3 > n_row1 >= 0 and 3 > n_row2 >= 0):
 				if (list2[n_row1][n_col1] == list2[i[0]][i[1]] and list2[n_row2][n_col2] == list2[i[0]][i[1]] and list2[i[0]][i[1]] != '.'):
 					return list2[i[0]][i[1]]
	return 'D'


 	

print(checkio(["X.O","XX.","XOO"]))
print(checkio(["OO.","XOX","XOX"]))
print(checkio(["OOX","XXO","OXX"]))
print(checkio(["...","...","..."]))