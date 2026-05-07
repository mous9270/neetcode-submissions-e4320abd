class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m=len(heights)
        n=len(heights[0])
        sp,sa=set(),set()
        ans=[]
        def dfs(i,j,seen,prev):
            if 0<=i<m and 0<=j<n and (i,j) not in seen and heights[i][j]>=prev:
                seen.add((i,j))
                for a,b in [(0,1),(1,0),(0,-1),(-1,0)]:
                    r,c=a+i,j+b
                    dfs(r,c,seen,heights[i][j])
            


        for i in range(m):
            dfs(i,0,sp,heights[i][0])
            dfs(i,n-1,sa,heights[i][n-1])
        for j in range(n):
            dfs(0,j,sp,heights[0][j])
            dfs(m-1,j,sa,heights[m-1][j])
        for i in sp:
            if i in sa:
                ans.append(i)
        return ans