def distinct_paths_bet_two_points(x1, y1, x2, y2):

    matrix = [[0 for y in range(y2 - y1 + 1)] for x in range(x2 - x1 + 1)]

    matrix[0][0] = 0

    for i in range(1, x2 - x1 + 1):
        matrix[i][0] = 1

    for i in range(1, y2 - y1 + 1):
        matrix[0][i] = 1

    for i in range(1, x2 - x1 + 1):
        for j in range(1, y2 - y1 + 1):
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

    return matrix[x2 - x1][y2 - y1]


if __name__ == '__main__':
    x1, y1 = (1, 2)
    x2, y2 = (7, 9)

    print("Number of distinct paths between points is", distinct_paths_bet_two_points(x1, y1, x2, y2))
