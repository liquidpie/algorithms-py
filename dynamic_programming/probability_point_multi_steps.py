def count_ways(n, p):
    """
    Probability of reaching a point with 2 or 3 steps at a time

    A person starts walking from position X = 0, find the probability to reach exactly on X = N if she can only take either 2 steps or 3 steps.
    Probability for step length 2 is given i.e. P, probability for step length 3 is 1 – P.

    Examples :

        Input : N = 5, P = 0.20
        Output : 0.32
        Explanation :-
        There are two ways to reach 5.
        2+3 with probability = 0.2 * 0.8 = 0.16
        3+2 with probability = 0.8 * 0.2 = 0.16
        So, total probability = 0.32.

    :param n: point to reach
    :param p: probability of step length 2
    :return: total probability of all the ways to reach point n
    """

    DP = [0.0 for i in range(n + 1)]

    # Base cases
    DP[0] = 1.0
    DP[1] = 0.0
    DP[2] = p
    DP[3] = 1 - p

    for i in range(4, n + 1):
        DP[i] = p * DP[i - 2] + (1 - p) * DP[i - 3]

    return DP[n]


if __name__ == '__main__':
    print(round(count_ways(5, 0.2), 2))
