import networkx as nx
from algorithms.kruskal import run_algorithm

def test_kruskal_algorithm():
    graph = nx.Graph()
    graph.add_weighted_edges_from([
        (1, 2, 1),
        (1, 3, 4),
        (2, 3, 2),
        (2, 4, 5),
        (3, 4, 3)
    ])
    mst_edges, total_weight, steps = run_algorithm(graph)
    assert set(mst_edges) == {(1, 2), (2, 3), (3, 4)}
    assert total_weight == 6

def test_disconnected_graph():
    graph = nx.Graph()
    graph.add_weighted_edges_from([
        (1, 2, 1),
        (3, 4, 2)
    ])
    mst_edges, total_weight, steps = run_algorithm(graph)
    assert set(mst_edges) == {(1, 2), (3, 4)}
    assert total_weight == 3

def test_empty_graph():
    graph = nx.Graph()
    mst_edges, total_weight, steps = run_algorithm(graph)
    assert mst_edges == []
    assert total_weight == 0