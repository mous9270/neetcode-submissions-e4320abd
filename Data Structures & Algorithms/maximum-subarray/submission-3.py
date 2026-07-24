class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        l,r=0,0
        ans=float('-inf')
        while r<len(nums):
            s=sum(nums[l:r+1])
            if s<0:
                l=r+1
                r=l
            else:
                if s>ans:
                    ans=s
                r+=1
        return ans if ans!=float('-inf') else max(nums)

        