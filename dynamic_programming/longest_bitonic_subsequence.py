def lbs(arr):
    """
    Given an array arr[0 … n-1] containing n positive integers, a subsequence of arr[] is called Bitonic
    if it is first increasing, then decreasing. Write a function that takes an array as argument and returns the length
    of the longest bitonic subsequence.
    A sequence, sorted in increasing order is considered Bitonic with the decreasing part as empty.
    Similarly, decreasing order sequence is considered Bitonic with the increasing part as empty.
    Examples:

    Input arr[] = {1, 11, 2, 10, 4, 5, 2, 1};
    Output: 6 (A Longest Bitonic Subsequence of length 6 is 1, 2, 10, 4, 2, 1)

    Input arr[] = {12, 11, 40, 5, 3, 1}
    Output: 5 (A Longest Bitonic Subsequence of length 5 is 12, 11, 5, 3, 1)

    Input arr[] = {80, 60, 30, 40, 20, 10}
    Output: 5 (A Longest Bitonic Subsequence of length 5 is 80, 60, 30, 20, 10)


    Approach:
    This problem is a variation of standard Longest Increasing Subsequence (LIS) problem.
    Let the input array be arr[] of length n. We need to construct two arrays lis[] and lds[]
    using Dynamic Programming solution of LIS problem.
    lis[i] stores the length of the Longest Increasing subsequence ending with arr[i].
    lds[i] stores the length of the longest Decreasing subsequence starting from arr[i].
    Finally, we need to return the max value of lis[i] + lds[i] – 1 where i is from 0 to n-1.

    :return: size of longest bitonic subsequence
    """
    n = len(arr)
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    lds = [1] * n

    # Compute LDS values from right to left
    for i in reversed(range(n - 1)):  # loop from n-2 down to 0
        for j in reversed(range(i - 1, n)):  # loop from n-1 down to i-1
            if arr[i] > arr[j] and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1

    maximum = lis[0] + lds[0] - 1
    for i in range(n):
        maximum = max(maximum, lis[i] + lds[i] - 1)

    return maximum


if __name__ == '__main__':
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print("Length of longest bitonic subsequence is " + str(lbs(arr)))
