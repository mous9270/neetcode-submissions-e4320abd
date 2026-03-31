class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s)==1:
            return 1
        l,r=0,0
        ans=0
        t=set()
        while r<len(s):
            while r<len(s) and s[r] not in t:
                t.add(s[r])
                r+=1
            if r-l>ans:
                ans=r-l
            if r<len(s) and s[r] in t:
                while s[l]!=s[r]:
                    t.remove(s[l])
                    l+=1
                l+=1
            r+=1
        return ans


