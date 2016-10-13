'''
广度优先遍历（bfs）
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

from collections import deque
def bfs(G,s,f):
	P,Q = {s: None},deque([s])
	while Q:                # get the prent node from each node.
		u = Q.popleft()
		for v in G[u]:
			if v in P: continue
			P[v] = u
			Q.append(v)
	print(P)
	path = [f]
	while P[f] is not None:  #search the parent node from P until found the start point(None). Then reverse it.
		path.append(P[f])
		f = P[f]
	path.reverse()
	return path


print(bfs(G,0,6))
