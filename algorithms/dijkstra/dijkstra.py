import heapq


def run_algorithm(graph, start_node):
    """
     Run Dijkstra's algorithm on the given graph with negative weight detection.

     Args:
         graph (networkx.Graph): The input graph.
         start_node: The starting node for Dijkstra's algorithm.

     Returns:
         tuple: (distances, path, steps)
             - distances: A dictionary of the shortest distances from start_node.
             - path: A dictionary of the shortest path tree.
             - steps: A list of steps for visualization.

     Raises:
         ValueError: If the graph contains negative edge weights.
         ValueError: If the start node is not in graph.
         ValueError: If the has no nodes.
     """
    distances = {node: float('inf') for node in graph.nodes}

    # validate empty graph
    if graph.nodes is None or len(graph.nodes) == 0:
        raise ValueError("Graph has no nodes.")

    # validation if start node in graph
    if start_node not in graph.nodes:
        raise ValueError("Start node not found in the graph")

    # validation for edges weight
    for u, v, data in graph.edges(data=True):
        if data.get('weight', 0) < 0:
            raise ValueError(f"Graph contains negative weight edges. Found on edge ({u}, {v}) with weight {data['weight']}.")

    distances[start_node] = 0
    visited = set()
    path = {}
    priority_queue = [(0, start_node)]
    steps = []

    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)
        step = {
            'current_node': current_node,
            'updated_edges': [],
            'annotation': f"Visiting Node {current_node}, Distance: {current_dist}"
        }

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                path[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
                step['updated_edges'].append((current_node, neighbor))

        steps.append(step)

    return distances, path, steps
