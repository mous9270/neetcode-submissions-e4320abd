class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        if m==1 and n==1:
            return board[0][0]==word
        w=len(word)
        def dfs(p, ix):
            i,j=p
            if w==ix:
                return True
            if word[ix]!= board[i][j]:
                return False
            temp=board[i][j]
            board[i][j]='#'
            for i_off, j_off in [(0,1), (1,0), (0,-1), (-1,0)]:
                r,c=i+i_off, j+j_off
                if 0<=r<m and 0<=c<n and dfs((r,c), ix+1):
                    return True
            board[i][j]=temp
            return False

        for i in range(m):
            for j in range(n):
                if dfs((i,j), 0):
                    return True
        return False