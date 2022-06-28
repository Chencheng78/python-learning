import os, sys

def solve_coin_change(coins, value):
    """A dynamic solution to the coin change problem"""

    table = [None for x in range(value + 1)]
    table[0] = []
    for i in range(1, value + 1):
        for coin in coins:
            if coin > i: continue
            elif not table[i] or len(table[i - coin]) + 1 < len(table[i]):
                if table[i - coin] != None:
                    table[i] = table[i - coin][:]
                    table[i].append(coin)

    if table[-1] != None:
        print( '%d coins: %s' % (len(table[-1]), table))
    else:
        print('No solution possible')

print(solve_coin_change([1,5],10))