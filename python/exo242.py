# Leecode 242

# pylint: disable-all

from collections import Counter

def is_anagram(s, t):
    c = Counter(s)
    print(c)

    for x in t:
        c[x] -= 1

    print(c)

    return all([x == 0 for x in c.values()])

s = "anagram"
t = "nagaram"
print(is_anagram(s, t))  # True

s = "rat"
t = "car"
print(is_anagram(s, t))  # False
