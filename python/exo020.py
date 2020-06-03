# Leetcode 20
# pylint: disable-all


def is_valid(s):
    """
    O(N) in time, O(N) in space
    """
    print(s)
    mappings = {
        '}': '{',
        ')': '(',
        ']': '['
    }

    closings = mappings.keys()
    openings = mappings.values()

    stack = []
    for elt in s:
        if elt in openings:
            stack.append(elt)
        elif elt in closings:
            if stack.pop() != mappings[elt]:
                print("%s did not match corresponding bracket" % elt)
                return False
        else:
            return False

    return True


print(is_valid("{[)}"))    # False
print(is_valid("{[}]"))    # False
print(is_valid("{[]}"))    # True
