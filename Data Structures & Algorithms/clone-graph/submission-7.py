"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        m={}
        visited=set()
        if not node:
            return None
        def dfs(node):
            if node in visited:
                return
            if node not in m:
                m[node]=Node(node.val)
                for n in node.neighbors:
                    dfs(n)
                    m[node].neighbors.append(m[n])
                    
            visited.add(node)
        
        dfs(node)
       
        return m[node]
