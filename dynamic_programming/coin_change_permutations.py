"""
Given a value N, if we want to make change for N cents, 
and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins,
how many ways can we make the change? The order of coins doesn’t matter.

For example, 
For N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. 
So output should be 4. 
For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. 
So output should be 5.

To count the total number of solutions, we can divide all set solutions into two sets.
1) Solutions that do not contain mth coin (or Sm).
2) Solutions that contain at least one Sm.

Let count(S[], m, n) be the function to count the number of solutions, 
then it can be written as sum of count(S[], m-1, n) and count(S[], m, n-Sm).

where m is the size of coin set.
"""


def coin_change(coin_set, m, sum):
    # We need n+1 rows as the table is constructed
    # in bottom up manner using the base case 0 value
    # case (n = 0)
    table = [[0 for x in range(m)] for y in range(sum + 1)]

    # Fill the entries for 0 value case (n = 0)
    for i in range(m):
        table[0][i] = 1

    # Fill rest of the table entries in bottom up manner
    for i in range(1, sum + 1):
        for j in range(m):
            # Count of solutions including S[j]
            x = table[i - coin_set[j]][j] if i - coin_set[j] >= 0 else 0
            # Count of solutions excluding S[j]
            y = table[i][j - 1] if j >= 1 else 0
            # total count
            table[i][j] = x + y

    return table[sum][m - 1]


def coin_change_recursive(coin_set, m, sum):

    # If n is 0 then there is 1
    # solution (do not include any coin)
    if sum == 0:
        return 1

    # If n is less than 0 then no
    # solution exists
    if sum < 0:
        return 0

    # If there are no coins and n
    # is greater than 0, then no
    # solution exist
    if m <= 0 and sum > 0:
        return 0

    # count is sum of solutions (i)
    # including S[m-1] (ii) excluding S[m-1]
    return coin_change_recursive(coin_set, m - 1, sum) + coin_change_recursive(coin_set, m, sum - coin_set[m - 1])


if __name__ == '__main__':
    coin_list = [1, 2, 3]
    m = len(coin_list)
    sum = 4
    print(coin_change(coin_list, m, sum))
