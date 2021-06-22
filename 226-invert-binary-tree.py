# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        if root is None:
            return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        #swap
        root.right = left
        root.left = right

        return root
        """
        if root is None:
            return root
        tmpLeftNode = root.left
        root.left = root.right
        root.right = tmpLeftNode

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root