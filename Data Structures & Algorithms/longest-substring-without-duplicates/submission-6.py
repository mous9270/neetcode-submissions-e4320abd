class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        m={}
        ans=0
        while r<len(s):
            if s[r] not in m:
                m[s[r]]=1
                ans=max(r-l+1, ans)
                r+=1
            else:
                while l<r and s[r] in m:
                    m.pop(s[l])
                    l+=1
        return ans


        