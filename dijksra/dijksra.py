import heapq
from setup import *


def dijkstra(current_graph):
    priority_queue = [(0, start_node)]  # (distance, node)

    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)
        steps.append((current_node, dict(distances)))  # Record the step

        for neighbor in current_graph.neighbors(current_node):
            weight = current_graph[current_node][neighbor]['weight']
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                path[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))