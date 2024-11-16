import networkx as nx
import matplotlib.pyplot as plt
from data import create_graph

graph = create_graph()
start_node = 1
visited = set()
path = {}
steps = []

pos = nx.spring_layout(graph)

# Initialize the figure
fig, ax = plt.subplots()
nx.draw(graph, pos, with_labels=True, ax=ax)
labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

distances = {node: float('inf') for node in graph.nodes}
distances[start_node] = 0

