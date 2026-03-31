class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board), len(board[0])
        w=len(word)
        if m==1 and n==1:
            return board[0][0]==word
        def dfs(i,j,ix):
            if ix==w:
                return True
            if board[i][j]!=word[ix]:
                return False
            
            t=board[i][j]
            board[i][j]='#'
            for a,b in [(1,0), (0,1), (-1,0), (0,-1)]:
                r,c=i+a, j+b
                if 0<=r<m and 0<=c<n and dfs(r,c,ix+1):
                    return True
            board[i][j]=t
            return False
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False