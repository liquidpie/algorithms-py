def count_ways(n):
    """
        Given N, count the number of ways to express N as sum of 1, 3 and 4.

        Examples:
            Input :  N = 4
            Output : 4
            Explanation: 1+1+1+1
                         1+3
                         3+1
                         4

            Input : N = 5
            Output : 6
            Explanation: 1 + 1 + 1 + 1 + 1
                         1 + 4
                         4 + 1
                         1 + 1 + 3
                         1 + 3 + 1
                         3 + 1 + 1

    :return: number of ways n can be expressed as 1, 3 and 4

    Time Complexity : O(n)
    Space Complexity : O(n)

    Reference: https://www.geeksforgeeks.org/count-ofdifferent-ways-express-n-sum-1-3-4/
    """

    DP = [0 for i in range(0, n + 1)]

    # Base Cases
    DP[0] = 1
    DP[1] = 1
    DP[2] = 1
    DP[3] = 2

    for i in range(4, n + 1):
        DP[i] = DP[i - 1] + DP[i - 3] + DP[i - 4]

    return DP[n]


if __name__ == '__main__':
    print(count_ways(10))
