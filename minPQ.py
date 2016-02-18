class minPQ:

	def __init__(self, items):
		self.Heap = self.buildHeap(items)

	def find_parent(self, i):
		n = i+1
		parent = n/2
		return parent-1

	def find_rchild(self, i):
		n = i+1
		rchild = 2*n + 1
		return rchild - 1

	def find_lchild(self, i):
		n = i+1
		lchild = 2*n
		return lchild - 1
		
	def deletemin(self):
		minimum = self.Heap[0]
		self.Heap[0] = self.Heap[len(self.Heap) - 1]
		self.Heap = self.Heap[:-1]
		self.minHeapify(0)
		return minimum

	def buildHeap(self, items):
		#len/2 down to 1
		A = len(items)
		for i in range(A/2):
			index = A/2 - (i + 1)
			items = self.minHeapifyBuild(index, items)
		return items

	def minHeapifyBuild(self, index, items):
		p_index = index
		l_index = self.find_lchild(index)
		r_index = self.find_rchild(index)

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
				self.minHeapifyBuild(l_index, items)

		elif min_value == r_value[1]:
			items[p_index] = r_value
			items[r_index] = p_value
			if r_index < len(items)/2:
				self.minHeapifyBuild(r_index, items)

		elif min_value == p_value[1]: 
			return items

		return items

	def minHeapify(self, index):
		p_index = index
		l_index = self.find_lchild(index)
		r_index = self.find_rchild(index)

		p_value = self.Heap[p_index]
		l_value = self.Heap[l_index]
		r_value = self.Heap[r_index]

		min_value = min([p_value[1], l_value[1], r_value[1]])

		if min_value == l_value:
			self.Heap[p_index] = l_value
			self.Heap[l_index] = p_value
			self.minHeapify(l_index)

		elif min_value == r_value:
			self.Heap[p_index] = r_value
			self.Heap[r_index] = p_value
			self.minHeapify(r_index)

		else: 
			return self.Heap

	def insert(self, item):
		item_index = len(self.Heap)
		parent_index = self.find_parent(item_index)
		try:
			parent_value = self.Heap[parent_index]
		except:
			self.Heap.append(item)
			return self.Heap
			
		self.Heap.append(item)

		while parent_value[1] > item[1]:
			self.Heap[parent_index] = item
			self.Heap[item_index] = parent_value

			item_index = parent_index
			parent_index = self.find_parent(parent_index)

			parent_value = self.Heap[parent_index]
			item_value = self.Heap[item_index]

		return self.Heap


#p = minPQ([(0, 10), (1, 3), (2, 4), (3, 1), (4, 9), (5,30), (6,3)])
#p.insert((9, 2))
#print p.Heap
#print p.deletemin()
