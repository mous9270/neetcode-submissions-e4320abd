class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        l,r=0, len(nums)-1
        ans=float('inf')
        while l<=r:
            m=(r+l)//2
            ans=min(ans,nums[m])
            if nums[l]<=nums[m] and nums[m]>nums[r]:
                l=m+1
            else:
                r=m-1
        return ans    