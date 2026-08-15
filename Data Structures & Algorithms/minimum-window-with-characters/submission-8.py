class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ms,mt={},{}
        for i in t:
            mt[i]=mt.get(i,0)+1
        have,need=0,len(mt)
        l,r=0,0
        ans,ans_len=float('inf'),float('inf')
        while r<len(s):
            ms[s[r]]=ms.get(s[r],0)+1
            if s[r] in mt:
                if ms[s[r]]==mt[s[r]]:
                    have+=1
                if have==need:
                    while have==need:
                        if (r-l+1)<ans_len:
                            ans=l
                            ans_len=r-l+1
                        ms[s[l]]-=1
                        if s[l] in mt and ms[s[l]]<mt[s[l]]:
                            have-=1
                        l+=1
            r+=1
    
        return s[ans:ans+ans_len] if ans!=float("inf") else ""
