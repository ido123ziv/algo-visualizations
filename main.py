import networkx as nx
from common.data_loader import load_graph_from_csv, load_graph_from_json
from common.visualizer import visualize_algorithm_progress, visualize_graph
from algorithms.dijkstra.dijkstra import dijkstra
import os
import pathlib


def run(graph, name: str):
    start_node = 1
    pos = nx.spring_layout(graph)
    visualize_graph(graph, pos, title="Dijkstra's Algorithm Visualization")

    distances, path, steps = dijkstra(graph, start_node)
    gif_name = f"animations/dijkstra_on_{name}.gif"
    # Visualize the progress generically
    visualize_algorithm_progress(
        graph, pos, steps,
        title="Dijkstra's Algorithm Animation",
        output_file=gif_name
    )


def main():
    graphs = os.listdir('data')
    for input_graph in graphs:
        graph_name = pathlib.Path(f"{os.getcwd()}/data/{input_graph}").stem
        if input_graph.endswith('csv'):
            graph = load_graph_from_csv("data/{}".format(input_graph))
        if input_graph.endswith('json'):
            graph = load_graph_from_json("data/{}".format(input_graph))
        if graph is None or graph == "":
            raise ValueError("Graph not in format")
        run(graph, graph_name)
        pass
    # graph_file = "algorithms/dijkstra/example.csv"
    # start_node = 1
    #
    # # Compute graph layout
    # pos = nx.spring_layout(graph)
    # visualize_graph(graph, pos, title="Dijkstra's Algorithm Visualization")
    #
    # # Run Dijkstra's algorithm
    # distances, path, steps = dijkstra(graph, start_node)
    #
    # # Visualize the progress generically
    # visualize_algorithm_progress(
    #     graph, pos, steps,
    #     title="Dijkstra's Algorithm Animation",
    #     output_file="dijkstra_progress.gif"
    # )


if __name__ == '__main__':
    main()
