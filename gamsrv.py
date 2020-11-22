import copy

from dijkstra import find_min_latency
from edge import Edge

if __name__ == "__main__":
    with open("gamsrv.in", "r+") as fileIn:
        nodes_number, edges_number = fileIn.readline().split()
        clients = [int(x) - 1 for x in next(fileIn).split()]
        routers = [x for x in range(int(nodes_number))]
        for x in clients:
            routers.remove(x)

        graph = [[]] * int(nodes_number)
        for i in range(int(edges_number)):
            node_index, edge_to, weight = fileIn.readline().split()
            graph_inside = copy.deepcopy(graph[int(node_index) - 1])
            graph_inside.append(Edge(int(edge_to), int(weight)))
            graph[int(node_index) - 1] = graph_inside
            graph_inside_2 = copy.deepcopy(graph[int(edge_to) - 1])
            graph_inside_2.append(Edge(int(node_index), int(weight)))
            graph[int(edge_to) - 1] = graph_inside_2

    with open("gamsrv.out", "w+") as fileOut:
        fileOut.write("%d" % find_min_latency(graph, clients, routers))
