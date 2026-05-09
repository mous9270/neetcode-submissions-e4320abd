class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        m={i:[] for i in range(n)}
        ans=0
        for i in range(len(edges)):
            m[edges[i][0]].append(edges[i][1])
            m[edges[i][1]].append(edges[i][0])
        visiting=set()
        visited=set()
        def dfs(i,prev):
            if i in visiting:
                return
            if i in visited:
                return
            visiting.add(i)
            for j in m[i]:
                if j == prev:
                    continue
                dfs(j,i)
            visiting.remove(i)
            visited.add(i)
          
        for i in range(n):
            if not i in visited:
                ans+=1
                dfs(i,-1)
        return ans