class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r=0,0
        ans=0
        m={}
        while r<len(s):
            m[s[r]]=m.get(s[r],0)+1
            if sum(m.values())-max(m.values())<=k:
                ans=max(ans, sum(m.values()))
                r+=1
            else:
                m[s[l]]-=1
                l+=1
                r+=1
        return ans

