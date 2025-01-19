from networkx import Graph


def dfs(graph: Graph, start: str):
    visited = set()
    result = []
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            stack.extend(reversed(dict(graph[vertex]).keys()))

    return result
