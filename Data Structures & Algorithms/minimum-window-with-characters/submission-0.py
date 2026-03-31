class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        mt={}
        for i in t:
            mt[i]=mt.get(i, 0)+1
        ms={}
        ans, ansLen=[-1,-1], float("inf")
        l=0
        have, want=0, len(mt)
        for r in range(len(s)):
            ms[s[r]]=ms.get(s[r], 0)+1
            if s[r] in mt and mt[s[r]]==ms[s[r]]:
                have+=1
            while have==want:
                if r-l+1<ansLen:
                    ans=[l,r]
                    ansLen=r-l+1


                ms[s[l]]-=1
                if s[l] in mt and ms[s[l]]<mt[s[l]]:
                    have-=1
                l+=1
        l,r=ans
        return s[l:r+1] if ansLen!=float("inf") else ""
            