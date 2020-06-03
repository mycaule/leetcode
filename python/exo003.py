# Leetcode 003
# pylint: disable-all


def bruteforce_longest_substring(arr) -> int:
    print(arr)
    result = []
    start = 0
    cursor = 0
    maxlen = 0

    for start in range(0, len(arr)):
        seen = set(arr[start])
        for i in range(start +1, len(arr)):
            if arr[i] not in seen:
                cursor = i
                seen.add(arr[i])
            else:   
                length = cursor-start+1
                maxlen = max(length, maxlen)
                break

    return maxlen


def dynamic_longest_substring(arr) -> int:
    print(arr)

    chars = {}
    start = 0
    maxlen = 0

    for i, letter in enumerate(arr):
        if letter in chars and chars[letter] >= start:
            start = chars[letter]+1
            length = i-start+1
            maxlen = max(maxlen, length)
            chars[letter] = i
        else:
            chars[letter] = i
            
    return maxlen



arr = "abcabcbb"
print(bruteforce_longest_substring("abcabcbb"))  # abc -> 3
print(bruteforce_longest_substring("bbbbb"))     # b -> 1
print(bruteforce_longest_substring("pwwkew"))    # wke -> 3

print(dynamic_longest_substring("abcabcbb"))     # 3
print(dynamic_longest_substring("bbbbb"))
print(dynamic_longest_substring("pwwkew"))       # 3
