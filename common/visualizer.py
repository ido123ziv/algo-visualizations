import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
import stat


def patch_file_permissions(file_path):
    os.chmod(file_path,
             stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH |
             stat.S_IXUSR | stat.S_IRUSR | stat.S_IWUSR |
             stat.S_IWGRP | stat.S_IXGRP)


def visualize_graph(graph, pos, title="Graph Visualization"):
    """Visualize the graph with node labels and edge weights."""
    plt.figure()
    nx.draw(graph, pos, with_labels=True,
            node_color='lightblue', edge_color='gray')
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos,
                                 edge_labels=labels)
    plt.title(title)
    plt.show()


def update_frame(graph, pos, ax, node_colors, edge_colors, edge_labels, steps, frame,
                 node_highlight_key, edge_highlight_key, annotation_key, title):
    """
    Update function for FuncAnimation, separated from the main visualize function.
    """
    ax.clear()
    ax.set_title(title)

    # Draw the base graph
    nx.draw(graph, pos, with_labels=True,
            node_color=node_colors,
            edge_color=edge_colors,
            ax=ax)
    nx.draw_networkx_edge_labels(graph,
                                 pos,
                                 edge_labels=edge_labels,
                                 ax=ax)

    # Get the current step data
    step = steps[frame]

    # Highlight nodes
    if node_highlight_key in step:
        highlight_nodes = step[node_highlight_key]
        if isinstance(highlight_nodes, (list, set)):
            for node in highlight_nodes:
                node_colors[node] = 'orange'
        else:
            node_colors[highlight_nodes] = 'orange'

    # Highlight edges
    if edge_highlight_key in step:
        highlight_edges = step[edge_highlight_key]
        for edge in highlight_edges:
            edge_index = list(graph.edges).index(edge)
            edge_colors[edge_index] = 'red'

    # Add annotation
    if annotation_key in step:
        ax.text(0.01, 0.01, step[annotation_key],
                transform=ax.transAxes,
                fontsize=10,
                va='bottom')


def visualize_algorithm_progress(graph, pos, steps,
                                 node_highlight_key='current_node',
                                 edge_highlight_key='updated_edges',
                                 annotation_key='annotation',
                                 title="Algorithm Progress",
                                 output_file="algorithm_progress.gif"):
    """
    Generic visualizer for graph-based algorithms.
    """
    fig, ax = plt.subplots()
    ax.set_title(title)

    # Initialize base graph elements
    node_colors = ['lightblue' for _ in range(len(graph.nodes))]
    edge_colors = ['gray' for _ in range(len(graph.edges))]
    edge_labels = nx.get_edge_attributes(graph, 'weight')

    # Create the animation
    anim = FuncAnimation(fig, update_frame,
                         frames=len(steps),
                         fargs=(graph, pos, ax, node_colors, edge_colors, edge_labels,
                                steps, node_highlight_key, edge_highlight_key, annotation_key, title),
                         interval=1000,
                         repeat=False)

    # Save the animation
    anim.save(output_file, writer='pillow')
    if os.path.exists(output_file):
        patch_file_permissions(output_file)

    # Only show the plot if not running in CI
    if not os.getenv("CI_RUN"):
        plt.show()
