# Leetcode 104

# pylint: disable-all

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def height(self):
        if p is None:
            return 0
        else:
            return 1 + max(p.left.height(), p.right.height())


p = TreeNode(3)
p.left = TreeNode(9)
p.right = TreeNode(20)
p.right.left = TreeNode(15)
p.right.right = TreeNode(7)

print(p.height())
