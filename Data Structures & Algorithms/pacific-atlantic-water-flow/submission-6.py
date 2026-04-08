class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights),len(heights[0])
        sp,sa=set(),set()
        ans=[]
        def dfs(i,j,seen,prev):
            if 0<=i<m and 0<=j<n and (i,j) not in seen and heights[i][j]>=prev:
                seen.add((i,j))
                for a,b in [(0,1),(1,0),(0,-1),(-1,0)]:
                    r,c=i+a, j+b
                    dfs(r,c,seen,heights[i][j])
        for i in range(m):
            dfs(i,0,sp,heights[i][0])
            dfs(i,n-1,sa,heights[i][n-1])
        for j in range(n):
            dfs(0,j,sp,heights[0][j])
            dfs(m-1,j,sa,heights[m-1][j])

        for i in range(m):
            for j in range(n):
                if (i,j) in sp and (i,j) in sa:
                    ans.append((i,j))
        return ans