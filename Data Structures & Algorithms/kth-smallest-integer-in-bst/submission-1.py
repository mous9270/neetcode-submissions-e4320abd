# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans,c=0,0
        def dfs(node):
            nonlocal c
            nonlocal ans
            if node:
                dfs(node.left)
                c+=1
                if c==k:
                    ans=node.val
                
                dfs(node.right)
        dfs(root)
        return ans
        # ans=[]
        # return self.dfs(root, ans)
    # def dfs(self, node, ans: list):
    #     if node:
    #         self.dfs(node.left, ans)
    #         ans.append(node.val)
    #         if len(ans)==k:
    #             return ans
    #         self.dfs(node.right, ans)
        
        
        