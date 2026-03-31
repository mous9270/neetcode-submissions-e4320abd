# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=collections.deque()
        # curr=root
        ans=[]
        q.append(root)
        while q:

            t=[]
            for i in range(len(q)):
                k=q.popleft()
                if k:
                    t.append(k.val)
                    q.append(k.left)
                    q.append(k.right)
            ans.append(t)
        return ans[:-1]
                
