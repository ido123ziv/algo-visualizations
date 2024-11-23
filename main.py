import networkx as nx
import os
import pathlib
import importlib
import pkgutil
from common.data_loader import load_graph_from_csv, load_graph_from_json
from common.visualizer import visualize_algorithm_progress, visualize_graph


def discover_algorithms():
    """
    Dynamically discover all algorithms in the `algorithms` package.
    Each algorithm must define a `run_algorithm(graph, start_node)` function.
    """
    algorithms = {}
    for _, name, _ in pkgutil.iter_modules(['algorithms']):
        module = importlib.import_module(f"algorithms.{name}")
        if hasattr(module, 'run_algorithm'):
            algorithms[name] = module.run_algorithm
    return algorithms


def run(graph, algorithm_name, algorithm_func, graph_name):
    """
    Run a specific algorithm on a graph and generate visualization.
    """
    start_node = 1
    pos = nx.spring_layout(graph)
    visualize_graph(graph, pos, title=f"{algorithm_name.capitalize()} Algorithm Visualization")

    distances, path, steps = algorithm_func(graph, start_node)
    # this is used for creating a folder if doesn't exist
    if not os.path.exists("animations"):
        os.mkdir("animations")
    # Run the algorithm and get steps
    gif_name = f"animations/{algorithm_name}_on_{graph_name}.gif"

    # Visualize the progress generically
    visualize_algorithm_progress(
        graph, pos, steps,
        title=f"{algorithm_name.capitalize()} Algorithm Animation",
        output_file=gif_name
    )


def main():
    # Discover algorithms dynamically
    algorithms = discover_algorithms()

    # Load all graphs from the data folder
    graphs = os.listdir('data')
    for input_graph in graphs:
        graph_name = pathlib.Path(f"data/{input_graph}").stem
        if input_graph.endswith('csv'):
            graph = load_graph_from_csv(f"data/{input_graph}")
        elif input_graph.endswith('json'):
            graph = load_graph_from_json(f"data/{input_graph}")
        else:
            raise ValueError("Unsupported graph format")

        # Run all algorithms on the current graph
        for algorithm_name, algorithm_func in algorithms.items():
            run(graph, algorithm_name, algorithm_func, graph_name)


if __name__ == '__main__':
    main()
