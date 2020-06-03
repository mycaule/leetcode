# Leetcode 019

# pylint: disable-all

def remove_end(l, n):
    del l[-n]
    return l


l = [1, 2, 3, 4, 5]
print(l)
print(remove_end(l, 2))   # [1, 2, 3, 5]
