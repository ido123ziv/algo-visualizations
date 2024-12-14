import networkx as nx
from algorithms.prim import run_algorithm


def test_prim_algorithm():
    graph = nx.Graph()
    graph.add_weighted_edges_from([
        (1, 2, 1),
        (1, 3, 4),
        (2, 3, 2),
        (2, 4, 5),
        (3, 4, 3)
    ])
    start_node = 1
    mst_edges, total_weight, steps = run_algorithm(graph, start_node)
    assert set(mst_edges) == {(1, 2), (2, 3), (3, 4)}
    assert total_weight == 6


def test_non_existent_start_node():
    graph = nx.Graph()
    graph.add_weighted_edges_from([
        (1, 2, 1),
        (1, 3, 4),
        (2, 3, 2),
        (2, 4, 5),
        (3, 4, 3)
    ])
    start_node = 5
    try:
        run_algorithm(graph, start_node)
    except ValueError as e:
        assert str(e) == "Start node not found in the graph."
