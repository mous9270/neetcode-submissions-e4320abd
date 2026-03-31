# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if min(p.val, q.val)<=root.val<=max(q.val,p.val):
            return root
        elif p.val<=root.val and q.val<=root.val:
            if root.left:
                return self.lowestCommonAncestor(root.left, p, q)
        else:
            if root.right:
                return self.lowestCommonAncestor(root.right, p, q)