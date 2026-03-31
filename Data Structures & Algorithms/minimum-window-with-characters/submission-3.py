class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mt={}
        for i in t:
            mt[i]=mt.get(i, 0)+1
        ms={}
        have,need=0, len(mt)
        ansL, ansLen=0, float('inf')
        l,r=0, 0
        while r<len(s):
            ms[s[r]]=ms.get(s[r], 0)+1
            if s[r] in mt and mt[s[r]]==ms[s[r]]:
                have+=1
            while have==need:
                if ansLen>r-l+1:
                    ansLen=r-l+1
                    ansL=l
                ms[s[l]]-=1
                if s[l] in mt and ms[s[l]]<mt[s[l]]:
                    have-=1
                l+=1
            r+=1
        return s[ansL:ansL+ansLen] if ansLen!=float('inf') else ""