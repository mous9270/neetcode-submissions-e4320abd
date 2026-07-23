class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d={}
        a,b=m-1,n-1
        t=a+b+1
        d[0]=1
        for i in range(1,t):
            d[i]=d[i-1]*i
        
        return d[a+b]//(d[a]*d[b])
