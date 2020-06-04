# Leetcode 017

mappings = {
    "2": ['a', 'b', 'c'],
    "3": ['d', 'e', 'f'],
    "4": ['g', 'h', 'i'],
    "5": ['j', 'k', 'l'],
    "6": ['m', 'n', 'o'],
    "7": ['p', 'q', 'r'],
    "8": ['t', 'u', 'v'],
    "9": ['w', 'x', 'y', 'z']
}

def letter_combinations(str):
    if len(str) == 0:
        return ['']
    else:
        return [c+s 
            for c in mappings[str[0]] 
            for s in letter_combinations(str[1:])
        ]
s1 = "23"
s2 = "233"

print(letter_combinations(s1))
# ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

print(letter_combinations(s2))
