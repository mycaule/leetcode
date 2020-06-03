# Leetcode 002
# pylint: disable-all


def add_stringify(l1, l2):
    """
    O(N) in time, O(N) in space
    """
    n1 = int(''.join(str(x) for x in l1)[::-1])
    n2 = int(''.join(str(x) for x in l2)[::-1])

    return [int(x) for x in str(n1 + n2)[::-1]]


def add_iterative(l1, l2):
    """
    O(N) in time, O(N) in space
    """
    carry = 0

    l3 = []
    for (i, v) in enumerate(l1):
        s = l1[i] + l2[i] + carry
        if s >= 10:
            l3.append(s-10)
            carry = 1
        else:
            l3.append(s)
            carry = 0

    return l3


def add_recursive(l1, l2, carry=0):
    """
    O(N) in time, O(N) in space
    """

    if (len(l1) == 0 and len(l2) == 0):
        return []

    s = l1[0] + l2[0] + carry

    if s >= 10:
        carry = 1
        return [s-10] + add_recursive(l1[1::], l2[1::], carry)
    else:
        carry = 0
        return [s] + add_recursive(l1[1::], l2[1::], carry)


l1 = [2, 4, 3]
l2 = [5, 6, 4]

print(l1)
print(l2)

print(add_stringify(l1, l2))
print(add_iterative(l1, l2))
print(add_recursive(l1, l2))


# Using basic linked list would require lightly modifying
# previous code using that structure


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val) + '->' + str(self.next)


p1 = ListNode(2)
p1.next = ListNode(4)
p1.next.next = ListNode(3)

print(p1)

print(p1.val)
p1 = p1.next
print(p1.val)
p1 = p1.next
print(p1.val)
p1 = p1.next
print(p1 is None)
