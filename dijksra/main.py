# import matplotlib.pyplot as plt
# import networkx as nx
# from data import create_graph
from setup import *
import dijksra as dj
import visual as vs

# # Define the position layout for nodes
# pos = nx.spring_layout(G)
#
# # Initialize the figure
# fig, ax = plt.subplots()
# nx.draw(G, pos, with_labels=True, ax=ax)
# labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
#
# plt.savefig("visualization.png")
# plt.title("Graph Visualization for Dijkstra's Algorithm")
# plt.show()


def main():
    dj.dijkstra(graph)
    vs.animate()


if __name__ == '__main__':
    main()
