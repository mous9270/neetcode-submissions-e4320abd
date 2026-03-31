# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, float('-inf'), float('inf'))
    def isValid(self, root, l, r):
        if not root:
            return True
        if l<root.val<r:
            return self.isValid(root.left, l, root.val) and self.isValid(root.right, root.val, r)
        else:
            return False
        