# dfs.py
from graph import Graph, calculate_path_cost

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