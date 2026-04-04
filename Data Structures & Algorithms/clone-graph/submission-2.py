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
            if not node:
                return None
            if node not in m:
                m[node]=Node(node.val)
                for n in node.neighbors:
                    dfs(n)
        dfs(node)
        for i in m:
            for j in i.neighbors:
                m[i].neighbors.append(m[j])
        return m[node]


        