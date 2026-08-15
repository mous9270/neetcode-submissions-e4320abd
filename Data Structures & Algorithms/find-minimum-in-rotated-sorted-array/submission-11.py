class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        l,r=0,len(nums)-1
        ans=float('inf')
        while l<r:
            m=(r+l)//2
            ans=min(ans, nums[m], nums[l],nums[r])
            if nums[m]>nums[l]:
                l=m
            else:
                r=m
        return ans