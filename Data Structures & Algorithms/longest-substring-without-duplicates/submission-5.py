class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        t=collections.deque()
        ans=0
        while r<len(s):
            if s[r] not in t:
                t.append(s[r])
                ans=max(ans,len(t))
                r+=1
            else:
                t.popleft()
                l+=1
        return ans