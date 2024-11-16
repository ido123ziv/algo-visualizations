import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from setup import *


def update(num):
    ax.clear()
    # Draw the base current_graph
    nx.draw(graph, pos, with_labels=True, ax=ax, node_color='lightblue', edge_color='gray')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    # Highlight visited nodes
    current_node, current_distances = steps[num]
    visited_nodes = {node for node, _ in steps[:num+1]}
    nx.draw_networkx_nodes(graph, pos, nodelist=visited_nodes, node_color='green', ax=ax)

    # Highlight current node
    nx.draw_networkx_nodes(graph, pos, nodelist=[current_node], node_color='red', ax=ax)

    # Update edge labels with the current shortest path estimates
    for node, dist in current_distances.items():
        ax.text(pos[node][0], pos[node][1] + 0.1, s=f"Dist: {dist}", fontsize=10, color="black")

    ax.set_title(f"Dijkstra's Algorithm Step {num + 1}")


def animate():
    # Create the animation
    ani = animation.FuncAnimation(fig, update, frames=len(steps), repeat=False, interval=1000)

    # Save or display the animation
    plt.show()
