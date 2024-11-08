#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import yaml
import rospy

# Fungsi untuk menghasilkan node acak
def generate_random_nodes(num_nodes, x_max, y_max):
    return np.random.rand(num_nodes, 2) * [x_max, y_max]

# Fungsi utama untuk menjalankan PRM
def main():
    rospy.init_node('prm_node', anonymous=True)

    # Membaca parameter dari file params.yaml
    with open('/home/hendriazwar/prm_ws/src/prm_project/params.yaml', 'r') as file:
        params = yaml.safe_load(file)

    num_nodes = params['num_nodes']
    x_max = params['x_max']
    y_max = params['y_max']
    threshold = params['threshold']

    # Generasi node dan pembuatan graf
    nodes = generate_random_nodes(num_nodes, x_max, y_max)
    G = nx.Graph()

    for i, (x, y) in enumerate(nodes):
        G.add_node(i, pos=(x, y))

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            dist = np.linalg.norm(nodes[i] - nodes[j])
            if dist < threshold:
                G.add_edge(i, j, weight=dist)

    start, goal = 0, num_nodes - 1
    path = nx.dijkstra_path(G, source=start, target=goal)

    pos = nx.get_node_attributes(G, 'pos')
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, node_color='blue', edge_color='red', with_labels=False, node_size=50)
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_nodes(G, pos, nodelist=[start], node_color='green', node_size=100, label='Start')
    nx.draw_networkx_nodes(G, pos, nodelist=[goal], node_color='red', node_size=100, label='Goal')
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='yellow', width=2)
    plt.title("Probabilistic Roadmap (PRM) with Shortest Path")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
