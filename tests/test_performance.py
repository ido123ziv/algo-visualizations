import pytest  # noqa: F401
# import networkx as nx
from common.data_loader import load_graph_from_csv
from algorithms.dijkstra.dijkstra import run_algorithm as dijkstra


def test_performance_on_dijkstra():
    graph = load_graph_from_csv('tests/large_graph.csv')
    start_node = 1
    distances, path, steps = dijkstra(graph, start_node)
