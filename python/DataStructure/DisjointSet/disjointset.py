class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = {}
        self.parent = {}

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def find(self, i):
        if self.parent[i] != i:
            return self.find(self.parent, self.parent[i])
        return i

    def union(self, x, y):
        self.parent[x] = y