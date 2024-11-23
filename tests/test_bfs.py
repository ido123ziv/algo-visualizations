import pytest
import networkx as nx
from algorithms.bfs.bfs import run_algorithm as bfs


# Test 1: Full Pipeline Test
def test_bfs_full_pipeline():
    graph = nx.DiGraph()
    graph.add_edges_from([
        (1, 2),
        (1, 3),
        (2, 4),
        (3, 5)
    ])
    start_node = 1

    distances, path, steps = bfs(graph, start_node)

    # Validate distances (shortest paths in terms of edges)
    assert distances == {1: 0, 2: 1, 3: 1, 4: 2, 5: 2}

    # Validate path (BFS tree structure)
    assert path == {2: 1, 3: 1, 4: 2, 5: 3}


# Test 2: Empty Graph
def test_empty_graph():
    graph = nx.DiGraph()

    with pytest.raises(ValueError, match="Graph has no nodes."):
        bfs(graph, start_node=1)


# Test 3: Graph with Disconnected Nodes
def test_disconnected_graph():
    graph = nx.DiGraph()
    graph.add_edges_from([
        (1, 2),
        (2, 3)
    ])
    start_node = 1

    distances, path, steps = bfs(graph, start_node)

    # Validate distances for connected nodes
    assert distances == {1: 0, 2: 1, 3: 2}

    # Add a disconnected node
    graph.add_node(4)
    distances, path, steps = bfs(graph, start_node)

    # Validate the disconnected node
    assert distances[4] == float('inf')
    assert 4 not in path


# Test 4: Cyclic Graph
def test_cyclic_graph():
    graph = nx.DiGraph()
    graph.add_edges_from([
        (1, 2),
        (2, 3),
        (3, 1),  # Cycle
        (3, 4)
    ])
    start_node = 1

    distances, path, steps = bfs(graph, start_node)

    # Validate distances
    assert distances == {1: 0, 2: 1, 3: 2, 4: 3}

    # Validate path
    assert path == {2: 1, 3: 2, 4: 3}


# Test 5: Non-existent Start Node
def test_non_existent_start_node():
    graph = nx.DiGraph()
    graph.add_edges_from([
        (1, 2),
        (2, 3)
    ])
    start_node = 4

    with pytest.raises(ValueError, match="Start node not found in the graph."):
        bfs(graph, start_node)


# Test 6: Multiple Components
def test_multiple_components():
    graph = nx.DiGraph()
    graph.add_edges_from([
        (1, 2),
        (2, 3),
        # Separate component
        (4, 5)
    ])
    start_node = 1

    distances, path, steps = bfs(graph, start_node)

    # Validate distances for the first component
    assert distances == {1: 0, 2: 1, 3: 2, 4: float('inf'), 5: float('inf')}

    # Validate path for the first component
    assert path == {2: 1, 3: 2}


# Test 7: Single Node Graph
def test_single_node_graph():
    graph = nx.DiGraph()
    graph.add_node(1)
    start_node = 1

    distances, path, steps = bfs(graph, start_node)

    # Validate distances
    assert distances == {1: 0}

    # Validate path (no edges)
    assert path == {}


# Test 8: Graph with Parallel Edges (Ignored in BFS)
def test_parallel_edges():
    graph = nx.DiGraph()
    graph.add_edges_from([
        (1, 2),
        (1, 2),  # Parallel edge
        (2, 3)
    ])
    start_node = 1

    distances, path, steps = bfs(graph, start_node)

    # Validate distances
    assert distances == {1: 0, 2: 1, 3: 2}

    # Validate path
    assert path == {2: 1, 3: 2}
