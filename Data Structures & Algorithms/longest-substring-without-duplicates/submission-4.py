class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        l,r=0,0
        m=collections.deque()
        while r<len(s):
            if s[r] in m:
                m.popleft()
                l+=1
            else:
                m.append(s[r])
                ans=max(ans, len(m))
                r+=1
        return ans