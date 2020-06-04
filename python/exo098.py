# Leetcode 098

# pylint: disable-all

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_valid_bst(p):
    if p.val is None:
        return True
    elif p.left is None and p.right is None:
        return True
    elif p.left is None:
        return p.val <= p.right.val and is_valid_bst(p.right)
    elif p.right is None:
        return p.left.val <= p.val and is_valid_bst(p.left)
    else:
        return p.left.val <= p.val and p.val <= p.right.val and is_valid_bst(p.left) and is_valid_bst(p.right)


p = TreeNode(2)
p.left = TreeNode(1)
p.right = TreeNode(3)

print(is_valid_bst(p))  # True

q = TreeNode(5)
q.left = TreeNode(1)
q.right = TreeNode(4)
q.right.left = TreeNode(3)
q.right.right = TreeNode(6)

print(is_valid_bst(q))  # False
