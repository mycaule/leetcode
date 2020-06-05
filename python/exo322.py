# Leetcode 322

# pylint: disable-all

def change(amount, coins):
    change = {}

    for coin in sorted(coins, reverse=True):
        change[coin] = int(amount/coin) 
        amount = amount % coin

    return sum(change.values())


print(change(11, [1, 2, 5]))  # 3
print(change(3, [2]))         # -1
