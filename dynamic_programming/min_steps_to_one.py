"""
Given a positive integer - num, Following is a list of possible operations which can be performed on it:
1. num / 2, If number is divisible by 2
2. num / 3, If number is divisible by 3
3. num - 1

With these 3 available operations, find out the minimum number of steps required to reduce the number to 1.
"""


def min_steps(n):
    dp = [0 for x in range(n + 1)]

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1

        if i % 2 == 0:
            dp[i] = min(1 + dp[i // 2], dp[i])

        if i % 3 == 0:
            dp[i] = min(1 + dp[i // 3], dp[i])

    return dp[n]


if __name__ == '__main__':
    print(min_steps(10))