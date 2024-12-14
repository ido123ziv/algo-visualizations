def run_algorithm(graph, start_node):
    """
    Run Bellman-Ford Algorithm to find the shortest paths from the start node to all other nodes.

    Args:
        graph (networkx.Graph): The input graph.
        start_node: The starting node for Bellman-Ford Algorithm.

    Returns:
        tuple: (distances, path, steps)
            - distances: A dictionary of the shortest distances from start_node.
            - path: A dictionary representing the shortest path tree.
            - steps: A list of steps for visualization.
    """
    distances = {node: float('inf') for node in graph.nodes}
    path = {}
    steps = []

    # validate empty graph
    if graph.nodes is None or len(graph.nodes) == 0:
        raise ValueError("Graph has no nodes.")

    # validation if start node in graph
    if start_node not in graph.nodes:
        raise ValueError("Start node not found in the graph.")

    distances[start_node] = 0

    # Relax edges repeatedly
    for _ in range(len(graph.nodes) - 1):
        for u, v, data in graph.edges(data=True):
            weight = data['weight']
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                path[v] = u
                step = {
                    'current_node': v,
                    'updated_edges': [(u, v)],
                    'annotation': f"Updating distance of node {v} to {distances[v]}"
                }
                steps.append(step)

    # Check for negative weight cycles
    for u, v, data in graph.edges(data=True):
        weight = data['weight']
        if distances[u] + weight < distances[v]:
            raise ValueError("Graph contains a negative weight cycle.")

    return distances, path, steps
