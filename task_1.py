import networkx as nx
import matplotlib.pyplot as plt
from graph import G

pos = {
    "Kyiv": (0, 0),
    "Poltava": (2, -0.4),
    "Kharkiv": (3, -0.1),
    "Uzhorod": (-3.5, -1),
    "Lviv": (-3, -0.5),
    "Dnipro": (2.3, -1),
    "Odesa": (0, -2),
    "Mykolaiv": (0.5, -1.8),
    "Zaporizhzhia": (2.3, -1.5),
    "Mariupol": (3.2, -1.9),
    "Chernihiv": (0.2, 0.6),
    "Sumy": (2.1, 0.3),
    "Vinnytsia": (-1, -1),
}

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
is_connected = nx.is_connected(G)
degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)

print("Основні характеристики графа:")
print("Кількість вузлів:", num_nodes)
print("Кількість ребер:", num_edges)
print("Граф зв'язний:", "Так" if is_connected else "Ні")
print("Ступінь центральності:", degree_centrality)
print("Близькість вузла:", closeness_centrality)
print("Посередницство вузла:", betweenness_centrality)

nx.draw(G, pos, with_labels=True)
plt.show()
