# Leetcode 112

# pylint: disable-all

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def has_path_sum(self, v):
        d = v - self.val
        # print(self.val, d)
       
        if d < 0:
            return False
        elif self.left is None and self.right is None:
            return d == 0
        elif self.left is None:
            return self.right.has_path_sum(d)
        elif self.right is None:
            return self.left.has_path_sum(d) 
        else:
            return self.left.has_path_sum(d) or self.right.has_path_sum(d)

#
#        5
#       / \
#      4   8
#     /   / \
#    11  13  4
#   /  \      \
#  7    2      1
#

p = TreeNode(5)
p.left = TreeNode(4)
p.left.left = TreeNode(11)
p.left.left.left = TreeNode(7)
p.left.left.right = TreeNode(2)

p.right = TreeNode(8)
p.right.left = TreeNode(13)
p.right.right = TreeNode(4)
p.right.right.right = TreeNode(1)

print(p.has_path_sum(22))   # True: 5-4-11-2
print(p.has_path_sum(12))   # False

