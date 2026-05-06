class WordDictionary:

    def __init__(self):
        self.children={}
        self.word=None

    def addWord(self, word: str) -> None:
        curr=self
        for i in word:
            if i not in curr.children:
                curr.children[i]=WordDictionary()
            curr=curr.children[i]
        curr.word=word
        

    def search(self, word: str) -> bool:
        def dfs(node, word):
            for i in range(len(word)):
                j=word[i]
                if j!='.':
                    if j not in node.children:
                        return False
                    node=node.children[j]
                else:
                    for child in node.children.values():
                        if dfs(child, word[i+1:]):
                            return True
                    return False
            return node.word!=None

        return dfs(self, word)
        # return self.children
        
