def min_cost_path(matrix, m, n):
    """
        Given a cost matrix cost[][] and a position (m, n) in cost[][], 
        write a function that returns cost of minimum cost path to reach (m, n) from (0, 0).
        Each cell of the matrix represents a cost to traverse through that cell.
        Total cost of a path to reach (m, n) is sum of all the costs on that path (including both source and destination).
        You can only traverse down, right and diagonally lower cells from a given cell, i.e., 
        from a given cell (i, j), cells (i+1, j), (i, j+1) and (i+1, j+1) can be traversed.
        You may assume that all costs are positive integers.
    :param matrix: input matrix
    :param m: row dimension
    :param n: col dimension
    :return: min cost
    """
    total_cost = [[0 for x in range(m)] for y in range(n)]

    total_cost[0][0] = matrix[0][0]

    # Initialize first column of total_cost array
    for i in range(1, m):
        total_cost[i][0] = total_cost[i - 1][0] + matrix[i][0]

    # Initialize first row of total_cost array
    for j in range(1, n):
        total_cost[0][j] = total_cost[0][j - 1] + matrix[0][j]

    # construct rest of total_cost array
    for i in range(1, m):
        for j in range(1, n):
            total_cost[i][j] = min(total_cost[i - 1][j - 1],
                                   total_cost[i - 1][j],
                                   total_cost[i][j - 1]) + matrix[i][j]

    return total_cost[m - 1][n - 1]


if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [4, 8, 2],
              [1, 5, 3]]

    print(min_cost_path(matrix, 3, 3))
