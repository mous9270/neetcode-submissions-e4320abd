# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, float('-inf'), float('inf'))

    def valid(self, node, p, q):
        if not node:
            return True
        if p<node.val<q:
            return self.valid(node.left, p, node.val) and self.valid(node.right, node.val, q)
        else:
            return False