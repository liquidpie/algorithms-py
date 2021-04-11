import sys

INF = sys.maxsize
V = 4  # number of vertices


def shortest_path(graph, u, v, k):
    """
        Suppose then that we are given a graph G with lengths on the edges, along with two nodes
        s and t and an integer k, and we want the shortest path from s to t that uses exactly k edges.
        Is there a quick way to adapt Dijkstra's algorithm to this new task? Not quite: that
        algorithm focuses on the length of each shortest path without remembering the number of
        hops in the path, which is now a crucial piece of information.

        Time complexity of the this solution is O(V^3 * K)

        Another DP approach: https://www.geeksforgeeks.org/shortest-path-with-exactly-k-edges-in-a-directed-and-weighted-graph-set-2/

    """

    # DP Table
    # THe value sp[i][j][e] will store weight of the shortest path from i to j with exactly k edges
    sp = [[None] * V for i in range(V)]
    for i in range(V):
        for j in range(V):
            sp[i][j] = [None] * (k + 1)

    # Loop for number of edges from 0 to k
    for e in range(k + 1):
        for i in range(V):  # source vertex
            for j in range(V):  # destination vertex

                # initialize
                sp[i][j][e] = INF

                # base cases
                if e == 0 and i == j:
                    sp[i][j][e] = 0
                if e == 1 and graph[i][j] != INF:
                    sp[i][j][e] = graph[i][j]

                # go to adjacent only when number
                # of edges is more than 1
                if e > 1:
                    for a in range(V):
                        # There should be an edge from
                        # i to a and a should not be
                        # same as either i or j
                        if graph[i][a] != INF and i != a and j != a and sp[a][j][e - 1] != INF:
                            sp[i][j][e] = min(sp[i][j][e], graph[i][a] + sp[a][j][e - 1])

    return sp[u][v][k]


if __name__ == '__main__':
    graph = [
        [0, 10, 3, 2],
        [INF, 0, INF, 7],
        [INF, INF, 0, 6],
        [INF, INF, INF, 0]
    ]
    u = 0
    v = 3
    k = 2

    print(shortest_path(graph, u, v, k))

