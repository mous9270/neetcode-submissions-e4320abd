class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        d = self.trie
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d["#"] = True   # mark end of word

    def search(self, word: str) -> bool:

        def dfs(i, node):
            if i == len(word):
                return "#" in node

            c = word[i]

            if c == ".":
                for child in node:
                    if child != "#" and dfs(i + 1, node[child]):
                        return True
                return False
            else:
                if c not in node:
                    return False
                return dfs(i + 1, node[c])

        return dfs(0, self.trie)