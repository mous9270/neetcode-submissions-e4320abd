class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        m={char:[] for word in words for char in word}
        for i in range(len(words)-1):
            k=min(len(words[i]), len(words[i+1]))
            if len(words[i])>len(words[i+1]) and words[i][:k]==words[i+1][:k]:
                return ""
            j=0
            while j<k and words[i][j]==words[i+1][j]:
                j+=1
            if j<k:
                m[words[i][j]].append(words[i+1][j])
        ans=[]
        visit={}
        def dfs(i):
            if i in visit:
                return visit[i]
            visit[i]=True
            for j in m[i]:
                if dfs(j):
                    return True
            visit[i]=False
            ans.append(i)
            return False
        for i in m:
            if dfs(i):
                return ""
        ans=ans[::-1]
        return "".join(ans)

        
        
