def find_coins_greedy(amount: int) -> dict:
    items = {50: 0, 25: 0, 10: 0, 5: 0, 2: 0, 1: 0}
    for item in items:
        while amount >= item:
            amount -= item
            items[item] += 1
    return {k: v for k, v in items.items() if v > 0}


if __name__ == '__main__':
    print(find_coins_greedy(113))
