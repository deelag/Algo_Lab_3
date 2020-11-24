import copy

from dijkstra import find_min_latency, dijkstra
from edge import Edge

if __name__ == "__main__":
    with open("gamsrv.in", "r+") as fileIn:
        nodes_number, edges_number = fileIn.readline().split()
        clients = [int(x) - 1 for x in next(fileIn).split()]
        routers = [x for x in range(int(nodes_number))]
        for x in clients:
            routers.remove(x)

        graph = []
        for _ in range(int(nodes_number)):
            graph.append([])

        for i in range(int(edges_number)):
            node_index, edge_to, weight = fileIn.readline().split()
            graph[int(node_index) - 1].append(Edge(int(edge_to), int(weight)))
            graph[int(edge_to) - 1].append(Edge(int(node_index), int(weight)))

    with open("gamsrv.out", "w+") as fileOut:
        fileOut.write("%d" % find_min_latency(graph, clients, routers))
