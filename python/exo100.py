# Leetcode 100

# pylint: disable-all

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_same_tree(p, q):
    if p is None and q is None:
        return True
    elif p is None:
        return False
    elif q is None:
        return False
    else:
        if p.val != q.val:
            return False
        else:
            return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

print(is_same_tree(p, q))  # True

q.left.val = None

print(is_same_tree(p, q))  # False
