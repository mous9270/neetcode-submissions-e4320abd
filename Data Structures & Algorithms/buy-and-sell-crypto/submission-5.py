class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        ans=0
        while r<len(prices):
            p=prices[r]-prices[l]
            if p>0:
                ans=max(p,ans)
                r+=1
            else:
                l=r
                r+=1
        return ans
