
N = 3  # Number of steps


def safe_probability(x, y, n, dp):
    """
    Find the probability that a person is safe after taking `n` steps on an island

    An island is in the form of a square matrix, and a person is standing inside the matrix.
    The person can move one step in any direction (RIGHT, LEFT, TOP, DOWN) in the matrix (2D plane).
    Calculate the probability that the person is safe after walking n steps on the island,
    provided that he dies if he steps outside the plane.

    Examples:
    Input: 2 × 2 matrix
    The starting coordinates is (0, 0)
    The total number of steps is 1

    Output:The safe probability is 0.5


    Input: 3 × 3 matrix
    The starting coordinates is (1, 1)
    The total number of steps is 1

    Output:The safe probability is 1


    Input: 3 × 3 matrix
    The starting coordinates is (0, 0)
    The total number of steps is 3

    Output:The safe probability is 0.25

    The following solution assumes all steps carry equal probability, i.e., 1/4 or 0.25. It can easily be
    modified to handle unequal probabilities.

    We can easily solve this problem with Dynamic Programming. For given position (x, y) and remaining
    steps n, the main problem can easily be divided into subproblems:

    Prob(x,y,n) = (Prob(x - 1,y,n - 1) + Prob(x + 1,y,n - 1) + Prob(x,y - 1,n - 1) + Prob(x, y + 1, n - 1)) / 4

    Time Complexity: O(N * N)
    Space Complexity: O(N * N)

    :param x: coordinates
    :param y: coordinates
    :return: probability if person is safe

    Reference: https://www.techiedelight.com/probability-alive-after-taking-n-steps-island/
    """

    # Base case
    if n == 0:
        return 1.0

    # calculate unique key from current coordinates `(x, y)` of person
    # and number of steps(n) left
    key = (x, y, n)

    # if the subproblem is seen for the first time
    if key not in dp:

        p = 0.0

        # move one step up
        if x > 0:
            p += 0.25 * safe_probability(x - 1, y, n - 1, dp)

        # move one step down
        if x < N - 1:
            p += 0.25 * safe_probability(x + 1, y, n - 1, dp)

        # move one step left
        if y > 0:
            p += 0.25 * safe_probability(x, y - 1, n - 1, dp)

        # move one step right
        if y < N - 1:
            p += 0.25 * safe_probability(x, y + 1, n - 1, dp)

        dp[key] = p

    return dp[key]


if __name__ == '__main__':

    x, y = 0, 0
    n = 3
    dp = {}

    print(safe_probability(x, y, n, dp))
