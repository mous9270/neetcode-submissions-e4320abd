class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0, len(nums)-1
        ans=nums[0]
        while l<r:
            m=(r+l)//2
            ans=min(ans, nums[l], nums[m], nums[r])
            if l<r and nums[l]<nums[m]:
                l=m
            else:
                r=m
        return ans
        