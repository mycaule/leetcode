# Leetcode 200

# pylint: disable-all

def sink(arr, i, j):
    if not(0 <= i and i < len(arr) and 0 <=j and j < len(arr[0])):
        return 0

    if arr[i][j] == 1:
        arr[i][j] = 0
        sink(arr, i-1, j)
        sink(arr, i+1, j)
        sink(arr, i, j-1)
        sink(arr, i, j+1)
        return 1
    else:
        return 0


def num_islands(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            count += sink(arr, i, j)

    return count


arr = [[1,1,1,1,0],
       [1,1,0,1,0],
       [1,1,0,0,0],
       [1,1,0,0,0],
       [0,0,0,0,0]]
print(num_islands(arr))  # 1

arr = [[1,1,0,0,0],
       [1,1,0,0,0],
       [0,0,1,0,0],
       [0,0,1,0,0],
       [0,0,0,1,1]]
print(num_islands(arr))  # 3

arr = [[1,1,1],
       [0,1,0],
       [1,1,1]]
print(num_islands(arr))  # 1
