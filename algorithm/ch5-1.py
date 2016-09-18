G = [
	[1,2,3,4,5],
	[2,4],
	[3],
	[4],
	[5],
	[2,6,7],
	[5,7],
	[5,6]
 ]

def iter_dfs(G,s):
	S,Q = set(),[]
	Q.append(s)
	while Q:
		u = Q.pop()
		if u in S: continue
		S.add(u)
		Q.extend(G[u])
		yield u

def rec_dfs(G,s,S=None):
	if S is None: S = set()
	S.add(s)
	for u in G[s]:
		if u in S : continue
		rec_dfs(G,u,S)

	return S

print(list(iter_dfs(G,0)))
print(rec_dfs(G,0))