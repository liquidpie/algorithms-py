def max_profit_activity_selection(activity, n):
    """
    Also known as Weighted Job Scheduling

    Given N jobs where every job is represented by following three elements of it.

    Start Time
    Finish Time
    Profit or Value Associated (>= 0)

    Find the maximum profit subset of jobs such that no two jobs in the subset overlap.

    Example:

        Input: Number of Jobs n = 4
               Job Details [Start Time, Finish Time, Profit]
               Job 1:  [1, 2, 50]
               Job 2:  [3, 5, 20]
               Job 3:  [6, 19, 100]
               Job 4:  [2, 100, 200]
        Output: The maximum profit is 250.
        We can get the maximum profit by scheduling jobs 1 and 4.
        Note that there is longer schedules possible Jobs 1, 2 and 3
        but the profit with this schedule is 20+50+100 which is less than 250.

    The Greedy Strategy for activity selection doesn’t work here as a schedule with more jobs may have smaller profit or value.

    Approach:

        1) First sort jobs according to finish time.
        2) Now apply following recursive process.
           // Here arr[] is array of n jobs
           findMaximumProfit(arr[], n)
           {
             a) if (n == 1) return arr[0];
             b) Return the maximum of following two profits.
                 (i) Maximum profit by excluding current job, i.e.,
                     findMaximumProfit(arr, n-1)
                 (ii) Maximum profit by including the current job
           }

        How to find the profit including current job?
        The idea is to find the latest job before the current job (in
        sorted array) that doesn't conflict with current job 'arr[n-1]'.
        Once we find such a job, we recur for all jobs till that job and
        add profit of current job to result.
        In the above example, "job 1" is the latest non-conflicting
        for "job 4" and "job 2" is the latest non-conflicting for "job 3".

    Time Complexity of the above Dynamic Programming Solution is O(n2).
    Note that the this solution can be optimized to O(nLogn) using Binary Search in _get_previous_non_conflicting() instead of linear search.

    Reference:
        https://www.geeksforgeeks.org/weighted-job-scheduling
        https://www.geeksforgeeks.org/weighted-job-scheduling-log-n-time

    :return: the optimal profit
    """
    # Sort jobs according to their finish time
    activity.sort(key=lambda x: x[1])

    # Create an array to store solutions of subproblems. dp[i] stores the profit for jobs till arr[i] (including arr[i])
    dp = [0 for _ in range(n)]
    dp[0] = activity[0][2]

    for i in range(n):
        included_profit = activity[i][2]
        idx = _get_previous_non_conflicting(activity, i)
        included_profit += dp[idx] if idx != -1 else 0
        dp[i] = max(included_profit, dp[i - 1])

    return dp[n - 1]


def _get_previous_non_conflicting(activity, i):
    """
        Find the previous job (in sorted array) that doesn't conflict with the job[i]
    """
    for j in range(i - 1, -1, -1):
        if activity[i][0] >= activity[j][1]:
            return j
    return -1


def _get_previous_non_conflicting_binary_search(activity, i):
    low = 0
    high = i - 1

    while low <= high:
        mid = (low + high) // 2

        if activity[mid][1] <= activity[i][0]:
            if activity[mid + 1][1] <= activity[i][0]:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    return -1


if __name__ == '__main__':
    activity = [[3, 10, 20], [1, 2, 50], [6, 19, 100], [2, 100, 200]]
    result = max_profit_activity_selection(activity, len(activity))
    print("The optimal profit is " + str(result))
