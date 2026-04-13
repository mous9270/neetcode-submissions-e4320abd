class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        g={char:set() for word in words for char in word}
        for i in range(len(words)-1):
            w1,w2=words[i],words[i+1]
            m=min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:m]==w2[:m]:
                return ""
            for j in range(m):
                if w1[j]!=w2[j]:
                    g[w1[j]].add(w2[j])
                    break
        visiting=set()
        visited=set()
        ans=[]
        def dfs(i):
            if i in visiting:
                return False
            if i in visited:
                return True
            visiting.add(i)
            
            for j in g[i]:
                if not dfs(j):
                    return False
            visiting.remove(i)
            visited.add(i)
            ans.append(i)
            return True

        for i in g:
            if not dfs(i):
                return ""
        return ''.join(ans[::-1])
        