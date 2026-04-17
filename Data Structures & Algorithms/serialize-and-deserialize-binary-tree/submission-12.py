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
        def dfs(node):
            nonlocal s
            if node:
                s+=str(node.val)+','
                dfs(node.left)
                dfs(node.right)
            else:
                s+='N'+','
        dfs(root)
        return s

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        dd=data.split(',')
        d=dd[:-1]
        i=0
        def sub():
            nonlocal i
            if d[i]=='N':
                i+=1
                return None
                
            else:
                node=TreeNode(int(d[i]), None, None)
                i+=1
                node.left=sub()
                node.right=sub()
            return node
        return sub()
