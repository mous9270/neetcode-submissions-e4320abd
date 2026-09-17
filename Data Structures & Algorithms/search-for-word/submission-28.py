class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
      m,n=len(board),len(board[0])
    #   if len(board)==1:
    #     return board[0][0]==word
      def dfs(i,j,k):
        # if k==len(word):
        #   return True
        if board[i][j]==word[k]:
            k+=1
            if k==len(word):
                return True
            t=board[i][j]
            board[i][j]='#'
            for a,b in [(0,1),(0,-1),(1,0),(-1,0)]:
                r,c=i+a,j+b
                if 0<=r<m and 0<=c<n and dfs(r,c,k):
                    return True
            board[i][j]=t
            return False
      for i in range(m):
        for j in range(n):
          if board[i][j]==word[0]:
            if dfs(i,j,0):
              return True
      return False
      
        