'''
遍历算法
'''

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

#无向图
G1 = [
	[1,2],
	[0,4],
	[0,5],
	[6],
	[1],
	[2,7],
	[3,7],
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

#带时间戳的DFS
def dfs(G,s,d,f,S = None,t=0):
	if S is None: S = set()
	d[s] = t; t+=1
	S.add(s)
	for u in G[s]:
		if u in S: continue
		t = dfs(G,u,d,f,S,t)
	f[s] = t; t+=1
	return t

d = [0,0,0,0,0,0,0]
f = [0,0,0,0,0,0,0]

print(list(iter_dfs(G1,0)))
print(rec_dfs(G1,0))
#print(dfs(G,0,d,f))