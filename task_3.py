from algorithms.dejkstra import dejkstra
from graph import G

shortest_paths = dejkstra(G, start="Kyiv")

print("Найкоротші шляхи від Києва до інших міст:")
print(shortest_paths)
