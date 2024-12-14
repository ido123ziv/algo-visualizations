import networkx as nx
from algorithms.bellman_ford import run_algorithm

def test_bellman_ford_algorithm():
    graph = nx.DiGraph()
    graph.add_weighted_edges_from([
        (1, 2, 4),
        (1, 3, 2),
        (2, 3, 3),
        (2, 4, 2),
        (3, 2, 1),
        (3, 4, 5)
    ])
    start_node = 1
    distances, path, steps = run_algorithm(graph, start_node)
    assert distances == {1: 0, 2: 3, 3: 2, 4: 5}
    assert path == {2: 3, 3: 1, 4: 2}

def test_negative_weight_cycle():
    graph = nx.DiGraph()
    graph.add_weighted_edges_from([
        (1, 2, 4),
        (2, 3, -10),
        (3, 1, 3)
    ])
    start_node = 1
    try:
        run_algorithm(graph, start_node)
    except ValueError as e:
        assert str(e) == "Graph contains a negative weight cycle."

def test_empty_graph():
    graph = nx.DiGraph()
    start_node = 1
    try:
        run_algorithm(graph, start_node)
    except ValueError as e:
        assert str(e) == "Graph has no nodes."

def test_non_existent_start_node():
    graph = nx.DiGraph()
    graph.add_weighted_edges_from([
        (1, 2, 4),
        (2, 3, 3)
    ])
    start_node = 4
    try:
        run_algorithm(graph, start_node)
    except ValueError as e:
        assert str(e) == "Start node not found in the graph."