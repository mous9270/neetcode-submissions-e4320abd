class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0, len(nums)-1
        ans=nums[0]
        while l<r:
            m=(r+l)//2
            ans=min(ans, nums[m],nums[l],nums[r])
            if nums[l]<nums[m] and nums[m]>nums[r]:
                l=m
            # elif nums[l]>nums[m] and nums[m]<nums[r]:
            #     r=m
            else:
                r=m
        return ans