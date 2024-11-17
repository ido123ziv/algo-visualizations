import networkx as nx
from common.data_loader import load_graph_from_csv, load_graph_from_json
from common.visualizer import visualize_graph
from algorithms.dijkstra.dijkstra import dijkstra


def main():
    graph_file = "algorithms/dijkstra/example.csv"
    graph = load_graph_from_csv(graph_file)
    start_node = 1

    distances, path, steps = dijkstra(graph, start_node)

    # Visualize the graph
    pos = nx.spring_layout(graph)
    visualize_graph(graph, pos, title="Dijkstra's Algorithm Visualization")


if __name__ == '__main__':
    main()
