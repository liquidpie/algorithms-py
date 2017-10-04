def coin_change(coin_value_list, change, min_coins, coins_used) :
    """
        
        count the minimum number of coins required for a change
    
    :param coin_value_list: coin denominations available
    :param change: amount for which coins to be dispenses
    :param min_coins: dict of minimum coins required for a change
    :param coins_used: coin denominations used to dispense particular change
    :return: count of minimum coins required for a change
    """
    for cents in range(change + 1) :

        coin_count = cents
        new_coin = 1

        for j in [c for c in coin_value_list if c <= cents] :
            if min_coins[cents - j] + 1 < coin_count :
                coin_count = min_coins[cents - j] + 1
                new_coin = j

        min_coins[cents] = coin_count
        coins_used[cents] = new_coin

    return min_coins[change]

def print_coins(coins_used, change) :
    coin = change
    while coin > 0 :
        print(coins_used[change], end=", ")
        coin = coin - coins_used[change]

if __name__ == '__main__' :
    coin_list = [1, 3, 5, 21, 25]
    change = 63
    min_coins = [0] * (change + 1)
    coins_used = [0] * (change + 1)

    print(coin_change(coin_list, change, min_coins, coins_used))

    print_coins(coins_used, change)
