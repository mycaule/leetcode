# Leetcode 005
# pylint: disable-all

def longest_substring(s):
    """
    O(N^2) in time O(N) in space
    """
    print(s)
    palindromes1 = []
    palindromes2 = []

    for i in range(len(s)):
        palindromes1.append("")
        palindromes2.append(s[i])

        # i-delta < i < i+1+delta in odd symmetry
        delta = 0
        while 0 <= i-delta and i+1+delta < len(s) and s[i-delta] == s[i+1+delta]:
            palindromes1[i] = s[i-delta:i+2+delta]
            delta = delta + 1
        
        # i-delta < i+delta in even symmetry
        delta = 0
        while 0 <= i-delta and i+delta < len(s) and s[i-delta] == s[i+delta]:
            palindromes2[i] = s[i-delta:i+1+delta]
            delta = delta +1

    # Can only store the maximum palindrome to reduce space complexity to O(1)
    print(palindromes1)
    print(palindromes2)

    return max(palindromes1 + palindromes2, key=len)

s1 = "racecar"
s2 = "abbabbc"
s3 = "google"

print(longest_substring(s1))   # racecar
print(longest_substring(s2))   # bbabb
print(longest_substring(s3))   # goog
