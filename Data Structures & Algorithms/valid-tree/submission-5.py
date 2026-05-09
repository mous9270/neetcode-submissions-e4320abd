class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        m={i:[] for i in range(n)}
        for  i in edges:
            m[i[0]].append(i[1])
            m[i[1]].append(i[0])
        visiting=set()
        visited=set()
        def dfs(i,prev):
            if i in visiting:
                return False
            if i in visited:
                return True
            visiting.add(i)
            for j in m[i]:
                if j==prev:
                    continue
                if not dfs(j,i):
                    return False
            visiting.remove(i)
            visited.add(i)
            return True

        
        # for i in range(n):
        #     if not dfs(i,-1):
        #         return False
        return dfs(0,-1) and len(visited) == n