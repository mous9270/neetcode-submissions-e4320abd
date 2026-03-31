# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=root.val
        def mps(node):
            nonlocal ans
            if not node:
                return 0
            lps=mps(node.left)
            rps=mps(node.right)
            lps=max(lps, 0)
            rps=max(rps, 0)
            ans=max(ans, lps+node.val+rps)
            return max(lps, rps)+node.val
        mps(root)
        return ans

