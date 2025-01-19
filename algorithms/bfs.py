from collections import deque
from networkx import Graph


def bfs(graph: Graph, start: str):
    visited = set()
    result = []
    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            queue.extend(set(dict(graph[vertex]).keys()) - visited)

    return result
