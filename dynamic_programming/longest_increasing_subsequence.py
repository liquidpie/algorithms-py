def lis(arr):
    """
        The Longest Increasing Subsequence (LIS) problem is to find the length of the longest 
        subsequence of a given sequence such that all elements of the subsequence are sorted 
        in increasing order. For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} 
        is 6 and LIS is {10, 22, 33, 50, 60, 80}.
        
        This algorithm runs in O(n ^ 2) time complexity
        
    :param arr: input array
    :return: count of LIS
    """
    n = len(arr)
    lis = [1] * n # length of the LIS ending at index i

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1 :
                lis[i] = lis[j] + 1

    # maximum of all LIS values
    maximum = 0

    # pick maximum of all LIS values
    for i in range(n):
        maximum = max(maximum, lis[i])

    return maximum


def lis_efficient(arr):
    # this algorithm runs in O(nlog n) time complexity
    # https://stackoverflow.com/questions/2631726/how-to-determine-the-longest-increasing-subsequence-using-dynamic-programming

    n = len(arr)
    # Let S[pos] be defined as the smallest integer that ends an increasing sequence of length pos.
    # To make things simpler, we can keep in the array S, not the actual integers,
    # but their indices(positions) in the set
    s = []

    for i in range(n):
        # If X > last element in S, then append X to the end of S.
        # This essentialy means we have found a new largest LIS.
        if not s:
            s.append(arr[i])
        elif arr[i] > s[-1]:
            s.append(arr[i])
        # Otherwise find the smallest element in S, which is >= than X,
        # and change it to X. Because S is sorted at any time, the element can be found using binary search in log(N)
        else:
            k = binary_search(s, arr[i])
            s[k] = arr[i]

    # length of s is the lis
    return len(s)


def binary_search(arr, item):

    beg = 0
    end = len(arr) - 1

    while beg < end:
        mid = int((beg + end) / 2)
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            beg = mid + 1
        else:
            end = mid

    return end

if __name__ == '__main__':
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]

    print(lis(arr))
    print(lis_efficient(arr))