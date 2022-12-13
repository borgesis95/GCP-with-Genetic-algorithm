

class Vertex:
    def __init__(self,vertex):
        self.num = vertex
        self.neighbors = []

    def getNeighbors(self):
        return self.neighbors

class Graph:
    def __init__(self):
        self.vertices  = []
        self.edges = []
        self.number_of_vertex = 0
        self.number_of_edges = 0

