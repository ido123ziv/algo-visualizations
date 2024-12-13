import networkx as nx

def run_algorithm(graph, start_node=None):
    """
    Run Kruskal's Algorithm to find the Minimum Spanning Tree (MST) on the given graph.

    Args:
        graph (networkx.Graph): The input graph.
        start_node: Not used in Kruskal's Algorithm, included for consistency.

    Returns:
        tuple: (mst_edges, total_weight, steps)
            - mst_edges: A list of edges in the MST.
            - total_weight: The total weight of the MST.
            - steps: A list of steps for visualization.
    """
    mst_edges = []
    total_weight = 0
    steps = []

    # Sort edges by weight
    sorted_edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])

    # Create a union-find data structure
    uf = nx.utils.UnionFind()

    for u, v, data in sorted_edges:
        if uf[u] != uf[v]:
            uf.union(u, v)
            mst_edges.append((u, v))
            total_weight += data['weight']
            step = {
                'current_node': None,
                'updated_edges': [(u, v)],
                'annotation': f"Adding edge ({u}, {v}) with weight {data['weight']}"
            }
            steps.append(step)

    return mst_edges, total_weight, steps