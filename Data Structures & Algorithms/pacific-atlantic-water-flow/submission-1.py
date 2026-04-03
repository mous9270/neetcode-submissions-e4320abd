class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        sp = set() # Pacific reachable
        sa = set() # Atlantic reachable
        
        def dfs(i, j, visit_set, prev_height):
            # 1. Check boundaries
            # 2. Check if already visited to prevent infinite loops
            # 3. Check if current height is >= previous (moving uphill)
            # if (r < 0 or c < 0 or r == m or c == n or 
            #     (r, c) in visit_set or heights[r][c] < prev_height):
            #     return
            if 0<=i<m and 0<=j<n and (i,j) not in visit_set and heights[i][j]>=prev_height:
                visit_set.add((i, j))
                
                # Explore neighbors
                for a,b in [(0,1), (0,-1),(1,0), (-1,0)]:
                    r,c=i+a, j+b
                    dfs(r,c,visit_set,heights[i][j])

        # Start DFS from the left and right edges (Rows)
        for i in range(m):
            dfs(i, 0, sp, heights[i][0])       # Left edge (Pacific)
            dfs(i, n - 1, sa, heights[i][n - 1]) # Right edge (Atlantic)
            
        # Start DFS from the top and bottom edges (Columns)
        for j in range(n):
            dfs(0, j, sp, heights[0][j])       # Top edge (Pacific)
            dfs(m - 1, j, sa, heights[m - 1][j]) # Bottom edge (Atlantic)
            
        # The answer is the intersection of both sets
        ans = []
        for i in range(m):
            for j in range(n):
                if (i, j) in sp and (i, j) in sa:
                    ans.append([i, j])
                    
        return ans