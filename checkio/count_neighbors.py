t = ((1, 0, 0, 1, 0),
		(0, 1, 0, 0, 0),
        (0, 0, 1, 0, 1),
        (1, 0, 0, 0, 0),
        (0, 0, 1, 0, 0))

def count_neighbours(t,r,c):
 	l_row = len(t)
 	l_col = len(t[0])
 	if (r>= l_row or c >=l_col):
 		return ('error')
 	NEIGHBORS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
 	count = 0
 	list1 = []
 	for diff in NEIGHBORS:
 		n_row = r + diff[0]
 		n_col = c + diff[1]
 		if (0 <= n_col < l_col and 0 <= n_row < l_row) :

 			list1.append(t[n_row][n_col])
 	return sum(list1)


 	#if (r==0 and c == 0):
 	#	return sum([t[0][1],t[1][0],t[1][1]])
 	#if (r == (l-1) and c == (l-1) ):
 	#	return sum([t])


print(count_neighbours(t,1,2))
print(count_neighbours(t,0,0))
print(count_neighbours(t,5,5))
print(count_neighbours(t,0,4))
print(count_neighbours(t,0,2))
print(count_neighbours(t,4,4))
print(count_neighbours(t,4,2))