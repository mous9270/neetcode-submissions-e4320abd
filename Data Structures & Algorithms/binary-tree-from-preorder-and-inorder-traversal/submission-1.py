# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        ans=curr=TreeNode()
        curr.val=preorder[0]
        x=inorder.index(preorder[0])
        y=len(inorder[:x])
        curr.left=self.buildTree(preorder[1:y+1], inorder[:x] )
        curr.right=self.buildTree(preorder[y+1:], inorder[x+1:])
        return ans
        
        