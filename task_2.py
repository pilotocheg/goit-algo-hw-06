from graph import G
from algorithms.bfs import bfs
from algorithms.dfs import dfs

# BFS
result = bfs(G, start="Kyiv")
print("Результат обходу в ширину:")
print(result, "\n")

# DFS
result = dfs(G, start="Kyiv")
print("Результат обходу в глибину:")
print(result)
