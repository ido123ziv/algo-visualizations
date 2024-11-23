import pytest
import networkx as nx
from common.data_loader import load_graph_from_csv
from algorithms.dijkstra.dijkstra import run_algorithm as dijkstra


def test_dijkstra_full_pipeline():
    graph = load_graph_from_csv('data/basic_directed_graph.csv')
    start_node = 1
    distances, path, steps = dijkstra(graph, start_node)

    # Validate distances
    assert distances[3] == 3  # Example expected distance
    assert distances[4] == 4  # Example expected distance
    # Validate path
    assert path[4] == 2
    assert path[3] == 2


# Test 2: Empty Graph
def test_empty_graph():
    graph = nx.DiGraph()
    # start_node = 1

    with pytest.raises(ValueError, match="Graph has no nodes."):
        dijkstra(graph, start_node=1)


# Test 3: Graph with Disconnected Nodes
def test_disconnected_graph():
    graph = nx.DiGraph()
    graph.add_weighted_edges_from([
        (1, 2, 1),
        (2, 3, 2)
    ])
    start_node = 1

    distances, path, steps = dijkstra(graph, start_node)

    assert distances == {1: 0, 2: 1, 3: 3}
    assert path == {2: 1, 3: 2}

    # Add a disconnected node
    graph.add_node(4)
    distances, path, steps = dijkstra(graph, start_node)

    assert distances[4] == float('inf')
    assert 4 not in path


# Test 4: Negative Weights (Dijkstra should not support negative weights)
def test_negative_weights():
    graph = nx.DiGraph()
    graph.add_weighted_edges_from([
        (1, 2, -1),
        (2, 3, 2)
    ])
    start_node = 1

    with pytest.raises(ValueError, match="Graph contains negative weight edges"):
        dijkstra(graph, start_node)


# Test 5: Cyclic Graph
def test_cyclic_graph():
    graph = nx.DiGraph()
    graph.add_weighted_edges_from([
        (1, 2, 1),
        (2, 3, 2),
        (3, 1, 3)
    ])
    start_node = 1

    distances, path, steps = dijkstra(graph, start_node)

    assert distances == {1: 0, 2: 1, 3: 3}
    assert path == {2: 1, 3: 2}


# Test 6: Non-existent Start Node
def test_non_existent_start_node():
    graph = nx.DiGraph()
    graph.add_weighted_edges_from([
        (1, 2, 1),
        (2, 3, 2)
    ])
    start_node = 4

    with pytest.raises(ValueError, match="Start node not found in the graph"):
        dijkstra(graph, start_node)
