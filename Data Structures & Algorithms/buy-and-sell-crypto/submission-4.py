class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        ans=0
        p=prices
        while r<len(prices):
            p=prices[r]-prices[l]
            if p>0:
                ans=max(ans,p)
                r+=1
            else:
                l=r
                r=r+1
        return ans
