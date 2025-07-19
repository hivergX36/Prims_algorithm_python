from collections import defaultdict
import re 

class Prim:

    def __init__(self):
        self.NbVertices = 0
        self.NbEdges = 0
        self.adjacency_list = {}
        self.adjacency_Matrix = []
        self.path = []
        self.cost = []
        
    
            
    def parse_graph(self,text):
        fichier = open(text, "r",encoding="utf8")
        lines = fichier.readlines()
        lines = [line.strip() for line in lines if line.strip() != " "]
        lines = [line.strip(",number of verticesedges''"": \n") for line in lines ]
        lines = [line.strip() for line in lines if line.strip() != "''"]
        lines = [[int(x) for x in lines[i].split(' ')] for i in range(len(lines)) if lines[i] != ""]
        self.NbVertices = lines[0][0]
        self.NbEdges = len(lines) - 1
        self.adjacency_list = defaultdict(list)
        self.adjacency_Matrix = [[0 for i in range(self.NbVertices)] for j in range(self.NbVertices)]
        for i in range(1, len(lines)):
            u, v, w = lines[i]
            self.adjacency_list[u].append((v, w))
            self.adjacency_Matrix[u][v] = w
    
    def display_graph(self):
        print("Number of vertices:", self.NbVertices)
        print("Number of edges:", self.NbEdges)
        print("Adjacency List:")
        for pred, succ in self.adjacency_list.items():
            print(f"{pred}: {succ[0]},{succ[1]}")
        print("Adjacency Matrix:")
        for row in self.adjacency_Matrix:
            print(row)
            
            
    def resolve(self, start_vertex):
        visited = [False] * self.NbVertices
        min_heap = [(0, start_vertex)]