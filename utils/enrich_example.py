import os
import argparse
import importlib
from common.data_loader import load_graph_from_csv
from common.visualizer import visualize_algorithm_progress
import networkx as nx


def main(args_stack):
    algo = args_stack.algorithm
    if not os.path.exists(f"algorithms/{algo}"):
        raise ValueError("Algorithm is not here yet!")

    module = importlib.import_module(f"algorithms.{algo}")
    if not hasattr(module, 'run_algorithm'):
        raise ValueError("Algorithm is not ready yet!")
    if args_stack.directed:
        graph = load_graph_from_csv("utils/directed_graph.csv")
    else:
        graph = load_graph_from_csv("utils/undirected_graph.csv")

    start_node = 1
    pos = nx.spring_layout(graph)

    gif_name = f"algorithms/{algo}/{algo}_progress.gif"

    # Run the algorithm and get steps
    distances, path, steps = module.run_algorithm(graph, start_node)
    visualize_algorithm_progress(
        graph, pos, steps,
        title=f"{algo.capitalize()} Algorithm Animation",
        output_file=gif_name
    )
    if os.path.exists(f"algorithms/{algo}/README.md"):
        with open(f"algorithms/{algo}/README.md", 'r') as readme:
            content = readme.read()
    else:
        content = f"""# {algo.capitalize()}
        This is a new algorithm here!
        """
    content += f""" ## Results
![](./{algo}_progress.gif)

    """
    with open(f"algorithms/{algo}/README.md", 'w+') as readme:
        readme.write(content)

    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Algorithm Chooser")
    parser.add_argument('--algorithm', metavar='-a', dest="algorithm",
                        help="which algorithm to add example for?",
                        required=True)
    parser.add_argument('--directed', dest="directed",
                        help="should we use directed graph?",
                        action="store_true",
                        required=False,
                        )
    parser.add_argument('--undirected',
                        action='store_false',
                        help="should we use directed graph?",
                        required=False,
                        )
    parser.set_defaults(directed=True)
    args = parser.parse_args()
    main(args)
