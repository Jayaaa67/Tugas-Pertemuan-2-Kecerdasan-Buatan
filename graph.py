# graph.py
class Graph:
    def __init__(self):
        self.graph = {}
        self.weights = {}
    
    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        
        self.graph[u].append(v)
        self.weights[(u, v)] = weight
    
    def get_neighbors(self, node):
        return self.graph.get(node, [])
    
    def get_weight(self, u, v):
        return self.weights.get((u, v), float('inf'))

# Fungsi untuk menghitung bobot jalur
def calculate_path_cost(graph, path):
    # Handle kasus ketika path adalah None atau list kosong
    if not path:
        return float('inf')
        
    total_cost = 0
    for i in range(len(path) - 1):
        total_cost += graph.get_weight(path[i], path[i+1])
    return total_cost