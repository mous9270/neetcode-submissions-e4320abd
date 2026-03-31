class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        w=len(word)
        def dfs(i,j, k):
            if board[i][j]!=word[k]:
                return False
            if k<w and board[i][j]==word[k]:
                k+=1
            if k==w:
                return True
            t=board[i][j]
            board[i][j]='#'
            for a,b in [(0,1), (1,0), (0,-1), (-1,0)]:
                r,c=i+a, j+b
                if 0<=r<m and 0<=c<n and dfs(r,c,k):
                    return True
            board[i][j]=t

        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False