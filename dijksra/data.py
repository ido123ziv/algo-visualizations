import os
import networkx as nx
import json


def create_graph(name: str = "graph.json") -> nx.classes.digraph.DiGraph:
    if not os.path.isfile(name):
        raise ValueError("File Doesn't Exists")
    with open('graph.json', 'r') as graph_file:
        graph_data = json.load(graph_file)

    graph_edges = [tuple(x.values()) for x in graph_data]
    print(json.dumps(graph_edges))
    # Create a current_graph
    graph = nx.DiGraph()
    edges = graph_edges
    graph.add_weighted_edges_from(edges)
    return graph
