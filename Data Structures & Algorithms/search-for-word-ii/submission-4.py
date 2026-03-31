class TrieNode:
    def __init__(self):
        self.children={}
        self.word=None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for w in words:
            curr=root
            for c in w:
                if c not in curr.children:
                    curr.children[c]=TrieNode()
                curr=curr.children[c]
            curr.word=w

        def dfs(i,j,curr):
            t=board[i][j]
            if t not in curr.children:
                return
            
            curr=curr.children[t]
            if curr.word:
                ans.append(curr.word)
                curr.word=None
            board[i][j]='#'
            for a,b in [(1,0),(0,1),(-1,0),(0,-1)]:
                r,c=i+a, j+b
                if 0<=r<m and 0<=c<n:
                    dfs(r,c, curr)
            board[i][j]=t
        
        m,n=len(board), len(board[0])
        ans=[]

        for i in range(m):
            for j in range(n):
                dfs(i,j,root)
        return ans