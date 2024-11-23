import networkx as nx
from common.data_loader import load_graph_from_csv
from common.visualizer import visualize_algorithm_progress, visualize_graph
from algorithms.dijkstra.dijkstra import dijkstra


def main():
    graph_file = "algorithms/dijkstra/example.csv"
    graph = load_graph_from_csv(graph_file)
    start_node = 1

    # Compute graph layout
    pos = nx.spring_layout(graph)
    visualize_graph(graph, pos, title="Dijkstra's Algorithm Visualization")

    # Run Dijkstra's algorithm
    distances, path, steps = dijkstra(graph, start_node)

    # Visualize the progress generically
    visualize_algorithm_progress(
        graph, pos, steps,
        title="Dijkstra's Algorithm Animation",
        output_file="dijkstra_progress.gif"
    )


if __name__ == '__main__':
    main()
