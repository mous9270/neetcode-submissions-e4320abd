class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        ans=0
        while r<len(prices):
            p=prices[r]-prices[l]
            ans=max(ans, p)
            if p<0:
                l=r
                r+=1
            else:
                r+=1
        return ans

        