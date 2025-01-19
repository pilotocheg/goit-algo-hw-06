from networkx import Graph


def dejkstra(graph: Graph, start: str):
    unvisited = list(graph.nodes())
    distances = {vertex: float("infinity") for vertex in unvisited}
    distances[start] = 0

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float("infinity"):
            break

        for neighbor, props in graph[current_vertex].items():
            distance = distances[current_vertex] + props["weight"]

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances
