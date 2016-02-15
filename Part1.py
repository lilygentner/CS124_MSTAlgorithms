import math
import random

#normal graph, part1
class Graph: 
    def __init__(self, n):
        self.vectors = [range(n)]
        self.matrix = generateGraphMatrix(n)

    def generateGraphMatrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = 0
            else:
                matrix[i][j] = random.random()
                matrix[j][i] = matrix[i][j]
    return matrix 

    def length(self, a, b):
        return self.matrix[a][b]


#unit distance graph
class unitDistanceGraph:
	def __init__(self, n, dimension):
		self.vectors = [range(n)]
		self.vectorLocationDict = generateUnitDistances(n, dimension)

	def generateUnitDistances(n, dimension): 
		vectorDict = {i: tuple(random.random() for _ in range(dimension)) for i in range(n)}
		return vectorDict

	def length(self, a, b):
		return eDistance(self.vectors[a], self.vectors[b])

	def eDistance(a, b):
    dimension = range(len(a))
    return math.sqrt(sum([(a[i] - b[i])**2 for i in dimension]))

def Prim(Graph):
	return True