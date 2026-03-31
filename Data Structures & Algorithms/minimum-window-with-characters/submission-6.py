class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mt={}
        for i in t:
            mt[i]=mt.get(i, 0)+1
        # return mt
        ms={}
        ansL, ansLen=0, float('inf')
        have, need=0, len(mt)
        l,r=0,0
        while r<len(s):
            ms[s[r]]=ms.get(s[r], 0)+1
            if s[r] in mt and ms[s[r]]==mt[s[r]]:
                have+=1
            while l<=r and have==need:
                if ansLen>r-l+1:
                    ansL=l
                    ansLen=r-l+1
                ms[s[l]]-=1
                if s[l] in mt and mt[s[l]]>ms[s[l]]:
                    have-=1
                l+=1
            r+=1
        return s[ansL:ansL+ansLen] if ansLen!=float('inf') else ""
        
        