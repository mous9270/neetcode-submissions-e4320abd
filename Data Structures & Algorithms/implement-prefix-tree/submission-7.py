class PrefixTree:

    def __init__(self):
        self.children={}
        self.word=None

    def insert(self, word: str) -> None:
        curr=self
        for i in word:
            if i not in curr.children:
                curr.children[i]=PrefixTree()
            curr=curr.children[i]
        curr.word=word


    def search(self, word: str) -> bool:
        curr=self
        for i in word:
            if i not in curr.children:
                return False
            curr=curr.children[i]
        return curr.word==word
        

    def startsWith(self, prefix: str) -> bool:
        curr=self
        for i in prefix:
            if i not in curr.children:
                return False
            curr=curr.children[i]
        return True
        
        