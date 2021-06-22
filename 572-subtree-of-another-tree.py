# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):

        if s is None:
            return False
        elif self.isMatch(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isMatch(self, s, t):
        if s is None or t is None:
            return s is None and t is None
        elif s.val == t.val:
            return self.isMatch(s.left, t.left) and self.isMatch(s.right, t.right)
        else:
            return False