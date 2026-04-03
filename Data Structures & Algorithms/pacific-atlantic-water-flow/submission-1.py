class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        sp = set() # Pacific reachable
        sa = set() # Atlantic reachable
        
        def dfs(r, c, visit_set, prev_height):
            # 1. Check boundaries
            # 2. Check if already visited to prevent infinite loops
            # 3. Check if current height is >= previous (moving uphill)
            if (r < 0 or c < 0 or r == m or c == n or 
                (r, c) in visit_set or heights[r][c] < prev_height):
                return
            
            visit_set.add((r, c))
            
            # Explore neighbors
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visit_set, heights[r][c])

        # Start DFS from the left and right edges (Rows)
        for r in range(m):
            dfs(r, 0, sp, heights[r][0])       # Left edge (Pacific)
            dfs(r, n - 1, sa, heights[r][n - 1]) # Right edge (Atlantic)
            
        # Start DFS from the top and bottom edges (Columns)
        for c in range(n):
            dfs(0, c, sp, heights[0][c])       # Top edge (Pacific)
            dfs(m - 1, c, sa, heights[m - 1][c]) # Bottom edge (Atlantic)
            
        # The answer is the intersection of both sets
        ans = []
        for r in range(m):
            for c in range(n):
                if (r, c) in sp and (r, c) in sa:
                    ans.append([r, c])
                    
        return ans
