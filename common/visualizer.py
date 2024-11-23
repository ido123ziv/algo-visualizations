import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def visualize_graph(graph, pos, title="Graph Visualization"):
    """Visualize the graph with node labels and edge weights."""
    plt.figure()
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.title(title)
    plt.show()


def visualize_algorithm_progress(graph, pos, steps, node_highlight_key='current_node',
                                 edge_highlight_key='updated_edges', annotation_key='annotation',
                                 title="Algorithm Progress", output_file="algorithm_progress.gif"):
    """
    Generic visualizer for graph-based algorithms.

    Args:
        graph (networkx.Graph): The graph to visualize.
        pos (dict): Node positions for consistent visualization.
        steps (list): List of steps, each step being a dictionary of highlights and annotations.
                      Example:
                      [
                          {
                              'current_node': 1,
                              'updated_edges': [(1, 2), (1, 3)],
                              'annotation': "Visiting Node 1"
                          },
                          ...
                      ]
        node_highlight_key (str): Key in steps dict for nodes to highlight.
        edge_highlight_key (str): Key in steps dict for edges to highlight.
        annotation_key (str): Key in steps dict for custom annotations.
        title (str): Title of the visualization.
        output_file (str): Path to save the animation as a GIF.
        :param steps:
        :param pos:
        :param graph:
        :param edge_highlight_key:
        :param title:
        :param output_file:
        :param annotation_key:
        :param node_highlight_key:
    """
    fig, ax = plt.subplots()
    ax.set_title(title)

    # Initialize base graph elements
    node_colors = ['lightblue' for _ in range(len(graph.nodes))]
    edge_colors = ['gray' for _ in range(len(graph.edges))]
    node_color_map = {node: i for i, node in enumerate(graph.nodes)}
    edge_list = list(graph.edges)

    def update(frame):
        ax.clear()
        ax.set_title(title)

        # Draw the base graph
        nx.draw(graph, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, ax=ax)
        edge_labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, ax=ax)

        # Get the current step data
        step = steps[frame]

        # Highlight nodes
        if node_highlight_key in step:
            highlight_nodes = step[node_highlight_key]
            if isinstance(highlight_nodes, (list, set)):
                for node in highlight_nodes:
                    node_colors[node_color_map[node]] = 'orange'
            else:
                node_colors[node_color_map[highlight_nodes]] = 'orange'

        # Highlight edges
        if edge_highlight_key in step:
            highlight_edges = step[edge_highlight_key]
            for edge in highlight_edges:
                if edge in edge_list:
                    edge_colors[edge_list.index(edge)] = 'red'

        # Add annotation
        if annotation_key in step:
            ax.text(0.01, 0.01, step[annotation_key], transform=ax.transAxes, fontsize=10, va='bottom')

    # Create the animation
    anim = FuncAnimation(fig, update, frames=len(steps), interval=1000, repeat=False)

    # Save the animation
    anim.save(output_file, writer='pillow')
    plt.show()
