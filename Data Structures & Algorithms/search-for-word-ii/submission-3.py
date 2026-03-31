class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores the complete word at the leaf node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. Build the Trie
        root = TrieNode()
        for w in words:
            node = root
            for char in w:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = w
        
        res = []
        rows, cols = len(board), len(board[0])
        
        # 2. Define the Backtracking function
        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
            
            curr_node = node.children[char]
            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None # Avoid duplicates
            
            # Mark the cell as visited
            board[r][c] = "#"
            
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    dfs(nr, nc, curr_node)
            
            # Backtrack: restore the cell
            board[r][c] = char

        # 3. Start searching from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
                
        return res