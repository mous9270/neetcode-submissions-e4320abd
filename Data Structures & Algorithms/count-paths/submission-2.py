class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        p=min(m,n)
        q=max(m,n)
        dp=[1]*p
        for i in range(q):
            for j in range(p):
                if i==0 or j==0:
                    continue
                dp[j]+=dp[j-1]
        return dp[-1]
                