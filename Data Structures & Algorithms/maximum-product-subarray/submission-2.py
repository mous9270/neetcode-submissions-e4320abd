class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=float('-inf')
        p,s=1,1
        n=len(nums)
        for i in range(n):
            if p==0:
                p=1
            if s==0:
                s=1
            p*=nums[i]
            s*=nums[n-i-1]
            ans=max(ans,p,s)
        return ans
