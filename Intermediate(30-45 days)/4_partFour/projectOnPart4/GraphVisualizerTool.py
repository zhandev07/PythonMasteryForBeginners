import tkinter as tk
from tkinter import messagebox, filedialog
import networkx as nx
import matplotlib.pyplot as plt
import json

class GraphVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Visualizer")
        self.root.geometry("400x400")
        
        self.graph = nx.Graph()
        
        self.create_widgets()

    def create_widgets(self):
        # Input for vertex
        tk.Label(self.root, text="Vertex:").grid(row=0, column=0, padx=5, pady=5)
        self.vertex_entry = tk.Entry(self.root)
        self.vertex_entry.grid(row=0, column=1, padx=5, pady=5)

        # Input for edge
        tk.Label(self.root, text="Edge (format: A,B,weight):").grid(row=1, column=0, padx=5, pady=5)
        self.edge_entry = tk.Entry(self.root)
        self.edge_entry.grid(row=1, column=1, padx=5, pady=5)

        # Buttons
        tk.Button(self.root, text="Add Vertex", command=self.add_vertex).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(self.root, text="Add Edge", command=self.add_edge).grid(row=2, column=1, padx=5, pady=5)
        tk.Button(self.root, text="Show Graph", command=self.show_graph).grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        tk.Button(self.root, text="BFS Traversal", command=self.bfs_traversal).grid(row=4, column=0, padx=5, pady=5)
        tk.Button(self.root, text="DFS Traversal", command=self.dfs_traversal).grid(row=4, column=1, padx=5, pady=5)
        tk.Button(self.root, text="Dijkstra's Algorithm", command=self.dijkstra_path).grid(row=5, column=0, padx=5, pady=5)
        tk.Button(self.root, text="Kruskal's Algorithm", command=self.kruskal_mst).grid(row=5, column=1, padx=5, pady=5)
        tk.Button(self.root, text="Save Graph", command=self.save_graph).grid(row=6, column=0, padx=5, pady=5)
        tk.Button(self.root, text="Load Graph", command=self.load_graph).grid(row=6, column=1, padx=5, pady=5)

        # Search functionality
        tk.Label(self.root, text="Search Node:").grid(row=7, column=0, padx=5, pady=5)
        self.search_entry = tk.Entry(self.root)
        self.search_entry.grid(row=7, column=1, padx=5, pady=5)
        tk.Button(self.root, text="Search", command=self.search_node).grid(row=8, column=0, columnspan=2, padx=5, pady=5)

    def add_vertex(self):
        vertex = self.vertex_entry.get().strip()
        if vertex:
            self.graph.add_node(vertex)
            messagebox.showinfo("Success", f"Vertex '{vertex}' added.")
            self.vertex_entry.delete(0, tk.END)  # Clear entry field
        else:
            messagebox.showwarning("Input Error", "Please enter a vertex.")

    def add_edge(self):
        edge = self.edge_entry.get().strip()
        if edge and "," in edge:
            parts = edge.split(",")
            if len(parts) == 3:
                node1, node2, weight = parts
                try:
                    weight = float(weight)
                    if node1 in self.graph.nodes and node2 in self.graph.nodes:
                        self.graph.add_edge(node1, node2, weight=weight)
                        messagebox.showinfo("Success", f"Edge '{edge}' added.")
                        self.edge_entry.delete(0, tk.END)  # Clear entry field
                    else:
                        messagebox.showwarning("Input Error", "Both vertices must exist.")
                except ValueError:
                    messagebox.showwarning("Input Error", "Weight must be a number.")
            else:
                messagebox.showwarning("Input Error", "Please enter a valid edge (format: A,B,weight).")
        else:
            messagebox.showwarning("Input Error", "Please enter a valid edge.")

    def show_graph(self):
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(self.graph)
        weights = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=weights)
        plt.title("Graph Visualization")
        plt.show()

    def bfs_traversal(self):
        start_vertex = self.vertex_entry.get().strip()
        if start_vertex in self.graph.nodes:
            visited = []
            queue = [start_vertex]
            while queue:
                vertex = queue.pop(0)
                if vertex not in visited:
                    visited.append(vertex)
                    neighbors = list(self.graph.neighbors(vertex))
                    queue.extend([n for n in neighbors if n not in visited])
            self.highlight_nodes(visited)
            messagebox.showinfo("BFS Traversal", f"Traversal Order: {visited}")
        else:
            messagebox.showwarning("Input Error", "Start vertex must exist in the graph.")

    def dfs_traversal(self):
        start_vertex = self.vertex_entry.get().strip()
        if start_vertex in self.graph.nodes:
            visited = []
            self.dfs_recursive(start_vertex, visited)
            self.highlight_nodes(visited)
            messagebox.showinfo("DFS Traversal", f"Traversal Order: {visited}")
        else:
            messagebox.showwarning("Input Error", "Start vertex must exist in the graph.")

    def dfs_recursive(self, vertex, visited):
        visited.append(vertex)
        for neighbor in self.graph.neighbors(vertex):
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    def highlight_nodes(self, visited):
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(self.graph)
        node_colors = ['lightgreen' if node in visited else 'lightblue' for node in self.graph.nodes]
        nx.draw(self.graph, pos, with_labels=True, node_color=node_colors, node_size=2000, font_size=15)
        plt.title("Highlighted Traversal Visualization")
        plt.show()

    def dijkstra_path(self):
        start_vertex = self.vertex_entry.get().strip()
        if start_vertex in self.graph.nodes:
            lengths = nx.single_source_dijkstra_path_length(self.graph, start_vertex)
            path_info = ", ".join(f"{node}: {length}" for node, length in lengths.items())
            messagebox.showinfo("Dijkstra's Algorithm", f"Shortest paths from {start_vertex}:\n{path_info}")
        else:
            messagebox.showwarning("Input Error", "Start vertex must exist in the graph.")

    def kruskal_mst(self):
        mst_edges = list(nx.minimum_spanning_edges(self.graph, data=True))
        if mst_edges:
            edges_str = ', '.join(f"{u}-{v} (Weight: {data['weight']})" for u, v, data in mst_edges)
            messagebox.showinfo("Kruskal's Algorithm", f"Minimum Spanning Tree Edges:\n{edges_str}")
        else:
            messagebox.showwarning("No Edges", "Graph has no edges to form a minimum spanning tree.")

    def save_graph(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'w') as f:
                json.dump(nx.node_link_data(self.graph), f)
            messagebox.showinfo("Success", "Graph saved successfully.")

    def load_graph(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'r') as f:
                data = json.load(f)
                self.graph = nx.node_link_graph(data)
            messagebox.showinfo("Success", "Graph loaded successfully.")

    def search_node(self):
        search_vertex = self.search_entry.get().strip()
        if search_vertex in self.graph.nodes:
            messagebox.showinfo("Search Result", f"Node '{search_vertex}' found.")
        else:
            messagebox.showwarning("Search Result", f"Node '{search_vertex}' not found.")
        self.search_entry.delete(0, tk.END)  # Clear entry field

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphVisualizer(root)
    root.mainloop()
