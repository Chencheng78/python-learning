

def tr(G):
	GT={}
	for u in G: GT[u] = set()
	for u in G:
		for v in G[u]:
			GT[v].add(u)
	return GT

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

def walk(G,s,S=set()):
	P,Q = dict(),set()
	P[s] = None
	Q.add(s)
	while Q:
		u = Q.pop()
		for v in G[u].difference(P,S):
			Q.add(v)
			P[v] = u
	return P

def scc(G):
	GT = tr(G)
	sccs, seen = [],set()
	for u in dfs_topsort(G):
		if u in seen: continue
		C = walk(GT,u,seen)
		seen.update(C)
		sccs.append(C)
	return sccs

N = {
	0:{1,3},
	1:{2},
	2:{},
	3:{2,4},
	4:{2}
}

N1 = {
	0:{1,2},
	1:{3,4},
	2:{3},
	3:{0,7},
	4:{5},
	5:{6},
	6:{4,7},
	7:{8},
	8:{7}
}

print(scc(N))
print(scc(N1))