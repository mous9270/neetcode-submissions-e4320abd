# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        s=""
        def sub(node):
            nonlocal s
            if node:
                s+=str(node.val)+','
                sub(node.left)
                sub(node.right)
            else:
                s+='N'+','
            
        sub(root)
        return s

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        dd=data.split(',')
        d=dd[:-1]
        i=0
        def dfs():
            nonlocal i
            if i<len(d):
                if d[i]!='N':
                    node=TreeNode(int(d[i]))
                    i+=1
                    node.left=dfs()
                    node.right=dfs()
                else:
                    node=None
                    i+=1
            # node.val=d[i] or 'N'
            
            return node
        return dfs()
