def find_all_paths(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
		return [path]
	if start not in graph:
		return []
	paths = []
	for node in graph[start]:
		if node not in path:
			newpaths = find_all_paths(graph, node, end, path)
			for newpath in newpaths:
				paths.append(newpath)
	return paths
def capture(matrix):
	diagonal = [matrix[i][i] for i in range(len(matrix))]
	node = len(matrix)
	print(diagonal)
	matrix_t = list(map(list,zip(*matrix)))
	connections = {}
	for i in range(node):
		# for j in range(node):
		# 	if matrix[i][j] == matrix_t[i][j] == 1 and i != j:
		connections[i] = [j for j in range(node) if matrix[i][j] == matrix_t[i][j] == 1 and i != j]
	#fconnections = sorted(set([''.join(sorted(i)) for i in connections]))
	print(connections)
	for i in connections:
		for j in connections[i]:

		print(connections.values())
	print(find_all_paths(connections,0,5))
	infected_node = set()
	time = []
	#while len(infected_node) != node:
	# for i in connections:
	# 	time.append(diagonal[int(i[1])]-diagonal[int(i[0])])
	# 	infected_node.add(i[0])
	# 	infected_node.add(i[1])
	print(infected_node)
	print(time)

	return connections
print(capture([[0, 1, 0, 1, 0, 1],
			   [1, 8, 1, 0, 0, 0],
	           [0, 1, 2, 0, 0, 1],
    	       [1, 0, 0, 1, 1, 0],
        	   [0, 0, 0, 1, 3, 1],
         	   [1, 0, 1, 0, 1, 2]]))