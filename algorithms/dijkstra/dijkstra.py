import heapq


def dijkstra(graph, start_node):
    """Implement Dijkstra's algorithm."""
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
        steps.append((current_node, dict(distances)))

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                path[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, path, steps
