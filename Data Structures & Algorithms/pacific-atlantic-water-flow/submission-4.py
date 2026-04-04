class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights), len(heights[0])
        ans=[]
        sp,sa=set(),set()
        def dfs(seen,i,j,prev):
            if 0<=i<m and 0<=j<n and (i,j) not in seen and heights[i][j]>=prev:
                seen.add((i,j))
                for a,b in [(0,1),(1,0),(0,-1),(-1,0)]:
                    r,c=i+a,j+b
                    if 0<=r<m and 0<=c<n:
                        dfs(seen,r,c,heights[i][j])


        for i in range(m):
            dfs(sp,i,0,heights[i][0])
            dfs(sa,i,n-1,heights[i][n-1])

        for j in range(n):
            dfs(sp,0,j,heights[0][j])
            dfs(sa,m-1,j,heights[m-1][j])
        
        for i in range(m):
            for j in range(n):
                if (i,j) in sp and (i,j) in sa:
                    ans.append((i,j))
        return ans