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

# Implementasi BFS (Breadth-First Search)
def bfs(graph, start, goal):
    # Menggunakan queue untuk FIFO
    queue = [(start, [start])]  # (node, path)
    visited = set()
    
    while queue:
        (node, path) = queue.pop(0)
        
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            
            for neighbor in graph.get_neighbors(node):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path))
    
    return None

# Implementasi DFS (Depth-First Search)
def dfs(graph, start, goal):
    # Menggunakan stack untuk LIFO
    stack = [(start, [start])]  # (node, path)
    visited = set()
    
    while stack:
        (node, path) = stack.pop()
        
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            
            for neighbor in graph.get_neighbors(node):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    stack.append((neighbor, new_path))
    
    return None

# Implementasi DFS dengan kedalaman iteratif
def iterative_deepening_dfs(graph, start, goal, max_depth=10):
    for depth in range(1, max_depth + 1):
        result = depth_limited_search(graph, start, goal, depth)
        if result:
            return result
    return None

def depth_limited_search(graph, start, goal, depth_limit):
    def dls_recursive(node, goal, depth, path):
        if node == goal:
            return path
        
        if depth <= 0:
            return None
        
        for neighbor in graph.get_neighbors(node):
            if neighbor not in path:  # Avoid cycles
                result = dls_recursive(neighbor, goal, depth - 1, path + [neighbor])
                if result:
                    return result
        
        return None
    
    return dls_recursive(start, goal, depth_limit, [start])

# Implementasi pencarian dua arah (Bidirectional Search) yang diperbaiki
def bidirectional_search(graph, start, goal):
    # Forward search dari start
    forward_queue = [(start, [start])]
    forward_visited = {start: [start]}
    
    # Backward search dari goal
    backward_queue = [(goal, [goal])]
    backward_visited = {goal: [goal]}
    
    while forward_queue and backward_queue:
        # Lakukan satu langkah pencarian dari arah forward
        current, path = forward_queue.pop(0)
        
        for neighbor in graph.get_neighbors(current):
            if neighbor in backward_visited:
                # Ketemu titik pertemuan
                forward_path = path + [neighbor]
                backward_path = backward_visited[neighbor]
                
                # Gabungkan jalur (hapus duplikasi pada titik pertemuan)
                complete_path = forward_path[:-1] + backward_path[::-1]
                return complete_path
            
            if neighbor not in forward_visited:
                new_path = path + [neighbor]
                forward_queue.append((neighbor, new_path))
                forward_visited[neighbor] = new_path
        
        # Lakukan satu langkah pencarian dari arah backward
        current, path = backward_queue.pop(0)
        
        for neighbor in graph.get_neighbors(current):
            if neighbor in forward_visited:
                # Ketemu titik pertemuan
                backward_path = path + [neighbor]
                forward_path = forward_visited[neighbor]
                
                # Gabungkan jalur (hapus duplikasi pada titik pertemuan)
                complete_path = forward_path + backward_path[::-1][1:]
                return complete_path
            
            if neighbor not in backward_visited:
                new_path = path + [neighbor]
                backward_queue.append((neighbor, new_path))
                backward_visited[neighbor] = new_path
    
    # Jika tidak menemukan jalur, kembalikan list kosong bukan None
    return []

# Fungsi untuk menghitung bobot jalur
def calculate_path_cost(graph, path):
    # Handle kasus ketika path adalah None atau list kosong
    if not path:
        return float('inf')
        
    total_cost = 0
    for i in range(len(path) - 1):
        total_cost += graph.get_weight(path[i], path[i+1])
    return total_cost

# Fungsi utama
def main():
    # Inisialisasi graf
    g = Graph()
    
    # Menambahkan edge sesuai grafik pada gambar
    g.add_edge('S', 'A', 3)
    g.add_edge('S', 'C', 2)
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'D', 5)
    g.add_edge('B', 'G', 7)
    g.add_edge('C', 'D', 6)
    g.add_edge('C', 'B', 3)
    g.add_edge('D', 'G', 1)
    
    # Cari jalur dengan berbagai metode
    bfs_path = bfs(g, 'S', 'G')
    dfs_path = dfs(g, 'S', 'G')
    id_dfs_path = iterative_deepening_dfs(g, 'S', 'G')
    bd_path = bidirectional_search(g, 'S', 'G')
    
    # Tambahkan pengecekan untuk setiap hasil pencarian
    bfs_path = bfs_path if bfs_path else []
    dfs_path = dfs_path if dfs_path else []
    id_dfs_path = id_dfs_path if id_dfs_path else []
    # bd_path sudah dihandle di fungsinya untuk mengembalikan list kosong
    
    # Hitung biaya untuk setiap jalur
    print("===== Hasil Pencarian Jalur =====")
    
    print("\n1. BFS (Breadth-First Search):")
    if bfs_path:
        print(f"   Jalur: {' → '.join(bfs_path)}")
        print(f"   Total bobot: {calculate_path_cost(g, bfs_path)}")
    else:
        print("   Tidak menemukan jalur")
    
    print("\n2. DFS (Depth-First Search):")
    if dfs_path:
        print(f"   Jalur: {' → '.join(dfs_path)}")
        print(f"   Total bobot: {calculate_path_cost(g, dfs_path)}")
    else:
        print("   Tidak menemukan jalur")
    
    print("\n3. DFS dengan Kedalaman Iteratif:")
    if id_dfs_path:
        print(f"   Jalur: {' → '.join(id_dfs_path)}")
        print(f"   Total bobot: {calculate_path_cost(g, id_dfs_path)}")
    else:
        print("   Tidak menemukan jalur")
    
    print("\n4. Pencarian Dua Arah:")
    if bd_path:
        print(f"   Jalur: {' → '.join(bd_path)}")
        print(f"   Total bobot: {calculate_path_cost(g, bd_path)}")
    else:
        print("   Tidak menemukan jalur")
    
    # Visualisasi Tree untuk BFS
    print("\n===== Pohon Pencarian BFS =====")
    visualize_bfs_tree(g, 'S', 'G')
    
    # Visualisasi Tree untuk DFS
    print("\n===== Pohon Pencarian DFS =====")
    visualize_dfs_tree(g, 'S', 'G')
    
    # Visualisasi Tree untuk DFS dengan Kedalaman Iteratif
    print("\n===== Pohon Pencarian DFS dengan Kedalaman Iteratif =====")
    visualize_id_dfs_tree(g, 'S', 'G')
    
    # Mencari jalur Tercepat (minimum cost)
    paths = []
    costs = []
    
    # Hanya tambahkan jalur valid ke dalam pertimbangan
    if bfs_path:
        paths.append(bfs_path)
        costs.append(calculate_path_cost(g, bfs_path))
    if dfs_path:
        paths.append(dfs_path)
        costs.append(calculate_path_cost(g, dfs_path))
    if id_dfs_path:
        paths.append(id_dfs_path)
        costs.append(calculate_path_cost(g, id_dfs_path))
    if bd_path:
        paths.append(bd_path)
        costs.append(calculate_path_cost(g, bd_path))
    
    # Pastikan ada jalur yang ditemukan sebelum mencari minimum
    if paths:
        min_cost = min(costs)
        min_index = costs.index(min_cost)
        
        print("\n===== Jalur Tercepat =====")
        print(f"Algoritma: {['BFS', 'DFS', 'DFS dengan Kedalaman Iteratif', 'Pencarian Dua Arah'][min_index % 4]}")
        print(f"Jalur: {' → '.join(paths[min_index])}")
        print(f"Total bobot: {min_cost}")
    else:
        print("\n===== Tidak Ada Jalur yang Ditemukan =====")

# Fungsi untuk visualisasi pohon BFS
def visualize_bfs_tree(graph, start, goal):
    queue = [(start, None)]  # (node, parent)
    visited = set([start])
    tree = {}
    
    while queue:
        node, parent = queue.pop(0)
        
        if parent is not None:
            if parent not in tree:
                tree[parent] = []
            tree[parent].append(node)
        
        for neighbor in graph.get_neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, node))
    
    # Print tree
    print_tree(tree, start, "", True)

# Fungsi untuk visualisasi pohon DFS
def visualize_dfs_tree(graph, start, goal):
    stack = [(start, None)]  # (node, parent)
    visited = set()
    tree = {}
    
    while stack:
        node, parent = stack.pop()
        
        if node not in visited:
            visited.add(node)
            
            if parent is not None:
                if parent not in tree:
                    tree[parent] = []
                tree[parent].append(node)
            
            # Tambahkan neighbor dalam urutan terbalik agar DFS bekerja seperti yang diharapkan
            neighbors = graph.get_neighbors(node)
            for neighbor in reversed(neighbors):
                if neighbor not in visited:
                    stack.append((neighbor, node))
    
    # Print tree
    print_tree(tree, start, "", True)

# Fungsi untuk visualisasi pohon DFS dengan Kedalaman Iteratif
def visualize_id_dfs_tree(graph, start, goal, max_depth=4):
    print(f"Tree untuk kedalaman maksimum {max_depth}:")
    
    for depth in range(1, max_depth + 1):
        print(f"\nKedalaman {depth}:")
        tree = {}
        depth_limited_tree(graph, start, depth, tree)
        print_tree(tree, start, "", True)

def depth_limited_tree(graph, node, depth, tree, parent=None, visited=None):
    if visited is None:
        visited = set()
    
    if parent is not None:
        if parent not in tree:
            tree[parent] = []
        tree[parent].append(node)
    
    if depth <= 0 or node in visited:
        return
    
    visited.add(node)
    
    for neighbor in graph.get_neighbors(node):
        if neighbor not in visited:
            depth_limited_tree(graph, neighbor, depth - 1, tree, node, visited.copy())

# Fungsi utility untuk mencetak pohon
def print_tree(tree, node, indent, last):
    # Print the current node
    branch = "└── " if last else "├── "
    print(indent + branch + node)
    
    # Print the children
    if node in tree:
        children = tree[node]
        count = len(children)
        
        for i, child in enumerate(children):
            is_last = i == count - 1
            new_indent = indent + ("    " if last else "│   ")
            print_tree(tree, child, new_indent, is_last)

if __name__ == "__main__":
    main()