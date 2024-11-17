import pytest
import networkx as nx
from algorithms.dijkstra.dijkstra import dijkstra


# Test 1: Basic Graph
def test_basic_graph():
    graph = nx.DiGraph()
    graph.add_weighted_edges_from([
        (1, 2, 1),
        (2, 3, 2),
        (1, 3, 4)
    ])
    start_node = 1

    distances, path, steps = dijkstra(graph, start_node)

    assert distances == {1: 0, 2: 1, 3: 3}
    assert path == {2: 1, 3: 2}
    assert len(steps) > 0  # Ensure steps are recorded


# Test 2: Empty Graph
def test_empty_graph():
    graph = nx.DiGraph()
    start_node = 1

    distances, path, steps = dijkstra(graph, start_node)

    assert distances == {}
    assert path == {}
    assert steps == []


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
