# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot:
            return False
        if not subRoot:
            return True
        if self.same(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def same(self, p, q):
        if not p and q or not q and p:
            return False
        elif not p and not q:
            return True
        else:
            if p.val!=q.val:
                return False
            else:
                return self.same(p.left, q.left) and self.same(p.right, q.right)
        