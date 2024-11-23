def run_algorithm(graph, start_node):
    """
    Run Depth-First Search (DFS) on the given graph.

    Args:
        graph (networkx.Graph): The input graph.
        start_node: The starting node for DFS.

    Returns:
        tuple: (distances, path, steps)
            - distances: A dictionary of the shortest distances from start_node.
            - path: A dictionary representing the DFS tree.
            - steps: A list of steps for visualization.
    """
    distances = {node: float('inf') for node in graph.nodes}
    distances[start_node] = 0
    path = {}
    visited = set()
    stack = [start_node]
    steps = []

    while stack:
        current_node = stack.pop()
        visited.add(current_node)

        step = {
            'current_node': current_node,
            'updated_edges': [],
            'annotation': f"Visiting Node {current_node}, Distance: {distances[current_node]}"
        }

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
                distances[neighbor] = distances[current_node] + 1
                path[neighbor] = current_node
                step['updated_edges'].append((current_node, neighbor))

        steps.append(step)

    return distances, path, steps
