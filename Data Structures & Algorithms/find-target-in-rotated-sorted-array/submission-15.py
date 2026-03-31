class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            m=(r+l)//2
            t=[l,m,r]
            for i in t:
                if nums[i]==target:
                    return i
            if l<r and nums[l]<nums[m]:
                if l<r and nums[l]<target<nums[m]:
                    r=m-1
                else:
                    l=m+1
            else:
                if l<r and nums[m]<target<nums[r]:
                    l=m+1
                else:
                    r=m-1
        return -1
        