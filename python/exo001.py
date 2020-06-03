# LeetCode 001
# pylint: disable-all


def pair_brute_force(arr, p):
    """
     Brute force method
     O(N^2) in time, O(1) in space
    """
    n = len(arr)
    for i in range(0, n):
        for j in range(i, n):
            if arr[i] + arr[j] == p:
                return (i, j)


def pair_hashmap(arr, p):
    """
    Using hashmap to store compliments
    O(N) in time, O(N) in space
    """
    t = {}
    n = len(arr)

    for i in range(0, n):
        if arr[i] in t:
            return (t[arr[i]], i)
        else:
            t[p-arr[i]] = i


p = 26
arr = [2, 15, 11, 7]

print(p)
print(arr)
print(pair_brute_force(arr, p))
print(pair_hashmap(arr, p))
