import math
import random


#normal graph
class nGraph: 
    def __init__(self, n):
        self.vertices = range(n)
        self.matrix = self.generateGraphMatrix(n)

    def generateGraphMatrix(self, n):
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

    def neighbors(self, a):
        row = self.matrix[a]
        return [i for i in range(len(row)) if row[i] != 0]



#unit distance graph
class uGraph:
    def __init__(self, n, dimension):
        self.vertices = range(n)
        self.vLocation = self.generateUnitDistances(n, dimension)

    def generateUnitDistances(self, n, dimension): 
        vectorDict = {i: tuple(random.random() for _ in range(dimension)) for i in range(n)}
        return vectorDict

    def length(self, a, b):
        aL = self.vLocation[a]
        bL = self.vLocation[b]
        dimensions = range(len(aL))
        return math.sqrt(sum([(aL[i] - bL[i])**2 for i in dimensions]))

    def neighbors(self, a):
        return [x for x in self.vertices if x != a]






