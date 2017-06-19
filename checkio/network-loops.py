def adjacency_dict(network):
	key=set([i[0] for i in network ]+[i[1] for i in network])
	dict = {k:[] for k in key}
	for i in network:
		dict[i[0]].append(i[1])
		dict[i[1]].append(i[0])

	return dict
'''
def iter_dfs(G,s):
	startpoint = s
	S,Q = set(),[]
	cycle =[]
	route = []
	Q.append(s)
	while Q:
		u = Q.pop()
		step+=1
		if u in S and u != startpoint: continue
		if u == startpoint and step>3:
			cycle.append(route+[startpoint])

		S.add(u)
		route.append(u)
		Q.extend(G[u])
		#yield u
	return cycle
'''
def cycle(network,start):
	route = []

	Q = [start]
	for i in Q:
		if

def find_cycle(network):
	network = adjacency_dict(network)
	#print(network)
	return cycle(network,1)

print(adjacency_dict(((1, 2), (2, 3), (3, 4), (4, 5), (5, 7),(7, 6), (8, 5), (8, 4), (8,1), (1, 5), (2, 4))))
print(find_cycle(((1, 2), (2, 3), (3, 4), (4, 5), (5, 7),(7, 6), (8, 5), (8, 4), (8,1), (1, 5), (2, 4))))
