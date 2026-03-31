class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r=0,0
        m={}
        ans=0
        while r<len(s):
            m[s[r]]=m.get(s[r],0)+1
            if abs((r-l+1)-max(m.values()))<=k:
                ans=max(ans, r-l+1)
            else:
                while l<r and abs((r-l+1)-max(m.values()))>k:
                    m[s[l]]-=1
                    l+=1
            r+=1
        return ans

