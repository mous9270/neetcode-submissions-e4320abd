class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        ans=0
        while r<len(prices):
            p=prices[r]-prices[l]
            if p>ans:
                ans=p
            if p<0:
                l=r
                r=l+1
            else:
                r+=1
        return ans