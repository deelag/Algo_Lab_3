from queue import PriorityQueue

from edge import Edge


def find_min_latency(graph, clients, routers):
    """
    >>> graph =  [[Edge(3, 10)], [Edge(3, 40), Edge(4, 100)], [Edge(1, 10), Edge(2, 40), Edge(4, 80)], [Edge(2, 100), Edge(3, 80), Edge(5, 50)], [Edge(4, 50), Edge(6, 20)], [Edge(5, 20)]]
    >>> clients = [0, 1, 5]
    >>> routers = [2, 3, 4]
    >>> find_min_latency(graph, clients, routers)
    100
    >>> graph = [[Edge(2, 50)], [Edge(1, 50), Edge(3, 1000000000)], [Edge(2, 1000000000)]]
    >>> clients = [0, 2]
    >>> routers = [1]
    >>> find_min_latency(graph, clients, routers)
    1000000000
    """
    max_values = []

    for router in routers:
        client_distances = []
        for client in clients:
            client_distances.append(dijkstra(graph, router).pop(client))
        max_values.append(max(client_distances))
    return min(max_values)


def dijkstra(graph, start_node):
    """
    >>> graph =  [[Edge(3, 10)], [Edge(3, 40), Edge(4, 100)], [Edge(1, 10), Edge(2, 40), Edge(4, 80)], [Edge(2, 100), Edge(3, 80), Edge(5, 50)], [Edge(4, 50), Edge(6, 20)], [Edge(5, 20)]]
    >>> dijkstra(graph, 0)
    [0, 50, 10, 90, 140, 160]
    >>> dijkstra(graph, 1)
    [50, 0, 40, 100, 150, 170]
    >>> graph = [[Edge(2, 50)], [Edge(1, 50), Edge(3, 1000000000)], [Edge(2, 1000000000)]]
    >>> dijkstra(graph, 0)
    [0, 50, 1000000050]
    """
    nodes_number = len(graph)
    visited = [False] * nodes_number
    infinity = 10 ** 15
    distances = [infinity] * nodes_number
    distances[start_node] = 0
    priority_queue = PriorityQueue()
    priority_queue.put((start_node, 0))
    while not priority_queue.empty():
        index, min_value = priority_queue.get()
        visited[index] = True
        # A neat optimization
        if distances[index] < min_value:
            continue
        for edge in graph[index]:
            if visited[edge.to - 1]:
                continue
            new_distance = distances[index] + edge.weight
            if new_distance < distances[edge.to - 1]:
                distances[edge.to - 1] = new_distance
                priority_queue.put((edge.to - 1, new_distance))
    return distances


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
