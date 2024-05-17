import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from math import sqrt

def createGraph(pathes, color_pathes):
    pathes =  np.array(pathes)
    color_pathes =  np.array(color_pathes)
    G = nx.Graph()
    for i in range(int(sqrt(pathes.size))):
        for j in range(int(sqrt(pathes.size))):
            if pathes[i, j] > 1:
                G.add_edge(i + 1, j + 1, weight=pathes[i, j])

    pos = nx.spring_layout(G, seed=666)
    nx.draw_networkx_edges(G, pos, width=2, edge_color="tab:green")
    for i in range(int(sqrt(pathes.size))):
        nx.draw_networkx_nodes(G, pos, nodelist=[i + 1], node_size=900, node_color="tab:red")
    for i in range (int(color_pathes.size/2)):
        nx.draw_networkx_edges(G, pos, edgelist= [(color_pathes[i][0], color_pathes[i][1])], width=4, edge_color="tab:red")
    nx.draw_networkx_labels(G, pos, font_size=20)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    plt.savefig("static/images/Graph.png", dpi=150)
    return
