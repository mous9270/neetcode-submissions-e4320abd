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
        def sub(root):
            nonlocal s
            if root:
                s+=str(root.val)+","
                sub(root.left)
                sub(root.right)
            else:
                s+="N"+","
            # if root.left:
                
            # else:
            #     s+="N"
            # if root.right:
                
            # else:
            #     s+="N"
        sub(root)
        return s

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        dd=data.split(",")
        d=dd[:-1]
        i=0
        def dfs():
            nonlocal i
            if d[i]=="N":
                i+=1
                return None
            node=TreeNode(int(d[i]))
            i+=1
            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()
    

        
        
        
