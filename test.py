import minPQ

heap = minPQ.minPQ([(1,0.4), (2,0.5)])
print heap.Heap

print heap.insert((2, 0.2))
print heap.find_parent(0)
print heap.Heap[0]

try:
	x = heap.Heap[0]
except: 
	print "didn't work"