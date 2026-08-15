class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m={}
        l,r=0,0
        ans=0
        while r<len(s):
            m[s[r]]=m.get(s[r],0)+1
            if sum(m.values())-max(m.values())<=k:
                ans=max(ans,sum(m.values()))
            else:
                while l<r and sum(m.values())-max(m.values())>k:
                    m[s[l]]-=1
                    l+=1
            r+=1
        return ans
