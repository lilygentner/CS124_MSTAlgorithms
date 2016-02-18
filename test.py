def find_parent(i):
	n = i+1
	parent = n/2
	return parent-1

def find_rchild(i):
	n = i+1
	rchild = 2*n + 1
	return rchild - 1

def find_lchild(i):
	n = i+1
	lchild = 2*n
	return lchild - 1

def buildHeap(items):
	#len/2 down to 1
	A = len(items)
	for i in range(A/2):
		index = A/2 - (i + 1)
		items = minHeapifyBuild(index, items)
	return items

def minHeapifyBuild(index, items):
	p_index = index
	l_index = find_lchild(index)
	r_index = find_rchild(index)

	p_value = items[p_index]
	try:
		l_value = items[l_index]
	except:
		l_value = (99999, 99999)
	
	try:
		r_value = items[r_index]
	except: 
		r_value = (99999, 99999)

	min_value = min([p_value[1], l_value[1], r_value[1]])

	if min_value == l_value[1]:
		items[p_index] = l_value
		items[l_index] = p_value
		if l_index < len(items)/2:
			minHeapifyBuild(l_index, items)

	elif min_value == r_value[1]:
		items[p_index] = r_value
		items[r_index] = p_value

		if r_index < len(items)/2:
			minHeapifyBuild(r_index, items)

	elif min_value == p_value[1]: 
		return items

	return items

items = [(0, 10), (1, 3), (2, 4), (3, 1), (4, 9), (5,30), (6,3), (7, 4)]
print buildHeap(items)