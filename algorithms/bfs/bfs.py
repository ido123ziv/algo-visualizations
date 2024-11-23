from collections import deque


def run_algorithm(graph, start_node):
    """
    Run Breadth-First Search (BFS) on the given graph.

    Args:
        graph (networkx.Graph): The input graph.
        start_node: The starting node for BFS.

    Returns:
        tuple: (distances, path, steps)
            - distances: A dictionary of the shortest distances from start_node.
            - path: A dictionary representing the BFS tree.
            - steps: A list of steps for visualization.
    """
    distances = {node: float('inf') for node in graph.nodes}
    # validate empty graph
    if graph.nodes is None or len(graph.nodes) == 0:
        raise ValueError("Graph has no nodes.")

    # validation if start node in graph
    if start_node not in graph.nodes:
        raise ValueError("Start node not found in the graph.")

    distances[start_node] = 0
    path = {}
    visited = set()
    queue = deque([start_node])
    steps = []

    while queue:
        current_node = queue.popleft()
        visited.add(current_node)

        step = {
            'current_node': current_node,
            'updated_edges': [],
            'annotation': f"Visiting Node {current_node}, Distance: {distances[current_node]}"
        }

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
                visited.add(neighbor)
                distances[neighbor] = distances[current_node] + 1
                path[neighbor] = current_node
                step['updated_edges'].append((current_node, neighbor))

        steps.append(step)

    return distances, path, steps
