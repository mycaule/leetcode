# Leetcode 674

# pylint: disable-all

def max_subseq_length(arr) -> int:
    result = 0
    anchor = 0

    for i in range(len(arr)):
        if i>0 and arr[i-1] >= arr[i]:
            anchor = i

        result = max(result, i-anchor+1)

    return result


print(max_subseq_length([1]))              # 1
print(max_subseq_length([1, 3, 5, 4, 7]))  # 3
print(max_subseq_length([2, 2, 2, 2, 2]))  # 1
