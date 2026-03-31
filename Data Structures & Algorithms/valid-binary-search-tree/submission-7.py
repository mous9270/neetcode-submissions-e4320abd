# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if self.valid(root, float('-inf'), float('inf')):
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        else:
            return False
    def valid(self, node, l, r):
        if not node:
            return True
        else:
            if l<node.val<r:
                return self.valid(node.left, l, node.val) and self.valid(node.right, node.val, r)
            else:
                return False