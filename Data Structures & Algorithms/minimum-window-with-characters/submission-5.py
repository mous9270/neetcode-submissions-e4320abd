class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mt={}
        for i in t:
            mt[i]=mt.get(i, 0)+1
        ms={}
        have, need=0, len(mt)
        al, alen=0, float('inf')
        l=0
        for r in range(len(s)):
            ms[s[r]]=ms.get(s[r], 0)+1
            if s[r] in mt and mt[s[r]]==ms[s[r]]:
                have+=1
            while have==need:
                if r-l+1<alen:
                    al=l
                    alen=r-l+1
                ms[s[l]]-=1
                if s[l] in mt and mt[s[l]]>ms[s[l]]:
                    have-=1
                l+=1
        return s[al:al+alen] if alen!=float('inf') else ""
        