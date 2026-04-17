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
            lms=mps(node.left)
            rms=mps(node.right)
            lms=max(lms, 0)
            rms=max(rms, 0)
            ans=max(ans, lms+rms+node.val)
            return max(lms,rms)+node.val
        mps(root)
        return ans