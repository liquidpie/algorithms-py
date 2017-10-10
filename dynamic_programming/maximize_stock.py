def maximize_profit(arr):

    # find local maxima and then subtract all the purchases from it

    profit = 0
    max_so_far = 0
    for i in reversed(arr):
        if i >= max_so_far:
            max_so_far = i
        profit += max_so_far - i
    return profit


if __name__ == "__main__":
    arr = [1, 3, 2, 1]
    print(maximize_profit(arr))