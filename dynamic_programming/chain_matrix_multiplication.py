import sys


def chain_matrix_multiplication(p):
    """
        Given a sequence of matrices, find the most efficient way to multiply these matrices together. 
        The problem is not actually to perform the multiplications, but merely to decide in which order to 
        perform the multiplications.
        
        We have many options to multiply a chain of matrices because matrix multiplication is associative. 
        In other words, no matter how we parenthesize the product, the result will be the same. 
        For example, if we had four matrices A, B, C, and D, we would have:
        
            (ABC)D = (AB)(CD) = A(BCD) = ....
        
        However, the order in which we parenthesize the product affects the number of simple arithmetic 
        operations needed to compute the product, or the efficiency. For example, suppose A is a 10 × 30 matrix, 
        B is a 30 × 5 matrix, and C is a 5 × 60 matrix. Then,
        
            (AB)C = (10×30×5) + (10×5×60) = 1500 + 3000 = 4500 operations
            A(BC) = (30×5×60) + (10×30×60) = 9000 + 18000 = 27000 operations.
    
    :param: an array p[] which represents the chain of matrices such that the ith matrix Ai is of dimension p[i-1] x p[i]
    :return: total optimal cost of matrix multiplication
    """

    n = len(p)
    cost_table = [[None] * n for i in range(n)]

    # base case
    # when i = j, there's nothing to multiply, so cost(i, i) = 0
    for i in range(1, n):
        cost_table[i][i] = 0

    # build cost table in bottom-up manner
    # s denotes the sub-problem size
    for s in range(1, n - 1):
        for i in range(1, n - s):
            j = i + s
            cost = sys.maxsize
            for k in range(i, j):
                cost = min(cost, cost_table[i][k] + cost_table[k + 1][j] + p[i - 1] * p[k] * p[j])
            cost_table[i][j] = cost

    return cost_table[1][n - 1]


if __name__ == '__main__':
    p = [50, 20, 1, 10, 100]

    print(chain_matrix_multiplication(p))
