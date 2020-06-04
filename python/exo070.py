# Leetcode 070

# pylint: disable-all

def climb_stairs(n):
    """
        Fibonacci like, use classical algorithms to improve more
    """
    if n == 0:
        return 0
    elif n == 1:
        # 1 = 1  (only one solution)
        return 1
    elif n == 2:
        # 2 = 1 + 1 or 2 = 2 (two solutions)
        return 2
    else:
        # n = 1 + (n-1) or 2 + (n-2)
        return climb_stairs(n-1) + climb_stairs(n-2)

print(climb_stairs(2))  # 2

print(climb_stairs(3))  # 3
