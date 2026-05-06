class TrieNode:
    def __init__(self):
        self.children={}
        self.word=None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for i in words:
            curr=root
            for j in i:
                if j not in curr.children:
                    curr.children[j]=TrieNode()
                curr=curr.children[j]
            curr.word=i
        

        m,n=len(board),len(board[0])
        ans=[]
        def dfs(i,j,node):
            t=board[i][j]
            if t not in node.children:
                return
            node=node.children[t]
            if node.word:
                ans.append(node.word)
                node.word=None
           
            board[i][j]='#'
            for a,b in [(0,1),(1,0),(0,-1),(-1,0)]:
                r,c =i+a,j+b
                if 0<=r<m and 0<=c<n:
                    dfs(r,c, node)
            board[i][j]=t  
        for i in range(m):
            for j in range(n):
                dfs(i,j,root)
        return ans
