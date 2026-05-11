class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        m={i:set() for word in words for i in word}
        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            k=min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:k]==w2[:k]:
                return ""
            for j in range(k):
                if w1[j]!=w2[j]:
                    m[w1[j]].add(w2[j])
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
            for j in m[i]:
                if not dfs(j):
                    return False
            visiting.remove(i)
            visited.add(i)
            ans.append(i)
            return True
        for i in m:
            if not dfs(i):
                return ""
        return ''.join(ans[::-1])


            