class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        ans=0
        def dfs(i,j):
            grid[i][j]='0'
            for a,b in [(0,1),(1,0),(0,-1),(-1,0)]:
                r,c=i+a,j+b
                if 0<=r<m and 0<=c<n:
                    if grid[r][c]=='1':
                        dfs(r,c)

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    ans+=1
                    dfs(i,j)
        return ans