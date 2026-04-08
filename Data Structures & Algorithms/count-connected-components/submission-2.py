class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        m={i:[] for i in range(n)}
        visit=set()
        ans=0
        for i in edges:
            m[i[0]].append(i[1])
            m[i[1]].append(i[0])
        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            for j in m[i]:
                dfs(j)
        for i in range(n):
            if i not in visit:
                ans+=1
                dfs(i)
                
        return ans
