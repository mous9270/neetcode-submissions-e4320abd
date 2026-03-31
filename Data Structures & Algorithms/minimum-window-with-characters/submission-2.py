class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        mt={}
        for i in t:
            mt[i]=mt.get(i, 0)+1
        have, need=0, len(mt)
        ms={}
        l,r=0,0
        ans=[0, float('inf')]
        while r<len(s):
            ms[s[r]]=ms.get(s[r], 0)+1
            if s[r] in mt and ms[s[r]]==mt[s[r]]:
                have+=1
            while have==need:
                if r-l+1<ans[1]:
                    ans[1]=r-l+1
                    ans[0]=l
                ms[s[l]]-=1
                if s[l] in mt and ms[s[l]]<mt[s[l]]:
                    have-=1
                l+=1
            r+=1
        return s[ans[0]:ans[0]+ans[1]] if ans[1]!=float('inf') else ""

