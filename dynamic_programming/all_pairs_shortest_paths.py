import sys

INF = sys.maxsize


def floyd_warshall(graph, v):
    """
        The Floyd Warshall Algorithm is for solving the All Pairs Shortest Path problem. 
        The problem is to find shortest distances between every pair of vertices in a given edge 
        weighted directed Graph. 
        
        We initialize the solution matrix same as the input graph matrix as a first step. 
        Then we update the solution matrix by considering all vertices as an intermediate vertex. 
        The idea is to one by one pick all vertices and update all shortest paths which include the picked 
        vertex as an intermediate vertex in the shortest path. When we pick vertex number k as an intermediate vertex,
        we already have considered vertices {0, 1, 2, .. k-1} as intermediate vertices. For every pair (i, j) 
        of source and destination vertices respectively, there are two possible cases.
        
        1) k is not an intermediate vertex in shortest path from i to j. We keep the value of dist[i][j] as it is.
        2) k is an intermediate vertex in shortest path from i to j. 
           We update the value of dist[i][j] as dist[i][k] + dist[k][j]. 
        
    :param graph: weighted graph
    :param v: number of vertices
    :return: None
    """

    # dist[][] will be the output matrix that will finally
    # have the shortest distances between every pair of vertices
    # initializing the solution matrix same as input graph matrix
    # OR we can say that the initial values of shortest distances
    # are based on shortest paths considering no
    # intermediate vertices
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

    # for all intermediate nodes
    for k in range(v):
        # pick all vertices as source one by one
        for i in range(v):
            # pick all vertices as target one by one
            for j in range(v):
                # if vertex k is on shortest path from i to j (i, j)
                # then update the value of dist(i, j)
                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])

    # let's print the shortest distances between every pair of vertices
    for i in range(v):
        for j in range(v):
            if dist[i][j] == INF:
                print("{:>7s}".format("INF"), end="")
            else:
                print("{:>7d}\t".format(dist[i][j]), end="")
            if j == v - 1:
                print()


if __name__ == '__main__':
    """
            Weighted graph
            
                10
           (0)------->(3)
            |         /|\
          5 |          |
            |          | 1
           \|/         |
           (1)------->(2)
                3           """

    graph = [
              [0,   5,   INF, 10],
              [INF, 0,   3,   INF],
              [INF, INF, 0,   1],
              [INF, INF, INF, 0]
            ]
    floyd_warshall(graph, 4)
