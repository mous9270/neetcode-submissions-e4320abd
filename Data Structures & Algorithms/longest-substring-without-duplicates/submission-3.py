class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        ans=0
        t= collections.deque()
        while r<len(s):
            if s[r] in t:
                t.popleft()
                l+=1
            else:
                t.append(s[r])
                ans=max(ans, len(t))
                r+=1
        return ans

