# Leetcode 021

# pylint: disable-all

def merge(a, b):
    """
        We suppose that l1 an l2 are ordered
    """
    c = []
    
    N = len(a)
    M = len(b)
    i = 0
    j = 0

    while i < N or j < M :
        if j == M:
            c.append(a[i])
            i += 1
        elif i == N:
            c.append(b[j])
            j += 1
        elif a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    return c


l1 = [1, 3, 4]
l2 = [1, 2, 4]

print(l1)
print(l2)
print(merge(l1, l2))
