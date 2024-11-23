import pytest  # noqa: F401
import networkx as nx
from algorithms.dfs.dfs import run_algorithm as dfs

def test_dfs_full_pipeline():
    graph = nx.DiGraph()
    graph.add_edges_from([
        (1, 2),
        (1, 3),
        (2, 4),
        (3, 5)
    ])
    start_node = 1

    distances, path, steps = dfs(graph, start_node)

    # Validate distances (the shortest paths in terms of edges)
    assert distances == {1: 0, 2: 1, 3: 1, 4: 2, 5: 2}

    # Validate path (DFS tree structure)
    assert path ==  {2: 1, 3: 1, 4: 2, 5: 3}