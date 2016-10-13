'''
有向无环图(DAG)的拓扑排序
'''

N = {
	0:{1,3},
	1:{2},
	2:{},
	3:{2,4},
	4:{2}
}

def topsort(G):
	count = dict((u,0) for u in G)
	print(count)
	for u in G:
		for v in G[u]:
			count[v] += 1
	Q = [u for u in G if count[u] == 0]
	S = []
	while Q:
		u = Q.pop()
		S.append(u)
		for v in G[u]:
			count[v] -= 1
			if count[v] == 0:
				Q.append(v)
	return S
print(topsort(N))