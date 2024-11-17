import networkx as nx
import matplotlib.pyplot as plt


def visualize_graph(graph, pos, title="Graph Visualization"):
    """Visualize the graph with node labels and edge weights."""
    plt.figure()
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.title(title)
    plt.show()
