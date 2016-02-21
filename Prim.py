import Graph
import minPQ
import numpy as np
from sets import Set

def prim(G):

	#initialize empty priority queue
	H = minPQ.minPQ([])
	#initialize empty dictionary for dist and prev
	dist = {}
	prev = {}

	n = len(G.vertices)
	for v in G.vertices:
		dist[v] = 99999
		prev[v] = None

	S = Set([])
	start = G.vertices[0]
	dist[start] = 0
	H.insert((start, dist[start]))

	#print H.Heap
	while (len(H.Heap) > 0) and (len(S) < n):
		v = H.deletemin()
		while v[0] in [s[0] for s in S]:
			v = H.deletemin()
		S.add(v)
		for w in G.neighbors(v[0]):
			if dist[w] > G.length(v[0], w):
				dist[w] = G.length(v[0], w)
				H.insert((w, dist[w]))
	return S


def tree_len (result):
	return sum([r[1] for r in result])


