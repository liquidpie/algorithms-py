# Returns length of longest common
# substring of X[0..m-1] and Y[0..n-1]


def longest_common_substring(x, y, m, n):

    """
    Create a table to store lengths of
    longest common suffixes of substrings. 
    Note that LCSuff[i][j] contains the 
    length of longest common suffix of 
    X[0...i-1] and Y[0...j-1]. The first
    row and first column entries have no
    logical meaning, they are used only
    for simplicity of the program.

    LCSuff is the table with zero 
    value initially in each cell
    
    :param x: 
    :param y: 
    :param m: 
    :param n: 
    :return: 
    """

    lc_suff = [[0 for k in range(n + 1)] for l in range(m + 1)]

    # To store the length of 
    # longest common substring
    result = 0

    # Following steps to build
    # LCSuff[m+1][n+1] in bottom up fashion
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lc_suff[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                lc_suff[i][j] = lc_suff[i - 1][j - 1] + 1
                result = max(result, lc_suff[i][j])
            else:
                lc_suff[i][j] = 0
    return result
