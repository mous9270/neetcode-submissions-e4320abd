# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans=[]
        q=collections.deque()
        q.append(root)
        curr=root
        while q:
            t=[]
            for i in range(len(q)):
                k=q.popleft()
                if k:
                    t.append(k.val)
                    if k.left:
                        q.append(k.left)
                    if k.right:
                        q.append(k.right)
            ans.append(t)
        return ans

