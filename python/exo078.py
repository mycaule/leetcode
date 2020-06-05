# Leetcode 78

# pylint: disable-all

a = [1, 2, 3, 4, 5]
n = len(a)

for i in range(2**n):
    v = [c == '1' for c in format(i, '0%sb' % n)]
    b = [x for (x, y) in zip(a, v) if y]
    print(b)

