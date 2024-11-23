import heapq


def run_algorithm(graph, start_node):
    """
    Run Dijkstra's algorithm on the graph.
    """
    distances = {node: float('inf') for node in graph.nodes}
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
