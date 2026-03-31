# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=root.val
        def mps(root):
            nonlocal ans
            if not root:
                return 0
            lms=mps(root.left)
            rms=mps(root.right)
            lms=max(lms, 0)
            rms=max(rms, 0)
            ans=max(ans, root.val+lms+rms)
            return root.val+max(lms, rms)
        mps(root)
        return ans