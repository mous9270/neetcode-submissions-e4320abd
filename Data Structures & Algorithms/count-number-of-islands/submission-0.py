class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        ans=0
        def dfs(i,j):
            nonlocal ans
            if grid[i][j]=='1':
                grid[i][j]='0'
                for a,b in [(0,1),(1,0),(0,-1),(-1,0)]:
                    r,c=i+a,j+b
                    if 0<=r<m and 0<=c<n:
                        dfs(r,c)
                return True
                 
        for i in range(m):
            for j in range(n):
                if dfs(i,j):
                    ans+=1
        return ans