class Solution:
    def climbStairs(self, n: int) -> int:
        m={0:0,1:1,2:2}
        if n in m:
            return m[n]
        for i in range(3,n+1):
            m[i]=m[i-1]+m[i-2] 
        return m[n]