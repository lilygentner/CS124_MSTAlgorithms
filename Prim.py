import Graph
import minPQ
from sets import Set

def prim(G):

	#initialize empty priority queue
	H = minPQ.minPQ([])
	#initialize empty dictionary for dist and prev
	dist = {}
	prev = {}

	for v in G.vertices:
		dist[v] = 99999
		prev[v] = None

	S = Set([])
	start = G.vertices[0]
	dist[start] = 0
	H.insert((start, dist[start]))

	print len(H.Heap)
	while len(H.Heap) > 0:
		v = H.deletemin()
		print v
		S.add(v)
		for w in G.neighbors(v):
			if dist[w] > G.length(v, w):
				dist[w] = G.length(v, w)
				H.insert((w, dist[w]))

	return S

G = Graph.nGraph(10)	
print G.vertices

print prim(G)
