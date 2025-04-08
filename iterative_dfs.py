# iterative_dfs.py
from graph import Graph, calculate_path_cost

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