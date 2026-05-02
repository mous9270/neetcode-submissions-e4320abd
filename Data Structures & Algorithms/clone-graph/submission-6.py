"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        m={}
        def dfs(node):
            if node in m:
                return
            m[node]=Node(node.val)
            for n in node.neighbors:
                dfs(n)
        dfs(node)
        visited=set()
        def sub(node):
            if node in visited:
                return
            visited.add(node)
            for n in node.neighbors:
                m[node].neighbors.append(m[n])
                sub(n)
            
        sub(node)
        return m[node]
