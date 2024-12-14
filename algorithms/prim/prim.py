import heapq
import networkx as nx


def run_algorithm(graph: nx.Graph, start_node):
    """
    Run Prim's Algorithm to find the Minimum Spanning Tree (MST) on the given graph.

    Args:
        graph (networkx.Graph): The input graph.
        start_node: The starting node for Prim's Algorithm.

    Returns:
        tuple: (mst_edges, total_weight, steps)
            - mst_edges: A list of edges in the MST.
            - total_weight: The total weight of the MST.
            - steps: A list of steps for visualization.
    """
    if start_node not in graph.nodes:
        raise ValueError("Start node not found in the graph.")

    mst_edges = []
    total_weight = 0
    visited = set()
    priority_queue = [(0, start_node, None)]
    steps = []

    while priority_queue:
        weight, current_node, from_node = heapq.heappop(priority_queue)
        if current_node in visited:
            continue
        visited.add(current_node)
        if from_node is not None:
            mst_edges.append((from_node, current_node))
            total_weight += weight
            step = {
                'current_node': current_node,
                'updated_edges': [(from_node, current_node)],
                'annotation': f"Adding edge ({from_node}, {current_node}) with weight {weight}"
            }
            steps.append(step)
        for neighbor, data in graph[current_node].items():
            if neighbor not in visited:
                heapq.heappush(priority_queue, (data['weight'], neighbor, current_node))

    return mst_edges, total_weight, steps
