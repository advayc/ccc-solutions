import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def showgraph(graph):
    G = nx.DiGraph()

    # Add edges to the graph
    for node in graph:
        for neighbor in graph[node]:
            G.add_edge(node, neighbor)

    # Define node colors
    node_colors = {node: 'tab:blue' for node in G.nodes()}
    # Customize node color based on your graph's characteristics, if needed
    node_colors[list(G.nodes())[0]] = 'tab:red'

    pos = nx.spring_layout(G, seed=3113794652)  # positions for all nodes

    options = {"edgecolors": "tab:gray", "node_size": 800, "alpha": 0.9}
    node_color_list = [mcolors.CSS4_COLORS.get(node_colors[node], 'tab:blue') for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_color=node_color_list, **options)
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif', font_color="whitesmoke")

    plt.title('Graph Visualization')
    plt.axis('off')
    plt.show()

def showpath(graph, path):
    G = nx.DiGraph()

    # Add edges to the graph
    for node in graph:
        for neighbor in graph[node]:
            G.add_edge(node, neighbor)

    # Define node colors
    node_colors = {node: 'tab:blue' for node in G.nodes()}
    node_colors[path[0]] = 'tab:yellow'  # Starting node
    node_colors[path[-1]] = 'tab:blue'  # Ending node

    pos = nx.spring_layout(G, seed=3113794652)  # positions for all nodes

    options = {"edgecolors": "tab:gray", "node_size": 800, "alpha": 0.9}
    node_color_list = [mcolors.CSS4_COLORS.get(node_colors[node], 'tab:blue') for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_color=node_color_list, **options)

    # Highlight the path edges
    path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=2, alpha=0.7, edge_color="tab:red")

    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif', font_color="whitesmoke")

    plt.title('Graph Visualization with Highlighted Path')
    plt.axis('off')
    plt.show()
