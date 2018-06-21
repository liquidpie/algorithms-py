'''
There is an integer array consisting positive numbers only. 
Find maximum possible sum of elements such that there are no 2 consecutive elements present in the sum.

Solution:

Suppose we know the max sum for all subarrays, how can it help us to solve the overall problem? Let’s use max_sum[i] denote the maximum sum for subarray arr[0…i]. If the last number arr[i] is included in the sum, max_sum[i] should equal to arr[i] + max_sum[i-2] (because arr[i-1] cannot be included). Similarly, if arr[i] isn’t included, then max_sum[i] should equal to arr[i-1].

Therefore, we have the following formula:

    max_sum[i] = MAX(arr[i] + max_sum[i-2], max_sum[i-1])
'''


def max_sum(arr, n):

    sum = [0 for i in range(n)]

    sum[-1] = 0
    sum[0] = arr[0]

    for i in range(1, n):
        sum[i] = max(sum[i - 1], sum[i - 2] + arr[i])

    return sum[n - 1]


if __name__ == '__main__':
    arr = [6, 4, 2, 8, 1]
    n = 5
    print(max_sum(arr, n))

