class PrefixTree:

    def __init__(self):
        self.children={}
        self.word=None

    def insert(self, word: str) -> None:
        curr=self
        for c in word:
            if c not in curr.children:
                curr.children[c]=PrefixTree()
            curr=curr.children[c]
        curr.word=word


    def search(self, word: str) -> bool:
        curr=self
        for c in word:
            if c not in curr.children:
                return False
            curr=curr.children[c]
        return curr.word==word
        

    def startsWith(self, prefix: str) -> bool:
        curr=self
        for c in prefix:
            if c not in curr.children:
                return False
            curr=curr.children[c]
        return True
        
        