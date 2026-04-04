class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        m=defaultdict(list)
        for i in edges:
            m[i[0]].append(i[1])
            m[i[1]].append(i[0])
        visit=set()
        ans=0
        def dfs(i,prev):
            if i in visit:
                return
            visit.add(i)
            for j in m[i]:
                if j==prev:
                    continue
                dfs(j,i)


        for i in range(n):
            if i not in visit:
                ans+=1
                dfs(i,-1)
        return ans