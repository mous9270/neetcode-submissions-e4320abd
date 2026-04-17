# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i=0
        ans=root.val
        def dfs(node):
            if not node:
                return None
            nonlocal i
            nonlocal ans
            dfs(node.left)
            if node:
                i+=1
                if i==k:
                    ans=node.val
            dfs(node.right)
        dfs(root)
        return ans
