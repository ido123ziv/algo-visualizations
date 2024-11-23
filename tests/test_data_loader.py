import pytest  # noqa: F401
import networkx as nx
from common.data_loader import load_graph_from_csv, load_graph_from_json


def test_load_graph_from_csv():
    graph = load_graph_from_csv('data/basic_directed_graph.csv')
    assert isinstance(graph, nx.DiGraph)
    assert len(graph.nodes) == 4  # Expected number of nodes
    assert len(graph.edges) == 5  # Expected number of edges
    assert graph[1][2]['weight'] == 1  # Check edge weight


def test_load_graph_from_json():
    graph = load_graph_from_json('data/basic_weighted_directed_graph.json')
    assert isinstance(graph, nx.DiGraph)
    assert len(graph.nodes) > 0
    assert len(graph.edges) > 0
