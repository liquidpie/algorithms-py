'''
Minimum Number of Platforms Required for a Railway/Bus Station

Given arrival and departure times of all trains that reach a railway station, find the minimum number of platforms required for the railway station so that no train waits.
We are given two arrays which represent arrival and departure times of trains that stop

Examples:

Input:  arr[]  = {9:00,  9:40, 9:50,  11:00, 15:00, 18:00}
        dep[]  = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}
Output: 3
There are at-most three trains at a time (time between 11:00 to 11:20)

'''


def min_stations(arr, dep, n):
    arr.sort()
    dep.sort()

    i = 1
    j = 0
    result = 0
    stations_req = 1

    while i < n and j < n:

        if arr[i] <= dep[j]:
            stations_req += 1
            i += 1

            result = stations_req if result < stations_req else result

        else:
            stations_req -= 1
            j += 1

    return result


if __name__ == '__main__':
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    n = 6

    print(min_stations(arr, dep, n))