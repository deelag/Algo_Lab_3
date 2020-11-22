from queue import PriorityQueue


def unity_clients_routers(clients, routers):
    nodes_number = len(clients) + len(routers)
    nodes = []
    for i in range(nodes_number):
        if len(clients) > 0:
            if i == clients[0]:
                nodes.append(0)
                clients.remove(clients[0])
        if len(routers) > 0:
            if i == routers[0]:
                nodes.append(1)
                routers.remove(routers[0])
    return nodes


def find_min_latency(graph, clients, routers):
    nodes = unity_clients_routers(clients, routers)
    max_values = []
    for i in range(len(nodes)):
        client_distances = []
        if nodes[i] == 1:
            client_distances.append(dijkstra(graph, i))
        if nodes[i] == 0:
            client_distances.pop(i)
        max_values.append(max(client_distances))
    return min(max_values)


# def find_min_latency(graph, clients, routers):
#     max_values = []
#
#     for router in routers:
#         client_distances = []
#         for client in clients:
#             client_distances.append(dijkstra(graph, router).pop(client))
#         max_values.append(max(client_distances))
#     return min(max_values)


def dijkstra(graph, start_node):
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
