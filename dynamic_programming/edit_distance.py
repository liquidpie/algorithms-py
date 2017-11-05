def edit_distance(str1, str2):
    """
        Find minimum number of editsinsertions, deletions, and substitutions 
        of charactersneeded to transform the first string into the second
        
        Edit distance is also known as Lavenstein distance
        
        Overall running time of algorithm is O(mn)
        
    :param str1: First String 
    :param str2: Second String
    :return: total edit distance
    """

    m = len(str1)
    n = len(str2)

    # Edit Distance matrix
    ed_matrix = [[0] * n for i in range(m)]

    # Base cases

    # 1. when str2 is empty
    for i in range(0, m):
        ed_matrix[i][0] = i

    # 2. when str1 is empty
    for j in range(1, n):
        ed_matrix[0][j] = j

    # solve for remaining cases
    for i in range(1, m):
        for j in range(1, n):
            ed_matrix[i][j] = min(1 + ed_matrix[i - 1][j], 1 + ed_matrix[i][j - 1], diff(str1[i], str2[j]) + ed_matrix[i - 1][j - 1])

    return ed_matrix[m - 1][n - 1]


def diff(char1, char2):
    return 0 if char1 == char2 else 1


if __name__ == '__main__':

    print(edit_distance("EXPONENTIAL", "POLYNOMIAL"))
    print(edit_distance("SNOWY", "SUNNY"))