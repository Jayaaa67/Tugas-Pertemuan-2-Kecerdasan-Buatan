# main.py
from graph import Graph, calculate_path_cost
from bfs import bfs, visualize_bfs_tree
from dfs import dfs, visualize_dfs_tree
from iterative_dfs import iterative_deepening_dfs, visualize_id_dfs_tree

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
    
    # Tambahkan pengecekan untuk setiap hasil pencarian
    bfs_path = bfs_path if bfs_path else []
    dfs_path = dfs_path if dfs_path else []
    id_dfs_path = id_dfs_path if id_dfs_path else []
    
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
    
    # Pastikan ada jalur yang ditemukan sebelum mencari minimum
    if paths:
        min_cost = min(costs)
        min_index = costs.index(min_cost)
        
        print("\n===== Jalur Tercepat =====")
        print(f"Algoritma: {['BFS', 'DFS', 'DFS dengan Kedalaman Iteratif'][min_index % 3]}")
        print(f"Jalur: {' → '.join(paths[min_index])}")
        print(f"Total bobot: {min_cost}")
    else:
        print("\n===== Tidak Ada Jalur yang Ditemukan =====")

if __name__ == "__main__":
    main()