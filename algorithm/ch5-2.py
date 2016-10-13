'''
基于DFS算法的
有向无环图(DAG)的拓扑排序
'''
N = {
	0:{1,3},
	1:{2},
	2:{},
	3:{2,4},
	4:{2}
}

def dfs_topsort(G):
	S,res = set(),[]
	def recurse(u):
		if u in S: return
		S.add(u)
		for v in G[u]:
			recurse(v)
		res.append(u)
	for u in G:
		recurse(u)
	res.reverse()
	return res

print(dfs_topsort(N))