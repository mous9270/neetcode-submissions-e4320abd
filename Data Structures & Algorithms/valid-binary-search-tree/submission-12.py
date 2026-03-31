# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, float('-inf'), float('inf'))
    
    def valid(self, root, p, q):
        if not root:
            return True
        if p<root.val<q:
            return self.valid(root.left, p, root.val) and self.valid(root.right, root.val, q)
        else:
            return False