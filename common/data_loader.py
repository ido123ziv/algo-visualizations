import pandas as pd
import networkx as nx
import json
import os


def load_graph_from_csv(file_path) -> nx.DiGraph:
    """Load graph data from a CSV file."""
    df = pd.read_csv(file_path)
    graph = nx.DiGraph()
    edges = [(row['start'], row['end'], row['weight']) for _, row in df.iterrows()]
    graph.add_weighted_edges_from(edges)
    return graph


def load_graph_from_json(file_path) -> nx.DiGraph:
    if not os.path.isfile(file_path):
        raise ValueError("File Doesn't Exists")
    with open(file_path, 'r') as graph_file:
        graph_data = json.load(graph_file)

    graph_edges = [tuple(x.values()) for x in graph_data]
    print(json.dumps(graph_edges))
    # Create a current_graph
    graph = nx.DiGraph()
    edges = graph_edges
    graph.add_weighted_edges_from(edges)
    return graph
