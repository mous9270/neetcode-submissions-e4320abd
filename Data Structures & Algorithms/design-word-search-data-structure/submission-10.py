class WordDictionary:

    def __init__(self):
        self.children={}
        self.word=None

    def addWord(self, word: str) -> None:
        curr=self
        for c in word:
            if c not in curr.children:
                curr.children[c]=WordDictionary()
            curr=curr.children[c]
        curr.word=word
        

    def search(self, word: str) -> bool:
        def dfs(node, word):
            for i in range(len(word)):
                c=word[i]
                if c!='.':
                    if c not in node.children:
                        return False
                    node=node.children[c]
                else:
                    for child in node.children.values():
                        if dfs(child, word[i+1:]):
                            return True
                    return False
            return node.word!=None

        return dfs(self, word)
        
