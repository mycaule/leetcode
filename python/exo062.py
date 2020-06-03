# Leetcode 062

# pylint: disable-all


def unique_paths(m, n):
    """
    O(MxN) time, O(MxN) space
    """
    mat = [[1 for i in range(n)] for j in range(m)]

    for i in range(1,m):
        for j in range(1,n):
            mat[i][j] = mat[i-1][j] + mat[i][j-1]

    return mat

print(unique_paths(3, 4)[2][3])
