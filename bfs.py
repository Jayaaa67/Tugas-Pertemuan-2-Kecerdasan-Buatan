# bfs.py
from graph import Graph, calculate_path_cost

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