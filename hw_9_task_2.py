def find_min_coins(amount):
    K = [0] + [float("inf")] * (amount + 1)
    W = [0] * (amount + 1)
    coins = {1: 0, 2: 0, 5: 0, 10: 0, 25: 0, 50: 0}

    for coin in coins:
        for i in range(coin, amount + 1):
            if K[i - coin] + 1 < K[i]:
                K[i] = K[i - coin] + 1
                W[i] = coin

    while amount > 0:
        coin = W[amount]
        coins[coin] += 1
        amount -= coin

    return {k: v for k, v in coins.items() if v > 0}


if __name__ == '__main__':
    print(find_min_coins(113))
