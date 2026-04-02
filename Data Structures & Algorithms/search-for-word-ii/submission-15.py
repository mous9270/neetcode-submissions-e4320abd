class TrieNode:
    def __init__(self):
        self.children={}
        self.word=None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for word in words:
            curr=root
            for c in word:
                if c not in curr.children:
                    curr.children[c]=TrieNode()
                curr=curr.children[c]
            curr.word=word
        m,n=len(board), len(board[0])
        ans=[]
        def dfs(i,j,curr):
            t=board[i][j]
            if t not in curr.children:
                return
            board[i][j]='#'
            curr=curr.children[t]
            if curr.word:
                ans.append(curr.word)
                curr.word=None
            for a,b in [(0,1), (1,0), (0,-1), (-1,0)]:
                r,c=i+a, j+b
                if 0<=r<m and 0<=c<n:
                    dfs(r,c,curr)
            board[i][j]=t

        for i in range(m):
            for j in range(n):
                dfs(i,j,root)
        return ans