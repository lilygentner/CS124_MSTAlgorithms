import math
import random

#find euclidian distance between two points
def eDistance(a, b):
    dimension = range(len(a))
    return math.sqrt(sum([(a[i] - b[i])**2 for i in dimension]))

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

class Graph: 
    def __init__(self, n):
        self.vectors = [range(n)]
        self.matrix = generateGraphMatrix(n)
        
    def length(self, a, b):
        return self.matrix[a][b]