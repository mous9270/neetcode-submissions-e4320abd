class Solution:
    def climbStairs(self, n: int) -> int:
        m={}
        for i in range(3):
            m[i]=i
        for i in range(3,n+1):
            m[i]=m[i-1]+m[i-2]
        return m[n]