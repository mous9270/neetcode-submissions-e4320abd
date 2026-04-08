class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        m={i:[] for i in range(n)}
        for i in edges:
            m[i[0]].append(i[1])
            m[i[1]].append(i[0])
        visit=set()
        def dfs(i,pre):
            if i in visit:
                return False
            visit.add(i)
            for j in m[i]:
                if j==pre:
                    continue
                if not dfs(j,i):
                    return False
            
            return True
        return dfs(0,-1) and len(visit)==n