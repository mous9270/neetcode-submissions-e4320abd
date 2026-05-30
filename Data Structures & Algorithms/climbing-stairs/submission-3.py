class Solution:
    def climbStairs(self, n: int) -> int:
        m={}
        for i in range(3):
            m[i]=i
        for i in range(n+1):
            if i not in m:
                m[i]=m[i-1]+m[i-2]
        return m[n]